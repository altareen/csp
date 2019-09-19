# Lab 3: Movie Critic

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Friday, September 20, 2019
+ **Total Points:** 10
+ In this lab, you must write a `Python` program that determines the user's interest
in seeing a particular movie.

## Background Theory
+ You interest in a movie depends upon the following two factors:
    1. The `price` of the movie's ticket, in dollars.
    2. The `rating` which the movie received, which can be any decimal number from 0 to 5, inclusive.
+ Your level of interest in a movie is shown by the following indicators:
    + `extremely interested`
    + `very interested`
    + `moderately interested`
    + `barely interested`
    + `completely uninterested`
+ The following are the criteria upon which you make your movie viewing decisions. *Hint:*
Implement these in `Python` using an `if-elif-else` code structure.
    1. You like bargains. Any movie that costs less than $5.00 is one that you are `extremely interested` in viewing, as long as that movie has received 2 or more stars.
    2. You dislike expensive movies. If a movie costs $12.00 or more, then you are `completely uninterested` in seeing it. However, if that movie happened to recieve 5 stars, then you are `barely interested` in seeing it.
    3. You enjoy high quality movies. You are `very interested` in seeing any movie that has a price below $12.00, and is rated greater than 4 stars.
    4. You are `moderately interested` in seeing any movie which costs between $5.00 and $11.99, as long as those movies received between 2 and 4 stars, inclusive.
    5. You dislike poorly rated movies. Any movie that has received less than 2 stars is one that you are `barely interested` in seeing, as long as it costs less than $5.00.
    6. If any movie falls outside of the previously mentioned criteria, then you are `completely uninterested` in seeing it.

## Code Distribution

Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Movie Critic | KB | [lab03.zip](/csp/zip/lab03.zip)

**Contents of `lab03.zip`:**
```bash
```

## Specification
+ Write a `Python` program in the file `moviecritic.py` that produces an output which
corresponds to your particular interest in a certain movie.
+ You will write your solution in a function called `temperedscale(octave, pitch)`
right below the place where it says: `YOUR CODE HERE`
+ When the function call `selectfilm(6.5, 3,5)` is executed, the
output of the program should be: `moderately interested`

## Testing
+ Run the file `testmoviecritic.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `moviecritic.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

