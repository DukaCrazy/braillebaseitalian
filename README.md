### - pip install braillebaseitalian

# Italian

## How to use?
```python
from braillebaseitalian import *

bbi = BrailleBaseItalian()
print(bbi.output_braille_txt("Libreria sviluppata per gestire il braille semplice e complesso 2026."))
```
Output: ⠨⠇⠊⠃⠗⠑⠗⠊⠁⠀⠎⠧⠊⠇⠥⠏⠏⠁⠞⠁⠀⠏⠑⠗⠀⠛⠑⠎⠞⠊⠗⠑⠀⠊⠇⠀⠃⠗⠁⠊⠇⠇⠑⠀⠎⠑⠍⠏⠇⠊⠉⠑⠀⠑⠀⠉⠕⠍⠏⠇⠑⠎⠎⠕⠀⠼⠃⠚⠃⠋⠲

# Announcement
- This package is part of an ecosystem called Braille Base. This name does not represent a company or business; it is an independent initiative aimed at providing registered braille tables for all of humanity.

- We constantly need help to register, update, and validate braille tables. There is still no official contact channel, but you can find new information on the blog braillebase.blogspot.com or brailletable.blogspot.com.

## Pre-registered Letters and Characters

```python
from braillebaseitalian import *

bbi = BrailleBaseItalian()
print(bbi.confidence_test("Libreria sviluppata per gestire il braille semplice e complesso 2026."))
```

Output: {0: ['⠨', ['⠨']], 1: ['L', ['⠇']], 2: ['i', ['⠊']], 3: ['b', ['⠃']], 4: ['r', ['⠗']], 5: ['e', ['⠑']], 6: ['r', ['⠗']], 7: ['i', ['⠊']], 8: ['a', ['⠁']], 9: [' ', ['⠀']], 10: ['s', ['⠎']], 11: ['v', ['⠧']], 12: ['i', ['⠊']], 13: ['l', ['⠇']], 14: ['u', ['⠥']], 15: ['p', ['⠏']], 16: ['p', ['⠏']], 17: ['a', ['⠁']], 18: ['t', ['⠞']], 19: ['a', ['⠁']], 20: [' ', ['⠀']], 21: ['p', ['⠏']], 22: ['e', ['⠑']], 23: ['r', ['⠗']], 24: [' ', ['⠀']], 25: ['g', ['⠛']], 26: ['e', ['⠑']], 27: ['s', ['⠎']], 28: ['t', ['⠞']], 29: ['i', ['⠊']], 30: ['r', ['⠗']], 31: ['e', ['⠑']], 32: [' ', ['⠀']], 33: ['i', ['⠊']], 34: ['l', ['⠇']], 35: [' ', ['⠀']], 36: ['b', ['⠃']], 37: ['r', ['⠗']], 38: ['a', ['⠁']], 39: ['i', ['⠊']], 40: ['l', ['⠇']], 41: ['l', ['⠇']], 42: ['e', ['⠑']], 43: [' ', ['⠀']], 44: ['s', ['⠎']], 45: ['e', ['⠑']], 46: ['m', ['⠍']], 47: ['p', ['⠏']], 48: ['l', ['⠇']], 49: ['i', ['⠊']], 50: ['c', ['⠉']], 51: ['e', ['⠑']], 52: [' ', ['⠀']], 53: ['e', ['⠑']], 54: [' ', ['⠀']], 55: ['c', ['⠉']], 56: ['o', ['⠕']], 57: ['m', ['⠍']], 58: ['p', ['⠏']], 59: ['l', ['⠇']], 60: ['e', ['⠑']], 61: ['s', ['⠎']], 62: ['s', ['⠎']], 63: ['o', ['⠕']], 64: [' ', ['⠀']], 65: ['⠼', ['⠼']], 66: ['2', ['⠃']], 67: ['0', ['⠚']], 68: ['2', ['⠃']], 69: ['6', ['⠋']], 70: ['.', ['⠲']]}