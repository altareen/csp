# Problem Set 10: Credit Card

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Monday, November 25, 2019
+ **Total Points:** 10
+ Implement a `Python` program that determines whether a provided credit card number is valid, according to Luhn's algorithm.

## Background Theory
+ Every credit card has a number, both printed on its face, and embedded in the magnetic stripe on its back. That number is also stored in a database somewhere, so that when your card is used to buy something, the creditor knows whom to bill.
+ There are many people with credit cards in this world, so those numbers are pretty long:
    + American Express: 15-digit numbers
    + MasterCard: 16-digit numbers
    + Visa: 13- and 16-digit numbers
+ Credit cards companies don't just assign a random series of digits to compose
    their credit card numbers. Rather, there is actually some structure to them:
    + American Express numbers must start with 34 or 37.
    + MasterCard numbers must start with 51, 52, 53, 54 or 55.
    + Visa numbers must start with 4.
+ Credit card numbers also have a **checksum** built into them, which is a mathematical relationship between at least one number, and the others. This checksum enables computers to detect errors and fraudulent credit card numbers, without having to query a database, which can be slow.
+ Credit card companies use an algorithm developed by Hans Peter Luhn, a researcher from IBM.
+ According to **Luhn's algorithm**, you can determine if a credit card is valid by executing the following steps:
    1. Multiply every other digit by 2, starting with the number's **second-to-last digit**, and then add those products' digits together.
    2. Take this result, and add it to the sum of the digits that weren't multiplied by 2.
    3. If the total's last digit is 0, then that credit card number is valid.

## Example Case
+ Consider an example of Luhn's algorithm with the following American Express number: 378282246310005
+ For the sake of clarity, I have underlined every other digit, starting with the number's second-to-last digit:

$$
3\underline{7}8\underline{2}8\underline{2}2\underline{4}6\underline{3}1\underline{0}0\underline{0}5
$$

+ Then, multiply each of the underlined digits(highlighted in bold) by 2:

$$
\textbf{7}\cdot{2} + \textbf{2}\cdot{2} + \textbf{2}\cdot{2} + \textbf{4}\cdot{2} + \textbf{3}\cdot{2} + \textbf{0}\cdot{2} + \textbf{0}\cdot{2}
$$

+ The partial products are as follows:

$$
14 + 4 + 4 + 8 + 6 + 0 + 0
$$

+ Next, add those products' digits(**Note:** not the products themselves) together:

$$
1 + 4 + 4 + 4 + 8 + 6 + 0 + 0 = 27
$$

+ Now, add the result of 27 to the sum of the digits in the credit card number that **weren't** multiplied by 2:

$$
27 + 3 + 8 + 8 + 2 + 6 + 1 + 0 + 5 = 60
$$

+ Notice that the last digit in the result of 60 is a 0, so the credit card number is legitimate.

## Hints
+ Note that the credit card number is being brought into the function as a string. This means that you will have to perform string slicing throughout your program, and convert between string values and integers. Use `int()` and `str()` to perform these conversions.
+ Luhn's algorithm clearly specifies that you must sum the digits starting from the **second-to-last digit**. Does this mean that you have to perform a reverse loop? Not necessarily. Think about what happens when a credit card has an **odd** quantity of digits, it means that we have to sum all of the elements located at the **odd-numbered** indexes:

$$
3\underline{7}8\underline{2}8\underline{2}2\underline{4}6\underline{3}1\underline{0}0\underline{0}5
$$

+ Now, think about what happens when a credit card has an **even** quantity of digits. In this case, we have to sum all of the elements located at the **even-numbered** indexes:

$$
\underline{5}1\underline{0}5\underline{1}0\underline{5}1\underline{0}5\underline{1}0\underline{5}1\underline{0}0
$$

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Credit Card | 1.4KB | [pset10.zip](/csp/zip/pset10.zip)

**Contents of `pset10.zip`:**
```bash
PSet10CreditCard/
├── creditcard.py
└── testcreditcard.py
```

## Specification
+ Write a `Python` program in the file `creditcard.py` which calculates the amount of radiation exposure in a given time period.
+ You will write your solution in a function called `validate(digits)` right below the place where it says: `YOUR CODE HERE`
+ If the credit card number is valid, then your `validate` function should return a string corresponding to the specific credit card brand. These return values should be `AMEX`, `MASTERCARD`, `VISA`, or `VALID`. Otherwise, if the credit card number is not valid, then your `validate` function should return the string `INVALID`.
+ When the function call `validate("378282246310005")` is executed, the output of the program should be: `AMEX`

## Testing
+ Run the file `testcreditcard.py` to execute the `PyUnit` test bench. `PyUnit` indicates a successful test with an `OK` output, and an unsuccessful test with a `FAIL` output.

## Submission
+ Upload the file `creditcard.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

