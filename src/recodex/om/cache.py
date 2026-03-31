from ..client import Client


class Cache:
    '''
    A cache for storing and retrieving entities from ReCodEx.
    '''
    _instance = None

    def __init__(self, client: Client):
        self._client = client
        self._caches = {
            "Group": {}
        }
        self._getters = {
            "Group": lambda client, id, _: client.send_request("groups", "detail", {}, {"id": id}).get_payload()
        }

    def get(self, entity: type, id: str):
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
            getter = self._getters.get(entity.__name__)
            if getter is None:
                raise Exception(f"{entity.__name__} with id {id} not found and no getter function is defined")
            data = getter(self._client, id, self)
            cache[id] = entity(data) if data is not None else None

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
        Injects objects into the cache for a given entity type.
        The objects is an iterable (like a list), of specific type
        '''
        if entity.__name__ not in self._caches:
            raise Exception(f"Unknown entity type {entity.__name__}")

        cache = self._caches[entity.__name__]
        for obj in objects:
            if type(obj) is not entity:
                raise Exception(f"Expected object of type {entity.__name__}, got {type(obj).__name__}")
            cache[obj.id()] = obj

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
