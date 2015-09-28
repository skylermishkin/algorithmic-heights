# algorithmic-heights

A collaborative attempt at the problem tree found [here](http://rosalind.info/problems/tree-view/?location=algorithmic-heights).


## Repository Structure

- README.md
- src/
    * problem_id/
        - tests
        - main.py
        - other_files.py


## Contributing

Never push to master.  

When you want to tackle a new problem, make a new branch and work on it there.  For example,

```
# make (and checkout) a new branch for problem id "ddeg"
git checkout -b ddeg
```

Then, when you have solved the problem, you can make a pull request for that branch to be merged into master.  This way, all the contributors can have a chance to look over your contribution before agreeing to include it in the master branch of the repository.

Also, test everything (see [here](https://docs.python.org/3.5/library/unittest.html) for tips).
