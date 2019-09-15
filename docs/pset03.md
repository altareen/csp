# Problem Set 3: Note Frequency

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Background
+ **Due Date:** Monday, September 23, 2019
+ **Total Points:** 10
+ Implement a `Python` program that calculates the frequency of a particular music
note, given its octave and pitch class.

## Theory
+ One of the oldest problems in music theory is how to map the notes of a musical
piece to a set of audio frequencies. Your task is to write a `Python` program that
performs a particular kind of mapping.
+ First, we must define a form of musical note notation. One common way of accomplishing
this is to use the *octave pitch* notation. This notation represents each note as
a number pair, where the first number indicates which *octave* the note belongs to, and
the second number indicates which semitone the *pitch* corresponds to.
+ There are 12 **semitone notes** within each octave on the keyboard, as in the
following diagram:

![Semitone notes](/csp/img/semitones.png "Semitone notes")

+ *octave pitch* representations are written in decimal format. For example, the
5th octave and 9th semitone(corresponding to note A) would be written as: 5.9
+ In order to map a sound frequency to this *octave pitch* representation, we must
begin by selecting a reference note. In the Western musical scale, we assign the
frequency 440Hz to the *octave pitch* reference note of 4.9. This corresponds to
the 4th octave, 9th semitone, which is note A.
+ Our mapping must ensure that the same note in the next higher octave has double
the frequency. In other words, 5.9 corresponds to 880Hz, and 3.9 corresponds to
220Hz. This mapping system assumes that each of the semitones within an octave is
equally spaced, and this is known as a **tempered scale.**
+ The formula we use to calculate the frequency from a given *octave pitch* note is as follows:
```python
frequency = ref * 2 ** (oct + (sem/12.0))
```
+ `frequency`: The result of the calculation, in Hertz.
+ `ref`: The frequency of the reference note, 440Hz.
+ `oct`: The *octave* note minus the reference note.
+ `sem`: The *pitch* semitone minus the reference semitone.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for fahrenheit | KB | [pset03.zip](/csp/zip/pset03.zip)

**Contents of `pset03.zip`:**
```bash
```

## Specification
+ Write a `Python` program in the file `notefrequency.py` that calculates the
frequency of a particular musical note, given its *octave* and *pitch* class.
+ You will write your solution in a function called `temperedscale(octave, pitch)`
right below the place where it says: `YOUR CODE HERE`
+ When the function call `temperedscale(0, 0)` is executed, the
output of the program should be: `16.351597831287414`

## Testing
+ Run the file `testnotefrequency.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `fahrenheit.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

