# local imports
from .util import insertion_sort


def main(fileContents):
    array = fileContents.split('\n')[1:]
    result = insertion_sort(array)
    return str(result)
