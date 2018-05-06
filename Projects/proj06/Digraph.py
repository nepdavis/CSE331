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

        self.g = {i: {} for i in range(n)}

    def insert_arc(self, s, d, w):

        """
        Creates arc between two nodes
        :param s: source node
        :param d: target node
        :param w: arc weight
        :return: None
        """

        if s > self.order - 1 or d > self.order - 1:

            raise IndexError

        else:

            if d not in self.g[s]:

                self.size += 1

            self.g[s][d] = w

    def out_degree(self, v):

        """
        Out degree of given node
        :param v: node
        :return: out degree of inputted node
        """

        if v in self.g:

            return len(self.g[v])

        else:

            raise IndexError

    def are_connected(self, s, d):

        """
        Checks to see if two nodes are connected
        :param s: source node
        :param d: target node
        :return: None
        """

        if s <= self.order - 1 and d <= self.order - 1:

            if d in self.g[s]:

                return True

            return False

        else:

            raise IndexError

    def is_path_valid(self, path):

        """
        Checks to see if a given path is valid
        :param path: Inputted path of nodes
        :return: Bool value whether path is valid
        """

        status = True

        for i in range(len(path) - 1):

            status = self.are_connected(path[i], path[i + 1])

            if not status:

                return False

        return status

    def arc_weight(self, s, d):

        """
        Gives the weight of an arc
        :param s: source node
        :param d: target node
        :return: weight of arc between source and target
        """

        if self.are_connected(s, d):

            return self.g[s][d]

        return math.inf

    def path_weight(self, path):

        """
        Gives total weight of inputted path
        :param path: Path of nodes
        :return: Total weight of path
        """

        weight = 0

        if self.is_path_valid(path):

            if len(path) == 1:

                return 0

            for i in range(len(path) - 1):

                weight += self.g[path[i]][path[i + 1]]

            return weight

        return math.inf

    def does_path_exist(self, s, d):

        """
        Checks to see if a path exists between two nodes, uses depth-first
        :param s: source node
        :param d: target node
        :return: Bool whether path exists between two nodes
        """

        if s > self.order - 1 or d > self.order - 1:

            raise IndexError

        visited = {v: False for v in range(self.order)}

        self.dfs(s, visited)

        return visited[d]

    def find_min_weight_path(self, s, d):

        """
        Finds minimum weight path between two nodes using Dijkstra's
        :param s: source node
        :param d: target node
        :return: min weight path between two nodes, ValueError if path
        doesn't exist
        """

        if s > self.order - 1 or d > self.order - 1:

            raise IndexError

        not_visited = set([i for i in range(self.order)])

        dist = {u: math.inf for u in not_visited}

        prev = {u: None for u in not_visited}

        dist[s] = 0

        while len(not_visited) != 0:

            temp_nodes = {k: v for k, v in dist.items() if k in not_visited}

            u = min(temp_nodes, key = temp_nodes.get)

            not_visited.remove(u)

            if u == d:

                break

            for v in self.g[u]:

                if dist[u] + self.arc_weight(u, v) < dist[v]:

                    dist[v] = dist[u] + self.arc_weight(u, v)

                    prev[v] = u

        if d in not_visited:

            raise ValueError

        path = []

        u = d + 0

        while prev[u] is not None:

            path = [u] + path

            u = prev[u]

        path = [u] + path

        return path

    def dfs(self, node, visited):

        """
        Depth first search to see if path exists between two nodes
        :param node: source node
        :param visited: target node
        :return: None -- fills dictionary with whether or not nodes were
        visited from source node
        """

        visited[node] = True

        if node in self.g:

            for v in self.g[node]:

                if not visited[v]:

                    self.dfs(v, visited)
