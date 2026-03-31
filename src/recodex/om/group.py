from .cache import Cache
from .base import LocalizedEntity
from .assignment import Assignment
from .user import User


class Group(LocalizedEntity):
    '''
    Wrapper for group data structure with additional features.
    '''

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

    def get_admins(self) -> list[User]:
        '''
        Gets the list of (primary) admins of the group.
        '''
        admins_ids = self._data.get("primaryAdminsIds") or []
        return [Cache.cache().get(User, admin_id) for admin_id in admins_ids]

    def get_all_admins(self) -> list[User]:
        '''
        Gets the list of all admins of the group (including secondary admins).
        '''
        admins_ids = self._data.get("privateData", "admins") or []
        return [Cache.cache().get(User, admin_id) for admin_id in admins_ids]

    def get_supervisors(self) -> list[User]:
        '''
        Gets the list of supervisors of the group.
        '''
        supervisors_ids = self._data.get("privateData", "supervisors") or []
        return [Cache.cache().get(User, supervisor_id) for supervisor_id in supervisors_ids]

    def get_observers(self) -> list[User]:
        '''
        Gets the list of observers of the group.
        '''
        observers_ids = self._data.get("privateData", "observers") or []
        return [Cache.cache().get(User, observer_id) for observer_id in observers_ids]

    def get_students(self) -> list[User]:
        '''
        Gets the list of students of the group.
        '''
        students_ids = self._data.get("privateData", "students") or []
        return [Cache.cache().get(User, student_id) for student_id in students_ids]

    def get_assignments(self) -> list[Assignment]:
        '''
        Gets the list of assignments of the group.
        '''
        assignments_ids = self._data.get("privateData", "assignments") or []
        return [Cache.cache().get(Assignment, assignment_id) for assignment_id in assignments_ids]

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
        groups_data = client.send_request("groups", "default", query_params=query).get_payload()

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

    @staticmethod
    def filter_factory_has_ancestor(group_id: str):
        def filter_has_ancestor(group):
            for aid in group.get("parentGroupsIds") or []:
                if aid == group_id:
                    return True
            return False

        return filter_has_ancestor
