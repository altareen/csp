# Lab 6: Smooth Signal

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Friday, November 1, 2019
+ **Total Points:** 10
+ Implement a `Python` program that smoothes an audio signal by averaging a list of integers.

## Background Theory
+ An audio signal is sometimes stored as a list of integer values. The values represent the intensity of the signal at successive time intervals. Of course, in a program, the signal is represented with a list.
+ Often, a small amount of noise is included in the signal. Noise is usually small, momentary changes in the signal level. An example is the **static** that is heard in addition to the signal in AM radio.
+ Smoothing a signal removes some of the noise, and improves the perceptual quality of the signal. This assignment requires you to smooth the values in a list of integers.

## Hints
+ First, you should create a result list called `smooth`, which has exactly the same size as the `audio` list. Recall that the multiplication operator can be used to create a list which is initialized with zeroes:
```python
smooth = [0] * len(audio)
```
+ The first element of the `smooth` list is a special case, because it should be calculated from the average of the **first** two elements of the `audio` list.
+ The last element of the `smooth` list is also a special case, because it should be calculated from the average of the **last** two elments of the `audio` list.
+ The internal elements of the `smooth` list can be calculated from a `for` loop in the following manner. First, you will need to determine the boundaries of this loop. You should probably begin at index `1`, and go up to index `len(audio)-1`. Recall that the `for` loop has the following variation:
```python
for i in range(start, stop):
```
This means that the loop will begin at `start`, and go up to(but not include) `stop`.
+ Then, you will need to calculate the average of three elements in the `audio` list, for every index `i`. In other words, you will need to calculate the average of the three values: `audio[i-1], audio[i], and audio[i+1]`.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Smooth Signal | 1.8KB | [lab06.zip](/csp/zip/lab06.zip)

**Contents of `lab06.zip`:**
```bash
Lab06SmoothSignal/
├── smoothsignal.py
└── testsmoothsignal.py
```

## Specification
+ Write a `Python` program in the file `smoothsignal.py` that smoothes an audio signal by averaging a list of integers.
+ You will write your solution in a function called `levelling(audio)` right below the place where it says: `YOUR CODE HERE`
+ When the function call `levelling([1, 5, 4, 5, 7, 6, 8, 6, 5, 4, 5, 4])` is executed, the output of the program should be: `[3 3 4 5 6 7 6 6 5 4 4 4 ]`

## Testing
+ Run the file `testsmoothsignal.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `smoothsignal.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.
