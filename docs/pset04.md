# Problem Set 4: Quarterback Rating

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Tuesday, October 8, 2019
+ **Total Points:** 10
+ Implement a `Python` program that calculates the **quarterback rating,** which
is a measure of the performance of a quarterback, in the game of American football.

## Background Theory
+ The game of American football is one of the more popular sports that is played
in the U.S.
+ The objective of the game is to advance the ball into a special region called
the **end zone.** One of the more effective ways to accomplish this task, is for
one of the players to throw the ball down the field. The player who is responsible
for throwing the ball is called the **quarterback.**
+ Throwing a football is a highly specialized skill, and some players are better
at it than others. There is an equation which objectively evaluates how good a
quarterback has performed during a particular game, based on a series of factors.
+ This **quarterback rating** equation is based on the following four factors:
completion percentage, yards per attempt, touchdowns per attempt, and interceptions
per attempt. Each of those factors is scaled to a value between `0` and `2.375`. A
description of each of these factors is as follows:
    + **Completion Percentage:** This reflects the quantity of successful passes that the quarterback has made, compared with the number of attempted passes.
    ```python
    a = (1.0*comps/attempts - 0.3) * 5
    ```
    + **Yards Per Attempt:** This indicates the number of yards that the quarterback has obtained by passing the football, compared with the number of attempted passes.
    ```python
    b = (1.0*yards/attempts - 3) * 0.25
    ```
    + **Touchdowns Per Attempt:** This indicates the quantity of touchdowns that the quarterback has achieved, compared with the number of attempted passes.
    ```python
    c = 20.0 * tdowns/attempts
    ```
    + **Interceptions Per Attempt:** This details the number of times that an opposing player has inadvertently caught the football, compared with the number of attempted passes. An interception is also known as a **pick.**
    ```python
    d = 2.375 - (25.0 * picks/attempts)
    ```
+ The following is an explanation of the variables used in the above mentioned equations:
    + `attempts`: The number of passing attempts.
    + `comps`: The number of completions, or successful passes.
    + `yards`: The quantity of yards gained by passing the football.
    + `tdowns`: The number of touchdowns obtained by passing the football.
    + `picks`: The number of interceptions, that is, when the football is caught by a member of the opposing team.
+ **Note:** If the result of any one of the above equations is greater than `2.375`,
then that factor is set to `2.375`. Also, if the result of any one of those equations
is a negative number, then that factor is set to `0`.
+ The above calculations are used to determine the quarterback rating in the following manner:
```python
rating = ((a + b + c + d) / 6.0) * 100
```

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Quarterback Rating | 1.4KB | [pset04.zip](/csp/zip/pset04.zip)

**Contents of `pset04.zip`:**
```bash
PSet04QuarterbackRating/
├── quarterbackrating.py
└── testquarterbackrating.py
```

## Specification
+ Write a `Python` program in the file `quarterbackrating.py` that calculates the
quarterback rating, which reflects the performance of a quarterback in a particular
game.
+ You will write your solution in a function called `calculaterating(attempts, comps, yards, tdowns, picks)`
right below the place where it says: `YOUR CODE HERE`
+ When the function call `calculaterating(35, 26, 235, 2, 1)` is executed, the
output of the program should be: `99.10714285714288`

## Testing
+ Run the file `testquarterbackrating.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `quarterbackrating.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

