
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

        """
        Returns the length of the tree
        :return: tree size
        """

        return self.size

    def height(self):

        """
        Outputs the height of the tree
        :return: the height of the tree
        """

        # if tree is empty
        if self.node is None:

            return -1

        # else
        return max(self.node.node_height(), self.node.node_height())

    def insert(self, item):

        """
        Inserts a value into tree set
        :param item: value to insert
        :return: a bool value of whether or not insert was successful
        """

        if self.node is None:

            self.node = TreeNode(item, None, False, True)

            self.size += 1

            return True

        elif self.node.__contains__(item, self.comp):

            return False

        else:

            self.inserting_node(self.node, item)

            return True

    def inserting_node(self, node, item):

        """
        recursive function to use to insert item after node
        :param node: current node to evaluate
        :param item: value to insert
        :return: None
        """

        if self.comp(item, node.data) < 0:

            if node.left is None:

                node.left = TreeNode(item, node, is_left = True)

                self.size += 1

            else:

                self.inserting_node(node.left, item)

        else:

            if node.right is None:

                node.right = TreeNode(item, node, is_left = False)

                self.size += 1

            else:

                self.inserting_node(node.right, item)

    def remove(self, item):

        """
        method to remove value from tree set
        :param item: value to remove
        :return: bool value whether or not removal was successful
        """

        if self.node is None:

            return False

        elif not self.node.__contains__(item, self.comp):

            return False

        elif self.comp(item, self.node.data) == 0 and self.size == 1:

            self.clear()

            return True

        else:

            self.deleting(self.node, item)

            self.size -= 1

            return True

    def deleting(self, node, item):

        """
        recursive function to remove value from tree set
        :param node: current node to evaluate
        :param item: value to remove
        :return: None
        """

        if self.comp(item, node.data) == 0:

            if node.is_root:

                temp = node.right

                while temp.left is not None:

                    if temp.left is None:
                        break

                    temp = temp.left

                node.data = temp.data

                self.deleting(node.right, temp.data)

            elif node.left is None and node.right is None:

                if node.is_left:

                    node.parent.left = None

                else:

                    node.parent.right = None

            elif node.left is None:

                node.right.parent = node.parent

                if node.is_left:

                    node.parent.left = node.right
                    node.right.is_left = True

                else:

                    node.parent.right = node.right
                    node.right.is_left = False

            elif node.right is None:

                node.left.parent = node.parent

                if node.is_left:

                    node.parent.left = node.left
                    node.left.is_left = True

                else:

                    node.parent.right = node.left
                    node.left.is_left = False

            else:

                temp = node.right

                while temp.left is not None:

                    if temp.left is None:

                        break

                    temp = temp.left

                node.data = temp.data

                self.deleting(node.right, temp.data)

        elif self.comp(item, node.data) < 0:

            self.deleting(node.left, item)

        else:

            self.deleting(node.right, item)

    def __contains__(self, item):

        """
        checks to see if value is in tree set
        :param item: value to check for
        :return: bool for whether or not value in tree set
        """

        if self.node is None:

            return False

        elif self.comp(item, self.node.data) != 0:

            return self.node.__contains__(item, self.comp)

        else:

            return True

    def first(self):

        """
        :return: first value in tree set (in order traversal)
        """

        if self.is_empty():

            raise KeyError

        for i in self:

            return i

    def last(self):

        """
        :return: last value in tree set (in order traversal)
        """

        if self.is_empty():

            raise KeyError

        temp = None

        for i in self:

            temp = i

        return temp

    def clear(self):

        """
        erases current tree set
        :return: None
        """

        self.node = None

        self.size = 0

    def __iter__(self):

        """
        iterates through node iterator
        :return: node iterator
        """

        if self.node is not None:

            return iter(self.node)

    def is_empty(self):

        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """

        return len(self) == 0

    def __repr__(self):

        """
        Creates a string representation of this set using
        an in-order traversal.
        :return: A string representing this set
        """

        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))


class TreeNode:

    """
    A TreeNode to be used by the TreeSet
    """

    def __init__(self, data, parent = None, is_left = False, is_root = False):

        """
        constructor
        :param data: value for node
        :param parent: node parent
        :param is_left: bool for left child
        :param is_root: bool for root node
        """

        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.is_left = is_left
        self.is_root = is_root

    def __repr__(self):

        """
        A string representing this node
        :return: A string
        """

        return 'TreeNode({0})'.format(self.data)

    def __iter__(self):

        """
        iterates through nodes
        :return: yields node data
        """

        if self.left is not None:

            for i in self.left:

                yield i

        yield self.data

        if self.right is not None:

            for j in self.right:

                yield j

    def __contains__(self, item, comp):

        """
        checks to see if value in nodes
        :param item: value to check for
        :param comp: function for evaluation
        :return: bool value for whether not is in tree set or not
        """

        if comp(item, self.data) == 0:

            return True

        elif comp(item, self.data) < 0:

            if self.left is not None:

                return self.left.__contains__(item, comp)

            else:

                return False

        else:

            if self.right is not None:

                return self.right.__contains__(item, comp)

            else:

                return False

    def node_height(self):

        """
        :return: height of node
        """

        if self.left is not None:

            height_left = self.left.node_height()

        else:

            height_left = -1

        if self.right is not None:

            height_right = self.right.node_height()

        else:

            height_right = -1

        return 1 + max(height_left, height_right)
