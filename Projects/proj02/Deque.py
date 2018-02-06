class Deque:

    """
    A double-ended queue
    """

    def __init__(self):

        """
        Initializes an empty Deque

        NOT FINISHED
        """

        self.front = None
        self.back = None

    def __len__(self):

        """
        Computes the number of elements in the Deque
        :return: The logical size of the Deque

        FINISHED, NEEDS TESTING
        """

        return len(self)

    def peek_front(self):

        """
        Looks at, but does not remove, the first element
        :return: The first element

        FINISHED, NEEDS TESTING
        """

        if self.is_empty():

            raise IndexError

        return self.front

    def peek_back(self):

        """
        Looks at, but does not remove, the last element
        :return: The last element

        FINISHED, NEEDS TESTING
        """

        if self.is_empty():

            raise IndexError

        return self.back

    def push_front(self, e):

        """
        Inserts an element at the front of the Deque
        :param e: An element to insert

        NOT FINISHED
        """
        pass

    def push_back(self, e):

        """
        Inserts an element at the back of the Deque
        :param e: An element to insert

        NOT FINISHED
        """
        pass

    def pop_front(self):

        """
        Removes and returns the first element
        :return: The (former) first element

        NOT FINISHED
        """
        raise IndexError

    def pop_back(self):

        """
        Removes and returns the last element
        :return: The (former) last element

        NOT FINISHED
        """
        raise IndexError

    def clear(self):

        """
        Removes all elements from the Deque
        :return:

        NOT FINISHED
        """
        pass

    def retain_if(self, condition):

        """
        Removes items from the Deque so that only items satisfying the given
        condition remain
        :param condition: A boolean function that tests elements

        NOT FINISHED
        """
        pass

    def __iter__(self):

        """
        Iterates over this Deque from front to back
        :return: An iterator

        NOT FINISHED
        """
        pass

    # provided functions

    def is_empty(self):

        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise

        FINISHED
        """

        return len(self) == 0

    def __repr__(self):

        """
        A string representation of this Deque
        :return: A string

        FINISHED
        """

        return 'Deque([{0}])'.format(','.join(str(item) for item in self))

