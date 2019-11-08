# Lab 7: Caesar Cipher

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Friday, November 8, 2019
+ **Total Points:** 10
+ Implement a `Python` program that encrypts a message using the caesar cipher.

## Background Theory
+ The main idea behind the Caesar Cipher is to shift each letter in a secret message by a fixed number of positions. If this shifting behaviour goes further than the end of the alphabet, then it **wraps around** to the beginning, and continues from there.
+ The security of this crypto-system relies on having only the sender and the recipient know the secret **key**, which is the number of places by which the letters have been shifted.

![Encryption shift](/csp/img/encrypt.png "Encryption shift")

## Hints
+ `Python` uses a numerical `ASCII` value to represent each text character in the alphabet. For example, the `ASCII` value of the letter `"a"` is `97`, and the `ASCII` value of the letter `"z"` is `122`.
+ In order to convert between the two formats, you need to use the following `Python` functions:
    + `ord(txt)` This returns the numerical `ASCII` code corresponding to the text character `txt`.
    + `chr(num)` This returns the text character corresponding to the numerical `ASCII` code `num`.
+ You will need to make an adjustment to the numerical output of `ord(txt)`, such that `"a"` corresponds to `0`, `"b"` corresponds to `1`, etc.
+ Unencrypted text is generally called **plaintext**, and encrypted text is generally known as **ciphertext**. The quantity by which the letters have been shifted is called a **key**.
+ In general, the Caesar Cipher encrypts messages by **rotating** each letter by `key` positions. More formally, `p` is the `ASCII` value of a letter in the plaintext, and `key` is the amount by which each letter is shifted, then the `ASCII` value of the corresponding letter in the ciphertext `c`, is computed by the following equation:

$$
c = (p + \mbox{key})\, \mbox{mod}\, 26
$$

+ You may assume that all of the characters in the plaintext messages are in **lowercase**.
+ There will be no punctuation present in any of the plaintext messages,with the exception of the space character. You should design your program so that any spaces in the plaintext message are transferred into the encrypted ciphertext.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Caesar Cipher | 1.5KB | [lab07.zip](/csp/zip/lab07.zip)

**Contents of `lab07.zip`:**
```bash
Lab07CaesarCipher/
├── caesarcipher.py
└── testcaesarcipher.py
```

## Specification
+ Write a `Python` program in the file `caesarcipher.py` that encrypts a message using the caesar cipher.
+ You will write your solution in a function called `encrypt(message, key)` right below the place where it says: `YOUR CODE HERE`
+ When the function call `encrypt("hello", 1)` is executed, the output of the program should be: `ifmmp`

## Testing
+ Run the file `testcaesarcipher.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `caesarcipher.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

