## GraduateHW
identifier name linter produces two output files 
- contain list of names and locations of all identifiers in the program.
- name and location of all identifiers that violate the Simon Butler naming convention.

## Setup:
create a Languages folder and clone the following github repositories inside that:
```sh
git clone https://github.com/tree-sitter/tree-sitter-go
git clone https://github.com/tree-sitter/tree-sitter-javascript
git clone https://github.com/tree-sitter/tree-sitter-python
```

The code is built with following libraries:

- [tree-sitter](https://tree-sitter.github.io/tree-sitter/)
- [pyenchant](https://pypi.org/project/pyenchant/)
- [pygithub](https://scikit-learn.org/stable/)

To run the program run the following command:

```bash
python tree-sitter-linter.py -i github-URL -e extension -l language -m output1-filepath -n output2-filepath
```
for exmaple:
python tree-sitter-linter.py -i https://github.com/adaptives/python-examples -e .py -l python -m output/output1.csv -n output/output2.csv

In the repository output folder is given with a sample output for reference, please use extensions like ".py, .js, .go or .ruby" and languages like "python, javascript, go and ruby" please make sure the directories exist for output1-filepath and output2-filepath.

## After running the program:
- output1-filepath consists of list of names and locations of all identifiers in the program.
- output2-filepath name and location of all identifiers that violate the Simon Butler naming convention.
