def merge(a, b, ordering, comparisons):

    i, j, k = 0, 0, 0

    c = [None for _ in range(len(a) + len(b))]

    while i < len(a) and j < len(b):

        if ordering(a[i], b[j]):

            c[k] = a[i]

            comparisons += 1
            k += 1
            i += 1

        else:

            c[k] = b[j]

            comparisons += 1
            k += 1
            j += 1

    c = c[:i + j]

    if i == len(a):

        c += b[j:]

    else:

        c += a[i:]

    return c


def merge_sort(roster, ordering, comparisons):

    if len(roster) == 1:

        return roster

    else:

        a = merge_sort(roster[:len(roster) // 2], ordering, comparisons)
        b = merge_sort(roster[len(roster) // 2:], ordering, comparisons)

        c = merge(a, b, ordering, comparisons)

        return c


def order_first_name(a, b):

    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """

    if a.first == b.first:

        if a.last < b.last:

            return True

        return False

    elif a.first < b.first:

        return True

    return False


def order_last_name(a, b):

    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """

    if a.last == b.last:

        if a.first < b.first:

            return True

        return False

    elif a.last < b.last:

        return True

    return False


def is_alphabetized(roster, ordering):

    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """

    i = 0

    while i < len(roster) - 1:

        if not ordering(roster[i], roster[i + 1]):

            return False

        i += 1

    return True


def alphabetize(roster, ordering):

    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a sorted version of roster
    :return: the number of comparisons made
    """

    comparisons = 0

    return merge_sort(roster, ordering, comparisons), comparisons
