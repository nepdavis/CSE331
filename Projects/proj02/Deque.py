class Deque:

    """
    A double-ended queue

    Implemented using circular array method
    """

    def __init__(self):

        """
        Initializes an empty Deque
        """

        # Init size at 10
        self.data = [None] * 10

        # Init pointers to 0 and logical size at 0
        self.front = 0
        self.size = 0

    def __len__(self):

        """
        Computes the number of elements in the Deque
        :return: The logical size of the Deque
        """

        # return the logical size of the array
        return self.size

    def peek_front(self):

        """
        Looks at, but does not remove, the first element
        :return: The first element
        """

        # if the array is empty
        if self.is_empty():

            # then throw error
            raise IndexError

        # if not empty, return front element
        return self.data[self.front]

    def peek_back(self):

        """
        Looks at, but does not remove, the last element
        :return: The last element
        """

        # if array is empty
        if self.is_empty():

            # then throw error
            raise IndexError

        # if not empty, return back element
        return self.data[(self.front + self.size - 1) % len(self.data)]

    def push_front(self, e):

        """
        Inserts an element at the front of the Deque
        :param e: An element to insert
        """

        # if array at capacity
        if self.size == len(self.data):

            # then resize to double the current physical size
            self.resize(2 * len(self.data))

        # locate physical index before front
        avail = (self.front - 1) % len(self.data)

        # set indexed position to e
        self.data[avail] = e

        # increase size
        self.size += 1

        # change front to new element
        self.front -= 1

    def push_back(self, e):

        """
        Inserts an element at the back of the Deque
        :param e: An element to insert
        """

        # if array at capacity
        if self.size == len(self.data):

            # then resize to double the current physical size
            self.resize(2 * len(self.data))

        # locate physical index after back
        avail = (self.front + self.size) % len(self.data)

        # set indexed position to e
        self.data[avail] = e

        # increase size
        self.size += 1

    def pop_front(self):

        """
        Removes and returns the first element
        :return: The (former) first element

        FINISHED, NEEDS TESTING
        """

        # if array is empty
        if self.is_empty():

            # then throw error
            raise IndexError

        # store value of front
        first = self.data[self.front]

        # remove value of array front
        self.data[self.front] = None

        # increment front index
        self.front = (self.front + 1) % len(self.data)

        # decrease size
        self.size -= 1

        # return former front element
        return first

    def pop_back(self):

        """
        Removes and returns the last element
        :return: The (former) last element
        """

        # if array is empty
        if self.is_empty():

            # then throw error
            raise IndexError

        # store back element
        last = self.data[(self.front + self.size - 1) % len(self.data)]

        # remove value of back element
        self.data[(self.front + self.size - 1) % len(self.data)] = None

        # decrease the size
        self.size -= 1

        # return former back element
        return last

    def clear(self):

        """
        Removes all elements from the Deque
        :return:
        """

        # for element in array
        for i in range(len(self.data)):

            # make element null
            self.data[i] = None

        # reinitialize front and size to 0
        self.front = 0
        self.size = 0

    def retain_if(self, condition):

        """
        Removes items from the Deque so that only items satisfying the given
        condition remain
        :param condition: A boolean function that tests elements
        """

        # init list of indices
        locs = []

        # for each index of physical array
        for i in range(len(self.data)):

            # if condition does not hold and an element exists at that loc
            if self.data[i] is not None and (not condition(self.data[i])):

                # then append that index to the list of indices
                locs.append(i)

                # decrease size
                self.size -= 1

        # remove all elements at the indices where the condition was not met
        self.data = [self.data[i] for i in range(len(self.data)) if i not in
                     locs]

    def __iter__(self):

        """
        Iterates over this Deque from front to back
        :return: An iterator
        """

        # for element in array
        for i in self.data:

            # yield that element for iter
            yield i

    # provided functions

    def is_empty(self):

        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise
        """

        # return truth value for array size 0 or not
        return len(self) == 0

    def __repr__(self):

        """
        A string representation of this Deque
        :return: A string
        """

        # return string format for array printing
        return 'Deque([{0}])'.format(','.join(str(item) for item in self))

    # helper methods

    def resize(self, new_size):

        """
        This functions re-sizes the deque to an inputted new size
        :param new_size: the desired new size of the deque
        :return: None

        FINISHED, NEEDS TESTING
        """

        # store deque data into a variable
        old_data = self.data

        # re-init the deque to a new size
        self.data = [None] * new_size

        # store former front index
        old_index = self.front

        # for index in logical size
        for i in range(self.size):

            # push old data to new array
            self.data[i] = old_data[old_index]

            # increment old index
            old_index = (1 + old_index) % len(old_data)

        # re-init front pointer
        self.front = 0
