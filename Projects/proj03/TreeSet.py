
class TreeSet:

    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """

    def __init__(self, comp):

        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """

        self.comp = comp
        self.node = None
        self.size = 0

    def __len__(self):

        return self.size

    def height(self):

        if self.node is None:

            return -1

        return 1 + max(self.node.left.height(), self.node.right.height())

    def insert(self, item):

        if self.node is None:

            self.node = TreeNode(item)

            self.size += 1

            return True

        elif self.comp(item, self.node.data) == 0:

            return False

        elif self.comp(item, self.node.data) < 0:

            self.node.left.insert(item)

        elif self.comp(item, self.node.data) > 0:

            self.node.right.insert(item)

        # RE-BALANCE

    def remove(self, item):

        if self.node is None:

            return False

        elif self.comp(item, self.node.data) == 0:

            if self.node.left is None and self.node.right is None:

                self.node = None

            elif self.node.left is None:

                self.node = self.node.right.node

            elif self.node.right is None:

                self.node = self.node.left.node

            else:

                temp = self.node.right

                while temp.left is not None:

                    if temp.left.node is None:

                        break

                    temp = temp.left

                self.node.data = temp.data

                self.node.right.delete(temp.data)

            self.size -= 1

            # RE-BALANCE

        elif self.comp(item, self.node.data) < 0:

            self.node.left.remove(item)

        elif self.comp(item, self.node.data) > 0:

            self.node.right.remove(item)

    def __contains__(self, item):

        if self.node is None:

            return False

        elif self.comp(item, self.first()) < 0:

            self.node.left.__contains__(item)

        elif self.comp(item, self.first()) > 0:

            self.node.right.__contains__(item)

        else:

            return True

    def first(self):

        if self.is_empty():

            raise KeyError

        return False

    def last(self):

        if self.is_empty():

            raise KeyError

        return False

    def clear(self):

        pass

    def __iter__(self):

        return iter([])

    # Pre-defined methods

    def is_empty(self):

        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """

        return len(self) == 0

    def __repr__(self):

        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """

        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))

    def is_balanced(self):

        if self.node is None:

            return True

        return abs(self.node.left.height() - self.node.right.height()) <= 1


class TreeNode:

    """
    A TreeNode to be used by the TreeSet
    """

    def __init__(self, data):

        """
        Constructor
        You can add additional data as needed
        :param data:
        """

        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):

        """
        A string representing this node
        :return: A string
        """

        return 'TreeNode({0})'.format(self.data)
