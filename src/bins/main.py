# local imports
from .util import binarySearch


def main(fileContents):
    array, targets = fileContents.split('\n')[2:]
    result = [binarySearch(array, target) for index in targets]
    return str(result)
