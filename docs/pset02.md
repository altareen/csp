# Problem Set 2: fahrenheit

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Background
+ **Due Date:** Monday, September 16, 2019
+ **Total Points:** 10
+ In this problem set, you must write a `Python` program that performs a simple
temperature conversion.

## Code Distribution

Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for fahrenheit | 1.1KB | [pset02.zip](/csa/zip/pset02.zip)

**Contents of `pset02.zip`:**
```bash
PSet02SourceCode/
├── fahrenheit.py
└── testfahrenheit.py
```

## Specification
+ Write a `Python` program in the file `fahrenheit.py` that
converts a temperature from celsius to fahrenheit. The formula for this
conversion is as follows: Take the temperature in celsius, multiply it by 9,
divide the result by 5, and add 32. The equation can be expressed as:

$$
\mbox{fahrenheit} = \frac{\mbox{celsius} \times 9}{5} + 32
$$

+ You will write your solution
in a function called
`calculatefahrenheit(celsius)`,
right below the place where it says: `YOUR CODE HERE`.

+ When the function call `calculatefahrenheit(100)` is executed, the
output of the program should be: `212.0`

## Testing
+ Run the file `testfahrenheit` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `fahrenheit.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

