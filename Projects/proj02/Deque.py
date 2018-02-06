class Deque:

    """
    A double-ended queue
    """

    def __init__(self):

        """
        Initializes an empty Deque

        FINISHED, NEEDS TESTING
        """

        self.data = [None] * 10
        self.front = 0
        self.size = 0

    def __len__(self):

        """
        Computes the number of elements in the Deque
        :return: The logical size of the Deque

        FINISHED, NEEDS TESTING
        """

        return self.size

    def peek_front(self):

        """
        Looks at, but does not remove, the first element
        :return: The first element

        FINISHED, NEEDS TESTING
        """

        if self.is_empty():

            raise IndexError

        return self.data[self.front]

    def peek_back(self):

        """
        Looks at, but does not remove, the last element
        :return: The last element

        FINISHED, NEEDS TESTING
        """

        if self.is_empty():

            raise IndexError

        return self.data[(self.front + self.size - 1) % len(self.data)]

    def push_front(self, e):

        """
        Inserts an element at the front of the Deque
        :param e: An element to insert

        FINISHED, NEEDS TESTING
        """

        if self.size == len(self.data):

            self.resize(2 * len(self.data))

        avail = (self.front - 1) % len(self.data)

        self.data[avail] = e

        self.size += 1

        self.front -= 1

    def push_back(self, e):

        """
        Inserts an element at the back of the Deque
        :param e: An element to insert

        FINISHED, NEEDS TESTING
        """

        if self.size == len(self.data):

            self.resize(2 * len(self.data))

        avail = (self.front + self.size) % len(self.data)

        self.data[avail] = e

        self.size += 1

    def pop_front(self):

        """
        Removes and returns the first element
        :return: The (former) first element

        FINISHED, NEEDS TESTING
        """

        if self.is_empty():

            raise IndexError

        first = self.data[self.front]

        self.data[self.front] = None

        self.front = (self.front + 1) % len(self.data)

        self.size -= 1

        return first

    def pop_back(self):

        """
        Removes and returns the last element
        :return: The (former) last element

        FINISHED, NEEDS TESTING
        """

        if self.is_empty():

            raise IndexError

        last = self.data[(self.front + self.size - 1) % len(self.data)]

        self.data[(self.front + self.size - 1) % len(self.data)] = None

        self.size -= 1

        return last

    def clear(self):

        """
        Removes all elements from the Deque
        :return:

        FINISHED, NEEDS TESTING (MAY NEED TO BE CHANGED TO O(N) TIME)
        """

        for i in range(len(self.data)):

            self.data[i] = None

        self.front = 0
        self.size = 0

    def retain_if(self, condition):

        """
        Removes items from the Deque so that only items satisfying the given
        condition remain
        :param condition: A boolean function that tests elements

        FINISHED, NEEDS TESTING
        """

        locs = []

        for i in range(len(self.data)):

            if not condition(self.data[i]) and self.data[i] is not None:

                locs.append(i)

                self.size -= 1

        self.data = [self.data[i] for i in range(len(self.data)) if i not in
                     locs]

    def __iter__(self):

        """
        Iterates over this Deque from front to back
        :return: An iterator

        FINISHED, NEEDS TESTING
        """

        for i in self.data:

            yield i

    # provided functions

    def is_empty(self):

        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise

        FINISHED, NEEDS TESTING
        """

        return len(self) == 0

    def __repr__(self):

        """
        A string representation of this Deque
        :return: A string

        FINISHED, NEEDS TESTING
        """

        return 'Deque([{0}])'.format(','.join(str(item) for item in self))

    # helper methods

    def resize(self, new_size):

        """

        :param new_size:
        :return:

        FINISHED, NEEDS TESTING
        """

        old_data = self.data

        self.data = [None] * new_size

        old_index = self.front

        for i in range(self.size):

            self.data[i] = old_data[old_index]

            old_index = (1 + old_index) % len(old_data)

        self.front = 0
