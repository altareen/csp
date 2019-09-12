# Lab 2: Easter Sunday

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Background
+ **Due Date:** Thursday, September 12, 2019
+ **Total Points:** 10
+ In this lab, you must write a `Python` program that determines which particular
day and month that Easter Sunday appears.

## Code Distribution

Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Easter Sunday | 1.2KB | [lab02.zip](/csp/zip/lab02.zip)

**Contents of `lab02.zip`:**
```bash
Lab02EasterSunday/
├── eastersunday.py
└── testeastersunday.py
```

## Specification
+ Write a `Python` program in the file `eastersunday.py` that
computes the date of Easter Sunday, given a particular year. Easter Sunday
is a holiday which falls on the first Sunday after the first full moon of
Spring. This algorithm was discovered by Carl Friedrich Gauss.
+ The parameter `year` is the variable for the year in question.
In the provided code, `year` takes on the value `2001`.
+ Your program must perform the following calculations:
  1. Divide `year` by `19` and call the remainder `a`. Ignore the quotient. 
  2. Divide `year` by `100` to get a quotient `b` and a remainder `c`. 
  3. Divide `b` by `4` to get a quotient `d` and a remainder `e`. 
  4. Divide `(8 * b + 13)` by `25` to get a quotient `g`. Ignore the remainder. 
  5. Divide `(19 * a + b - d - g + 15)` by `30` to get a remainder `h`. Ignore the quotient.
  6. Divide `c` by `4` to get a quotient `j` and a remainder `k`.
  7. Divide `(a + 11 * h)` by `319` to get a quotient `m`. Ignore the remainder. 
  8. Divide `(2 * e + 2 * j - k - h + m + 32)` by `7` to get a remainder `r`. Ignore the quotient.
  9. Divide `(h - m + r + 90)` by `25` to get a quotient `n`. Ignore the remainder. 
  10. Divide `(h - m + r + n + 19)` by `32` to get a remainder `p`. Ignore the quotient.
+ The result is that Easter Sunday falls on day: `p` of the month: `n`.
+ For example, given the year `2001`, we find that the result is:
`n = 4` and `p = 15`. This means that Easter Sunday was on April 15 in the year 2001.
+ You will write your solution in a function called
`retrievedate(year)`,
right below the place where it says: `YOUR CODE HERE`.

## Testing
+ Run the file `testeastersunday.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `eastersunday.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

