import math


def verify_subseq(seq, subseq):

    if len(subseq) == 0:

        return True

    if len(subseq) > len(seq):

        return False

    j = 0

    for i in range(len(seq)):

        if seq[i] == subseq[j]:

            j += 1

        if j == len(subseq):

            return True

    return False


def verify_increasing(seq):

    for i in range(len(seq) - 1):

        if seq[i + 1] <= seq[i]:

            return False

    return True


def find_lis(seq):

    n = len(seq)

    first = [None] * n
    second = [None] * (n + 1)

    second[0] = 0

    k = 0

    for i in range(n):

        low = 1
        high = k

        while low <= high:

            mid = int(math.ceil((low + high) / 2))

            if seq[second[mid]] < seq[i]:

                low = mid + 1

            else:

                high = mid - 1

        new_k = low

        first[i] = second[new_k - 1]

        second[new_k] = i

        if new_k > k:

            k = new_k

    third = [None] * k

    j = second[k]

    for i in range(k - 1, -1, -1):

        third[i] = seq[j]

        j = first[j]

    return third
