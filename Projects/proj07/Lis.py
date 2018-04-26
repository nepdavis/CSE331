import math


def verify_subseq(seq, subseq):

    """
    Function to check whether or not a sequence is a subsequence of another
    given sequence
    :param seq: sequence to check with
    :param subseq: subsequence to check for
    :return: bool value on whether or not subseq is subsequence of sequence seq
    """

    # if subsequence empty
    if len(subseq) == 0:

        # then it is a valid subsequence
        return True

    # if subsequence longer than sequence
    if len(subseq) > len(seq):

        # then not a valid subsequence
        return False

    # init a index for subseq
    j = 0

    # for each index in sequence
    for i in range(len(seq)):

        # if seq value equal to current subseq value
        if seq[i] == subseq[j]:

            # increment to next subseq value
            j += 1

        # if all subseq values are checked
        if j == len(subseq):

            # then return true
            return True

    # return false if j never equal to len of subseq
    return False


def verify_increasing(seq):

    """
    Function to check if a sequence is increasing
    :param seq: sequence to check with
    :return: bool value on whether or not seq is increasing
    """

    # for each value in seq
    for i in range(len(seq) - 1):

        # if current seq value greater than next seq value
        if seq[i + 1] <= seq[i]:

            # return false
            return False

    # return true if seq is increasing
    return True


def find_lis(seq):

    """
    Function to find longest increasing subsequence of given sequence seq.
    Runtime of O(nlogn)
    :param seq: sequence to check with
    :return: longest increasing subsequence
    """

    # if sequence is empty
    if len(seq) == 0:

        # return an empty sequence
        return []

    # init length of sequence
    n = len(seq)

    # init a list to store indices of values from sequence
    first = [None] * n

    # init a list to store indices to keep order of increasing values
    second = [None] * (n + 1)

    # init first value of second to 0
    second[0] = 0

    # init length of LIS
    k = 0

    # for range 0 to length of sequence - 1
    for i in range(n):

        # init counter low to 1
        low = 1

        # init counter high equal to length of LIS k
        high = k

        # binary search
        while low <= high:

            # created midpoint index
            mid = int(math.ceil((low + high) / 2))

            if seq[second[mid]] < seq[i]:

                # increment low
                low = mid + 1

            else:

                # decrement high
                high = mid - 1

        # init new length of LIS to low
        new_k = low

        # add new index of value to first
        first[i] = second[new_k - 1]

        # update index to current iteration
        second[new_k] = i

        # if LIS length has changed
        if new_k > k:

            # update LIS length
            k = new_k

    # init empty array equal to length of LIS; will be used to store LIS values
    third = [None] * k

    # get index value for last value in LIS
    j = second[k]

    # for i in range of LIS length - 1 to 0 (backwards)
    for i in range(k - 1, -1, -1):

        # LIS value at index i equal to seq value at index j
        third[i] = seq[j]

        # update j to next value index
        j = first[j]

    # return LIS
    return third
