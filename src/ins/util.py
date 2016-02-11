def _swap(array, index1, index2):
    val1 = array[index1]
    val2 = array[index2]
    array[index1] = val2
    array[index2] = val1
    return array
    
def insertion_sort(array):
	'''
	Sorts the given array lowest to highest (modifying the 
	original array). This algorithm is better used on short 
	arrays (quadratic run time), yet uses relatively little 
	additional memory.
	'''
    for i in range(1, len(array)):
        k = i
        while (k > 0 and array[k] < array[k-1]):
            _swap(array, k, k-1)
            k -= 1
    return array
