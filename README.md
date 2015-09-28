# algorithmic-heights

A collaborative attempt at the problem tree found [here](http://rosalind.info/problems/tree-view/?location=algorithmic-heights).


## Repository Structure

- README.md
- scripts/
    - run (runs a given problem solution on a given input file)
    - test (runs the entire test suite)
- src/
    - problem_id/
        - tests.py
        - util.py
        - main.py
            - Must export a function named `main` with signature

            ```
            (input_file_contents, *args) -> output_file_contents
            ```

            (for the cli to find).


## Running the Test Suite

To run the test suite from the project root, use

```shell
./scripts/test
```


## Trying out a Problem Solution

You can run problem solutions on sample data from a file using `scripts/run`.  For example, from the project root, running

```shell
./scripts/run fibo ~/Downloads/rosalind_fibo.txt
```

will run the solution for problem "fibo" with the input data from `~/Downloads/rosalind_fibo.txt`.


## Contributing

Never push to master.  

When you want to tackle a new problem, make a new branch and work on it there.  For example,

```
# make (and checkout) a new branch for problem id "ddeg"
git checkout -b ddeg
```

Then, when you have solved the problem, you can make a pull request for that branch to be merged into master.  This way, all the contributors can have a chance to look over your contribution before agreeing to include it in the master branch of the repository.

Also, test everything (see [here](https://docs.python.org/3.5/library/unittest.html) for tips).
