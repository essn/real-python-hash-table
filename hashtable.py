from typing import NamedTuple, Any


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")

        self._slots = capacity * [None]

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

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

    def copy(self):
        return HashTable.from_dict(dict(self.slots), self.capacity)

    def __str__(self):
        slots = [f"{key!r}: {value!r}" for key, value in self.slots]
        return "{" + ", ".join(slots) + "}"

    def __iter__(self):
        yield from self.keys

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

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.slots) == set(other.slots)
