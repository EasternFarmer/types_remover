# Types remover(s)

**My type removers I made taken
from [The_Farmer_Was_Replaced](https://github.com/EasternFarmer/The-Farmer-Was-Replaced/tree/main/scripts) repo**

## About

This repo has two protected scripts and one main file you can import from:

- `_types_remover_if.py` - A script I made from the top using if's, a for loop looping over the lines in the input file
  and regex for parameter detection
- `_types_remover_ast.py` - A script I spent a lot longer in documentation and asking for information than writing
- `types_remover.py` - A file created just so you can import the functions from it. <br>

The functions in the files are called `remove_types_ast` and `remove_types_if` and are doing almost the same thing
except implementation.<br>

### IMPORTANT TO NOTE

- The `remove_types_ast` function removes comments
- Both functions turn multi-line data assignation into a one-line statement