import math


class Digraph:
    def __init__(self, n):
        """
        Constructor
        :param n: Number of vertices
        """
        self.order = n
        self.size = 0
        # You may put any required initialization code here
        pass

    def insert_arc(self, s, d, w):
        pass

    def out_degree(self, v):
        return 0

    def are_connected(self, s, d):
        return False

    def is_path_valid(self, path):
        return False

    def arc_weight(self, s, d):
        return math.inf

    def path_weight(self, path):
        return math.inf

    def does_path_exist(self, s, d):
        return False

    def find_min_weight_path(self, s, d):
        return []

