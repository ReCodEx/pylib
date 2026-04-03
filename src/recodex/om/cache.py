from ..client import Client


class Cache:
    '''
    A cache for storing and retrieving entities from ReCodEx.
    '''
    _instance = None

    def __init__(self, client: Client):
        self._client = client
        self._caches = {
            "Assignment": {},
            "CommentThread": {},
            "Exercise": {},
            "Group": {},
            "Solution": {},
            "SolutionReview": {},
            "Submission": {},
            "User": {}
        }

    def has(self, entity: type, id: str) -> bool:
        '''
        Checks if an entity of the specified type and ID is present in the cache.
        '''
        if entity.__name__ not in self._caches:
            raise Exception(f"Unknown entity type {entity.__name__}")
        return id in self._caches[entity.__name__] and self._caches[entity.__name__][id] is not None

    def get(self, entity: type, id: str, strict: bool = True):
        '''
        Retrieves an entity of the specified type from the cache.
        The type is the class of the entity (like Group).
        '''
        if entity.__name__ not in self._caches:
            raise Exception(f"Unknown entity type {entity.__name__}")

        cache = self._caches[entity.__name__]
        if id not in cache:
            if self._client is None:
                raise Exception("Unable to fetch entity into a cache, no client instance was provided")

            obj = entity({"id": id})
            try:
                obj.refresh()  # this will fetch the data from the server and update the cache
            except Exception as e:
                if strict:
                    raise e
                obj = None
            cache[id] = obj

        return cache[id]

    def get_client(self) -> Client:
        '''
        Returns the client associated with this cache.
        '''
        if self._client is None:
            raise Exception("No client instance was provided to the cache")
        return self._client

    def set_client(self, client: Client):
        '''
        Sets the client associated with this cache (in case it needs to be injected later).
        '''
        self._client = client

    def inject(self, entity: type, objects):
        '''
        Injects one or multiple objects into the cache for a given entity type.
        The object(s) is an instance of base entity or an iterable (like a list), of specific entity.
        Returns a list of the injected objects in the same order as they were provided
        (not necessarily the same instances, but the corresponding objects which are stored in the cache).
        Single object is returned if one object (not in a list) was provided.
        '''
        if entity.__name__ not in self._caches:
            raise Exception(f"Unknown entity type {entity.__name__}")

        cache = self._caches[entity.__name__]

        single = type(objects) is entity
        if single:
            objects = [objects]

        result = []
        for obj in objects:
            if type(obj) is not entity:
                raise Exception(f"Expected object of type {entity.__name__}, got {type(obj).__name__}")
            if obj.id() in cache and type(cache[obj.id()]) is entity:
                cache[obj.id()].update(obj._data)  # update existing object in cache
            else:
                cache[obj.id()] = obj
            result.append(cache[obj.id()])

        return result[0] if single else result

    def update_raw(self, entity_name: str, data: dict):
        '''
        Updates the cache for a given entity type with the provided raw data.
        The data is a dictionary containing the entity data, including the ID.
        The entity type is specified by its name (like "Group").
        This method is used internally when refreshing entities, to update the cache with the new data.
        '''
        if entity_name not in self._caches:
            raise Exception(f"Unknown entity type {entity_name}")
        cache = self._caches[entity_name]
        id = data.get("id")
        if id is None:
            raise Exception("Data must contain an 'id' field to be updated in the cache")
        if id in cache and type(cache[id]).__name__ == entity_name:
            cache[id].update(data)  # update existing object in cache
        # no action is taken if the entity is not in the cache

    def remove(self, entity: type, id: str) -> bool:
        '''
        Removes an entity of the specified type and ID from the cache.
        Returns True if the entity was removed, False if it was not found in the cache.
        '''
        if entity.__name__ not in self._caches:
            raise Exception(f"Unknown entity type {entity.__name__}")
        cache = self._caches[entity.__name__]
        if id in cache:
            del cache[id]
            return True
        return False

    def clear(self, entity: type = None):
        '''
        Clears the cache for a given entity type, or all caches if no type is specified.
        '''
        if entity is not None:
            if entity.__name__ not in self._caches:
                raise Exception(f"Unknown entity type {entity.__name__}")
            self._caches[entity.__name__] = {}
        else:
            for key in self._caches.keys():
                self._caches[key] = {}

    def get_current_user(self):
        '''
        Gets the current user associated with the auth token used in the client.
        Returns None if the current user cannot be determined.
        '''
        from .user import User
        client = self.get_client()
        id = client.current_user_id
        if id is None:
            return None
        return self.get(User, id)

    @staticmethod
    def cache(client: Client = None) -> "Cache":
        '''
        Returns the singleton instance of the cache.
        '''
        if Cache._instance is None:
            Cache._instance = Cache(client)
        elif client is not None:
            Cache._instance.set_client(client)
        return Cache._instance
