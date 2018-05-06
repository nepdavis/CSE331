
class Heap:

    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self, comp):

        """
        Constructor
        :param comp: A comparison function determining the priority of the
        included elements
        """

        self.comp = comp
        # Added Members

        self.h = []
        self.size = 0

    def __len__(self):

        """
        Length of heap
        :return: length of heap
        """

        return self.size

    def peek(self):

        """
        Looks at minimum/root
        :return: value of minimum
        """

        if self.is_empty():

            raise IndexError

        return self.h[0]

    def insert(self, item):

        """
        Inserts value into heap
        :param item: item to insert
        :return: none
        """

        self.size += 1

        self.h.append(item)

        i = len(self) - 1

        while i > 0 and self.comp(item, self.h[parent(i)]):

            self.h[i] = self.h[parent(i)]

            i = parent(i)

        self.h[i] = item

    def extract(self):

        """
        Returns and removes root, re-balances heap
        :return: root
        """

        if self.is_empty():

            raise IndexError

        minimum = self.h[0]

        self.h[0] = self.h[-1]

        self.h.pop()

        self.size -= 1

        self.heapify(0)

        return minimum

    def extend(self, seq):

        """
        Extends heap with a collection of values in O(n + m) time
        :param seq: Collection of values to extend heap
        :return: None
        """

        self.h.extend(seq)

        self.size += len(seq)

        new_length = len(self) // 2

        for i in reversed(range(new_length)):

            self.heapify(i)

    def clear(self):

        """
        Resets the heap to be empty and makes size 0
        :return: None
        """

        self.h = []
        self.size = 0

    def __iter__(self):

        """
        Iterates through the heap
        :return: iterator generator
        """

        for i in self.h:

            yield i

    # Supplied methods

    def __bool__(self):

        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """

        return not self.is_empty()

    def is_empty(self):

        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """

        return len(self) == 0

    def __repr__(self):

        """
        A string representation of this heap
        :return:
        """

        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    # Added methods

    def heapify(self, key):

        """
        Heapifies current heap starting at key in place
        :param key: index to start at
        :return: None
        """

        left = 2 * key + 1
        right = 2 * key + 2

        if left < len(self) and self.comp(self.h[left], self.h[key]):

            small = left

        else:

            small = key

        if right < len(self) and self.comp(self.h[right], self.h[small]):

            small = right

        if small != key:

            self.h[key], self.h[small] = self.h[small], self.h[key]

            self.heapify(small)


# Required Non-heap member function


def find_median(seq):

    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.

    Creates min_heap and max_heap. Adds first value to max_heap. Smaller values
    go into max_heap, bigger ones into min_heap. Re-balances at each iteration.
    At the end of the iteration, it returns the median based on min_heap and
    max_heap lengths.

    :param seq: an iterable sequence
    :return: the median element
    """

    if not seq:

        raise IndexError

    # Init min and max heaps with correct functions
    min_heap = Heap(lambda a, b: a <= b)
    max_heap = Heap(lambda a, b: a >= b)

    # for value in sequence of values
    for i in seq:

        # if both heaps are empty
        if min_heap.is_empty() and max_heap.is_empty():

            # insert first value into max heap
            max_heap.insert(i)

        # if not empty
        else:

            # if current value less than max heap root
            if i < max_heap.peek():

                # insert value into max heap
                max_heap.insert(i)

            # if current values greater than or equal to max heap root
            else:

                # insert value into min heap
                min_heap.insert(i)

        # if max heap longer than min heap by at least 2
        if len(max_heap) > len(min_heap) + 1:

            # pop root of max heap
            root = max_heap.extract()

            # add old max heap root to min heap
            min_heap.insert(root)

        # if min heap longer than max heap by at least 2
        if len(min_heap) > len(max_heap) + 1:

            # pop root of min heap
            root = min_heap.extract()

            # add old min heap root to max heap
            max_heap.insert(root)

    # if both heaps same size
    if len(max_heap) == len(min_heap):

        # return a root as median
        return min_heap.peek()

    # if max heap longer
    elif len(max_heap) > len(min_heap):

        # return max heap root as median
        return max_heap.peek()

    # if min heap longer
    else:

        # return min heap root as median
        return min_heap.peek()


def parent(index):

    """
    Retrives parent index of input index
    :param index: index to get parent index for
    :return: parent index
    """

    return (index - 1) // 2
