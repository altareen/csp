# Problem Set 8: Book Identifier

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Monday, November 11, 2019
+ **Total Points:** 10
+ Implement a `Python` program that validates `ISBN-10` numbers.

## Background Theory
+ Any book that you purchase has an **International Standard Book Number**, otherwise known as an `ISBN` or `ISBN-10`. This is a 10-digit number that uniquely identifies books and media products published internationally.
+ It turns out that the last number of an `ISBN-10`'s digits is a **check digit,** otherwise known as a **checksum,** which is a number related mathematically to its preceding digits. 
+ The digits of an `ISBN-10` are supposed to adhere to a formula, and this check digit allows you to verify whether an `ISBN-10`'s other nine digits are valid, without having to resort to other means of verification, for instance, by performing a query on a database of books.

### Calculating the Check Digit
+ The check digit of an `ISBN-10` number can be defined as follows. If $x_1$ represents an `ISBN-10`'s first digit, and $x_{10}$ represents its last digit, then we have the following:

$$
x_{10} = (1 \cdot x_1 + 2 \cdot x_2 + 3 \cdot x_3 + 4 \cdot x_4 + 5 \cdot x_5 + 6 \cdot x_6 + 7 \cdot x_7 + 8 \cdot x_8 + 9 \cdot x_9)\, \mbox{modulus}\, 11
$$

+ In other words, to compute an `ISBN-10`'s tenth digit, multiply its first digit by 1, its second digit by 2, its third digit by 3, its fourth digit by 4, its fifth digit by 5, its sixth digit by 6, its seventh digit by 7, its eighth digit by 8, and its ninth digit by 9. Take the sum of those products and perform a modulus with 11. The result should be the `ISBN-10`'s tenth digit.

### Example Case
+ For example, the `ISBN-10` for the textbook *Absolute Beginner's Guide to C*, is `0-789-75198-4`, the tenth digit of which is `4`. Let's take the sum of the products of the`ISBN-10`'s first nine digits:

$$
(1 \cdot \texttt{0}) + (2 \cdot \texttt{7}) + (3 \cdot \texttt{8}) + (4 \cdot \texttt{9}) + (5 \cdot \texttt{7}) + (6 \cdot \texttt{5}) + (7 \cdot \texttt{1}) + (8 \cdot \texttt{9}) + (9 \cdot \texttt{8}) = 290
$$

+ If we now compute 290 modulus 11, we get a result of 4, which is equal to the tenth digit in the `ISBN-10`. This verifies that the `ISBN-10` number is legitimate.

## Hints
+ Note that the `ISBN-10` is being read in as a string, and it gets converted to an integer by using the `int()` function. The reason for this procedure is to accommodate `ISBN-10`'s with leading zeros.
+ Now that we have an `ISBN-10` in integer form, how can we get at its tenth(i.e. rightmost) digit? Perhaps we can make a clever use of the modulus operator:
```python
tenth = isbncode % 10
```
+ Now, how can we get a that same variable's ninth digit? Perhaps we can get rid of its tenth digit by using integer division:
```python
isbncode = isbncode // 10
```
+ Afterwards, we can access the ninth digit by using the modulus operator:
```python
ninth = isbncode % 10
```
+ Hopefully, you can detect a pattern here. Remember that a certain looping construct such as the `for` loop can be very useful here.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Book Identifier | 1.2KB | [pset08.zip](/csp/zip/pset08.zip)

**Contents of `pset08.zip`:**
```bash
PSet08BookIdentifier/
├── bookidentifier.py
└── testbookidentifier.py
```

## Specification
+ Write a `Python` program in the file `bookidentifier.py` that determines whether an `ISBN-10` number is legitimate or not.
+ You will write your solution in a function called `validatebook(isbncode)` right below the place where it says: `YOUR CODE HERE`
+ If the `ISBN-10` number is valid, then your `validatebook` method should return the string `YES`. Otherwise, if the `ISBN-10` number is not valid, then your `validatebook` method should return the string `NO`.
+ When the function call `validatebook("0789751984")` is executed, the output of the program should be: `YES`

## Testing
+ Run the file `testbookidentifier.py` to execute the `PyUnit` test bench. `PyUnit` indicates a successful test with an `OK` output, and an unsuccessful test with a `FAIL` output.

## Submission
+ Upload the file `bookidentifier.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

