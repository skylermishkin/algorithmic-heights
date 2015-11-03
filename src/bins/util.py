def binarySearch(array, target):
    '''
    Searches for `target` within `array` using a binary search.
    Assumes that the given array is sorted.
    '''
    length = len(array)
    halfLength = length // 2
    comparator = array[halfLength]

    if target == comparator:
        return halfLength
    elif target < comparator:
        return binarySearch(array[:halfLength], target)
    else:
        return halfLength + binarySearch(array)
