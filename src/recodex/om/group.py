from .cache import Cache


class Group:
    '''
    Wrapper for group data structure with additional features.
    '''

    def __init__(self, data: dict):
        self._data = data
        self._id = data.get("id")
        self._children = None
        if not self._id:
            raise Exception("Group data structure must contain an 'id' field")

    def id(self):
        '''
        Returns the ID of the group.
        '''
        return self._id

    def get(self, *args, default=None):
        '''
        Gets a value from the group data structure by a path of keys and indices.
        If the path does not exist, returns the default value (no error).
        '''
        if len(args) == 0:
            raise Exception("At least one argument is required")

        current = self._data
        for arg in args:
            if type(current) is dict and arg in current:
                current = current[arg]
            elif type(current) is list and arg is int and arg < len(current):
                current = current[arg]
            else:
                return default

        return current

    def get_strict(self, *args):
        '''
        Gets a value from the group data structure by a path of keys and indices.
        If the path does not exist, raises an error.
        '''
        if len(args) == 0:
            raise Exception("At least one argument is required")

        current = self._data
        for arg in args:
            if type(current) is dict and arg in current:
                current = current[arg]
            elif type(current) is list and arg is int and arg < len(current):
                current = current[arg]
            else:
                raise Exception(f"Path {'.'.join(map(str, args))} does not exist in the group data structure")

        return current

    def get_localized_texts(self):
        '''
        Gets the localized texts of the group as a dictionary with locale as key and texts-dict as value.
        The texts have the following keys: id, locale, name, description, and createdAt (timestamp).
        '''
        return {text["locale"]: text for text in self._data.get("localizedTexts") or []}

    def get_name(self, locale='en'):
        '''
        Gets the localized name of the group.
        If the selected locale is not available, falls back to English or the first available locale.
        '''
        texts = self.get_localized_texts()
        if locale in texts and "name" in texts[locale]:
            return texts[locale]["name"]
        if "en" in texts and "name" in texts["en"]:
            return texts["en"]["name"]

        first = next(iter(texts.values()), None)
        return first["name"] if first and "name" in first else None

    def get_parent(self) -> "Group | None":
        '''
        Gets the parent group of the group, or None if it does not have a parent.
        '''
        parent_id = self._data.get("parentGroupId")
        if not parent_id:
            return None
        parent = Cache.cache().get(Group, parent_id)
        if not parent:
            raise Exception(f"Parent group with ID {parent_id} not found")

        return parent

    def _inject_child(self, child: "Group"):
        if self._children is None:
            self._children = []
        self._children.append(child)

    def get_children(self) -> list["Group"]:
        '''
        Gets the list of sub-groups of the group.
        '''
        if self._children is None:
            children_ids = self._data.get("childGroups") or []
            children = []
            for child_id in children_ids:
                child = Cache.cache().get(Group, child_id)
                if not child:
                    raise Exception(f"Child group with ID {child_id} not found")
                children.append(child)
            self._children = children

        return self._children

    #
    # static methods
    #

    @staticmethod
    def load_all(archived=False, instanceId: str = None, filter_by=None):
        '''
        Loads groups from the given data and returns a list of Group objects.
        - archived - whether to include archived groups (default: False)
        - instanceId - the ID of the instance to filter groups by (None = use current user's instance)
        - filter_by - a function to filter the loaded groups being returned (default: None)
        '''
        cache = Cache.cache()
        client = cache.get_client()
        query = {"archived": archived}
        if instanceId is not None:
            query["instanceId"] = instanceId
        groups_data = client.send_request("groups", "default", {}, {}, query).get_payload()

        groups = [Group(data) for data in groups_data or []]
        cache.inject(Group, groups)  # inject groups into cache

        # build children lists and in groups
        for group in groups:
            parent = group.get_parent()
            if parent:
                parent._inject_child(group)

        return list(filter(filter_by, groups)) if filter_by is not None else groups

    @staticmethod
    def filter_root(group) -> bool:
        '''
        A filter function applicable as argument for `load_all()` to select only root groups (groups without a parent).
        There should be only one such group (per instance).
        '''
        return not group.get("parentGroupId")
