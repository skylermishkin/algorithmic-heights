def binarySearch(array, target):
    '''
    Searches for `target` within `array` using a binary search.
    Assumes that the given array is sorted.
    '''
    length = len(array)
	if (length < 2):	# in case where target does not exist in array
		return -1
    halfLength = length // 2
    comparator = array[halfLength]

    if target == comparator:
        return halfLength
    elif target < comparator:  # cut left
        return binarySearch(array[:halfLength], target)
    else:	# cut right
        return halfLength + binarySearch(array[halfLength:], target)
