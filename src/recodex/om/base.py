import datetime


class BaseEntity:
    '''
    Base class for all entities in the ReCodEx object model.
    '''
    default_timezone = datetime.timezone.utc

    def __init__(self, data: dict):
        self._data = data
        self._id = data.get("id")
        self._children = None
        if not self._id:
            raise Exception("Data structure must contain an 'id' field")

    def id(self):
        '''
        Returns the ID of the entity (all entities have an ID).
        '''
        return self._id

    def get(self, *args, default=None):
        '''
        Gets a value from the entity data structure by a path of keys and indices.
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
        Gets a value from the entity data structure by a path of keys and indices.
        If the path does not exist, raises an error.
        '''
        current = self.get(*args, default=self)
        if current is self:
            raise Exception(f"Path {'.'.join(map(str, args))} does not exist in the data structure")

        return current

    def get_ts(self, *args):
        '''
        Gets a timestamp value from the entity data structure by a path of keys and indices.
        If the path does not exist, returns None.
        '''
        ts = self.get(*args)
        if ts is None:
            return None
        if type(ts) is not int:
            raise Exception(f"Expected a timestamp (int) at path {'.'.join(map(str, args))}, got {type(ts).__name__}")

        # convert timestamp to datetime
        return datetime.datetime.fromtimestamp(ts, self.default_timezone)


class LocalizedEntity(BaseEntity):
    '''
    Wrapper for entities which have localized texts (like name and description) in multiple languages.
    '''

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
