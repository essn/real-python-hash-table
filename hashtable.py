class HashTable:
    def __init__(self, capacity):
        self.pairs = capacity * [None]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def _index(self, key):
        return hash(key) % len(self)

    def __delitem__(self, key):
        if key in self:
            self[key] = None
        else:
            raise KeyError(key)

    def __len__(self):
        return len(self.pairs)

    def __setitem__(self, key, value):
        self.pairs[self._index(key)] = (key, value)

    def __getitem__(self, key):
        pair = self.pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair[1]

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
