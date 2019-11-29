# Lab 9: Substitution Cipher

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Friday, November 22, 2019
+ **Total Points:** 10
+ Implement a `Python` program that encrypts a message using the substitution cipher.

## Background Theory
+ In a substitution cipher, we **encrypt** a message by replacing every letter in a plaintext message with some other letter.
+ In order to perform this encryption, we make use of a **key**. In the case of the substitution cipher, the key is a mapping of each of the letters of the alphabet to the letter that it should correspond to, when we encrypt it.
+ To **decrypt** the message, the receiver of the message would need to know the key, so that they could reverse the process.
+ A **key**, for example, might be the string `jtrekyavogdxpsncuizlfbmwhq`. This 26-character key means that `a`(the first letter of the alphabet) should be converted into `j`(the first letter of the key). Similarly, the letter `b`(the second letter of the alphabet) should be converted into `t`(the second letter of the key) and so on.
+ Therefore, a message like `hello` would be encrypted as `vkxxn`, replacing each of the letters according to the mapping as determined by the key.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Substitution Cipher | 1.7KB | [lab09.zip](/csp/zip/lab09.zip)

**Contents of `lab09.zip`:**
```bash
Lab09SubstitutionCipher/
├── substitutioncipher.py
└── testsubstitutioncipher.py
```

## Specification
+ Write a `Python` program in the file `substitutioncipher.py` that encrypts a message using the substitution cipher.
+ You will write your solution in a function called `encrypt(message, key)` right below the place where it says: `YOUR CODE HERE`
+ When the function call `encrypt("hello", "jtrekyavogdxpsncuizlfbmwhq")` is executed, the output of the program should be: `vkxxn`

## Testing
+ Run the file `testsubstitutioncipher.py` to execute the `PyUnit` test bench. `PyUnit` indicates a successful test with an `OK` output, and an unsuccessful test with a `FAIL` output.

## Submission
+ Upload the file `substitutioncipher.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

