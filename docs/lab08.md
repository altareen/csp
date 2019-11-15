# Lab 8: Polybius Cipher

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Friday, November 15, 2019
+ **Total Points:** 10
+ Implement a `Python` program that decrypts a message using the polybius cipher.

## Background Theory
+ The Polybius Square is an ancient Greek invention, discovered by a scholar named Polybius. It consists of a 5 by 5 grid, in which each square of the grid is filled in by a single letter.
+ In this programming assignment, the grid has been enlarged to 6 by 6, so that it can accommodate the digits 0-9, as well as all the alphabet letters.
+ Each letter in the grid can be represented by the two numbers that indicate its position in the grid. The first number denotes the specific row, and the second number denotes the column. In this manner, the letter `"q"` would be encoded by the digits `24`.

![Regular key](/csp/img/regularkey.png "Regular key")

+ Even though this method of encryption seems feasible, it is not very secure. We need to introduce the notion of a **key**, in order to increase the security of this encryption system. We can achieve this by simply re-ordering the placement of the alphabet and digits, before inserting them into the grid. In this updated version of the grid, the letter `"q"` would be encoded by the digits `45`.

![Scrambled key](/csp/img/scrambledkey.png "Scrambled key")

+ Decrypting a message is quite easy, simply use the pairs of numbers to locate each plaintext letter in the grid. For example, the number sequence `"0520020214"` can be decoded to the word `"hello"`.

## Hints
+ You will notice that you are not given a sequence of numbers to decode. Instead, you are provided with a series of letters. Upon close inspection, you should notice that the provided letters consist of the symbols `"a"`, `"b"`, `"c"`, `"d"`, `"e"` and `"f"`.
+ Each of the letter symbols corresponds to a row or column number in the polybius grid. Specifically, `"a" = 0`, `"b" = 1`, `"c" = 2`, `"d" = 3`, `"e" = 4` and `"f" = 5`. Your first task is to transform these letter symbols into their corresponding number symbols.
+ Recall that, in order to convert from an `ASCII` format to a number, you need to use the following `Python` function:
    + `ord(txt)` This returns the numerical `ASCII` code corresponding to the text character `txt`.
+ Then, you will need to make an adjustment to the numerical output of `ord(txt)`, such that `"a"` corresponds to `0`, `"b"` corresponds to `1`, etc.
+ Make sure that your resulting number sequence is in a string format.
+ Then, you must separate out pairs of digits from this number sequence, and perform a lookup in the two-dimensional key grid. The first number from the pair corresponds to the the row, and the second digit corresponds to the column. A lookup in a two-dimensional grid can be achieved by using two pairs of square brackets as follows:
```python
letter = key[row][column]
```

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Polybius Cipher | 1.8KB | [lab08.zip](/csp/zip/lab08.zip)

**Contents of `lab08.zip`:**
```bash
Lab08PolybiusCipher/
├── polybiuscipher.py
└── testpolybiuscipher.py
```

## Specification
+ Write a `Python` program in the file `polybiuscipher.py` that decrypts a message using the polybius cipher.
+ You will write your solution in a function called `decrypt(message, key)` right below the place where it says: `YOUR CODE HERE`
+ When the function call `decrypt("bcfbfeacbdadafcacafacacedfffffabfa", key)` is executed, the output of the program should be: `buy12cheesepizzas`

## Testing
+ Run the file `testpolybiuscipher.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `polybiuscipher.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

