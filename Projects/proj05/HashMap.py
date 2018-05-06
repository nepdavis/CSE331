class HashMap:

    def __init__(self, load_factor = 1.00):

        # You may change the default maximum load factor
        self.max_load_factor = load_factor

        # Other initialization code can go here
        self.size = 0

        self.table = [[]] * 101

        self.keys_set = set()

        self.keys_ref = [[]] * 101

    def __len__(self):

        """Returns the size of the hash map"""

        return self.size

    def load(self):

        """Returns the average number of keys per slot"""

        return self.size / len(self.table)

    def __contains__(self, key):

        """Returns bool whether or not key is in hash map"""

        return key in self.keys_set

    def __getitem__(self, key):

        """
        Returns value associated with input key
        :param key: Key to retrive value for
        :return: Value
        """

        # Checks if key is in map
        if self.__contains__(key):

            # Get hashed key
            i = self.hash(key)

            # Get chain index for key
            chain_idx = self.keys_ref[i].index(key)

            # Return value
            return self.table[i][chain_idx]

        # If key not in hash map, raise error
        raise KeyError(key)

    def __setitem__(self, key, value):

        """
        Inserts key value pair into hash map
        :param key: Key for pair
        :param value: Value associated with key
        :return: None
        """

        # Get hashed key
        i = self.hash(key)

        # If key not already in hash map
        if key not in self.keys_set:

            # Increment size
            self.size += 1

            # Add key to set of keys for reference
            self.keys_set.add(key)

            # Append key location to keys reference hash table
            self.keys_ref[i].append(key)

            # Apped value to hash map chain
            self.table[i].append(value)

        # If key already in hash map
        else:

            # Get key index for hash map chain
            chain_idx = self.keys_ref[i].index(key)

            # Overwrite value in hash map
            self.table[i][chain_idx] = value

        # If load greater than maximum load factor
        if self.load() >= self.max_load_factor:

            # Call resize for hash map
            self.resize()

    def __delitem__(self, key):

        """
        Deletes key value pair from hash map
        :param key: Key to remove, along with associated value
        :return: None
        """

        # If key is in hash map
        if self.__contains__(key):

            # Get hashed key
            i = self.hash(key)

            # Get chain index of key value pair
            chain_idx = self.keys_ref[i].index(key)

            # Delete value associated with key in hash map
            del self.table[i][chain_idx]

            # Delete key from hash table
            del self.keys_ref[i][chain_idx]

            # Remove key from set of keys
            self.keys_set.remove(key)

            # Decrement size
            self.size -= 1

        # If key not in hash map
        else:

            # Raise error
            raise KeyError(key)

    def __iter__(self):

        """
        Iterates over all key value pairs in the hash map
        :return: Yields iterator
        """

        # For each key in set of keys
        for key in self.keys_set:

            # Yield that key and associated value
            yield key, self.__getitem__(key)

    def clear(self):

        """
        Resets the hash map
        :return: None
        """

        self.size = 0

        self.table = [[]] * 100

        self.keys_set = set()

        self.keys_ref = [[]] * 100

    def keys(self):

        """
        Returns the set of unique keys in hash map
        :return: Set of keys
        """

        return self.keys_set

    # supplied methods

    def __repr__(self):

        """
        Formats the hash map
        :return: Formatted hash map
        """

        return '{{{0}}}'.format(
            ','.join('{0}:{1}'.format(k, v) for k, v in self))

    def __bool__(self):

        """
        Tests if the hash map is empty
        :return: True of False based on is_emtpy()
        """

        return not self.is_empty()

    def is_empty(self):

        """
        Tests to see if hash map is emtpy
        :return: True or False whether or not size is zero
        """

        return len(self) == 0

    # Helper functions can go here

    def hash(self, key):

        """
        Hashes a given key and mods it by length of hash map
        :param key: Key to hash
        :return: Hashed key
        """

        return hash(key) % len(self.table)

    def resize(self):

        """
        Resizes the hash map by 2*n - 1
        :return: None
        """

        # Stores the new size of the hash map
        new_size = len(self.table) * 2 - 1

        # Creates new hash map table (empty)
        new_table = [[]] * new_size

        # Creates new key hash table (empty)
        new_ref = [[]] * new_size

        # For key value pair in the current hash map
        for key, value in self:

            # Get new hashed key for new hash map
            i = hash(key) % len(new_table)

            # Put key in new key hash table for index reference
            new_ref[i].append(key)

            # Put value in hash map
            new_table[i].append(value)

        # Overwrite old hash map with new hash map
        self.table = new_table.copy()

        # Overwrite old key hash table with new key hash table
        self.keys_ref = new_ref.copy()


# Required Function
def word_frequency(seq):

    """
    Uses hash map to store word counts from a given sequence
    :param seq: Collection of words to count
    :return: a hash map with words as keys and counts of those words as values
    """

    # Initializes an emtpy hash map from HashMap class
    hash_map = HashMap()

    # For each word (not unique) in sequence
    for word in seq:

        # if that word is already in hash map
        if word in hash_map:

            # Increment value for that word
            hash_map[word] += 1

        # if word not yet in hash map
        else:

            # set count value for word equal to one
            hash_map[word] = 1

    # return filled hash map from sequence, words and words counts
    return hash_map
