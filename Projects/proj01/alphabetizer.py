def merge(a, b, ordering, comparisons):

    """
    Merges two sorted lists by sorting them iteratively and storing them in
    a new list c
    :param a: a sorted list
    :param b: a second sorted list
    :param ordering: the type of ordering (either first or last name)
    :param comparisons: current total number of comparisons made
    :return: the merged list c and the updated total number of comparisons
    """

    # set indices to 0
    i, j, k = 0, 0, 0

    # initialize list c of None's for merging
    c = [None for _ in range(len(a) + len(b))]

    # as long as a and b indices are not out of range
    while i < len(a) and j < len(b):

        # if a comes before b based on ordering
        if ordering(a[i], b[j]):

            # entry of c is entry of a
            c[k] = a[i]

            # update comparisons
            comparisons += 1

            # move on to next entry of c and a
            k += 1
            i += 1

        # if b comes before a based on ordering
        else:

            # entry of c is entry of b
            c[k] = b[j]

            # update comparisons
            comparisons += 1

            # move on to next entry of c and b
            k += 1
            j += 1

    # remove the None's from the end of the list that were not replaced
    c = c[:i + j]

    # if all of a was added to c
    if i == len(a):

        # add the rest of b to c
        c += b[j:]

    # if all of b was added to c
    else:

        # add the rest of a to c
        c += a[i:]

    # return the merged list c and the new total number of comparisons
    return c, comparisons


def merge_sort(roster, ordering, comparisons):

    if len(roster) == 1:

        return roster, comparisons

    else:

        a, comparisons = merge_sort(roster[:len(roster) // 2], ordering,
                                    comparisons)
        b, comparisons = merge_sort(roster[len(roster) // 2:], ordering,
                                    comparisons)

        c, comparisons = merge(a, b, ordering, comparisons)

        return c, comparisons


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

    return merge_sort(roster, ordering, comparisons)
