# local imports
from .util import fibo


# export main function for cli
def main(s):
    # turn input into integer, then pass to `fibo`
    return fibo(int(s))
