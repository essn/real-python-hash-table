from typing import NamedTuple, Any


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")

        self._slots = capacity * [None]

    @property
    def capacity(self):
        return len(self._slots)

    @property
    def values(self):
        return [pair.value for pair in self.slots]

    @property
    def slots(self):
        return {pair for pair in self._slots if pair}

    @property
    def keys(self):
        return {pair.key for pair in self.slots}

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def _index(self, key):
        return hash(key) % self.capacity

    def __delitem__(self, key):
        if key in self:
            self[key] = None
        else:
            raise KeyError(key)

    def __len__(self):
        return len(self.slots)

    def __setitem__(self, key, value):
        self._slots[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._slots[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
