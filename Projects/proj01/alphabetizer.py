def order_first_name(a, b):

    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """

    if a.first() < b.first():

        return True

    return False


def order_last_name(a, b):

    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """

    if a.last() < b.last():

        return True

    return False


def is_alphabetized(roster, ordering):

    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """
    return False


def alphabetize(roster, ordering):

    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a sorted version of roster
    :return: the number of comparisons made
    """

    comparisons = 0

    top = roster[:len(roster)//2]

    bottom = roster[len(roster)//2:]

    all = [None for _ in range(len(roster))]

    i, j = 0, 0

    k = len(roster)

    while i < len(top) and j < len(bottom):

        if top[i] < bottom[j]:

            all[k] = top[i]

            comparisons += 1
            k += 1
            i += 1

        else:

            all[k] = bottom[j]

            comparisons += 1
            k += 1
            j += 1

    return list(roster), 0
