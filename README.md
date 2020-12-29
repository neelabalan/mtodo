# mtodo :heavy_check_mark:

`mtodo` is an terminal application for parsing all `TODO:` in python source file(s) and uploads them to microsoft todo. It recursively traverses through all directories and gets the `TODO:`

> program.py
```python
1. # TODO: refactor this module
2. def hello():
3.    return 'hello'
```

the above piece of code would show up like `#program.py refactor this module - Line #1` in microsoft todo.
I added `#` before the module name to tag them so it will be easy to find all the todos of `program.py` in single window

### installation

`python setup.py install`

### usage

```bash
mtodo --list myproject --path <path>
# for adding from current directory
mtodo --list myproject --path .
```

### screenshot

![screenshot](https://github.com/neelabalan/mtodo/blob/main/assets/screenshot-todo.png)
