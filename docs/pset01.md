# Problem Set 1: helloworld

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Background
+ **Due Date:** Monday, September 9, 2019
+ **Total Points:** 10
+ This problem set introduces you to the **write-run** software development
cycle, with a very simple code framework.

## Code Distribution

Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for helloworld | 1.1KB | [pset01.zip](/csa/zip/pset01.zip)

**Contents of `pset01.zip`:**
```bash
PSet01SourceCode/
├── helloworld.py
└── testhelloworld.py
```

## Specification

### Using the Assignment Operator
+ Write a `Python` program in the file `helloworld.py` that
uses the assignment operator to assign the message `hello world` to
the `string` variable `greetings`.

+ You will write your solution in a **method** called
`displaymessage()`, right below the place
where it says: `YOUR CODE HERE`. Make sure that
the phrase `hello world` is placed in the variable `greetings`.
Save your code by using the keystroke combination `Ctrl-s`.

### Executing your `Python` Program
+ Now, you must **run** your `Python` program. Click on the
`Run` menu item, and select `Run...`

![Select menu](/csp/img/pset01Step01.png)

+ Then, you should see the `Run` dialog box appear. Select the
file: `helloworld`

![Method call](/csp/img/pset01Step02.png)

+ The output of your program should appear in the `Console` at
the bottom of your window. You should see the words `hello world`
displayed on the output.

![Terminal window](/csp/img/pset01Step03.png)

## Testing
+ Now, we are going to verify that we have a correct `Python`
program by using the `PyUnit` testing feature.

+ In order to run the `PyUnit` test bench, click on the `Run` menu item,
and select `Run...`

![Select menu](/csp/img/pset01Step01.png)

+ The `Run` dialog box should appear. This time, select the
file: `testhelloworld`

![Test bench](/csp/img/pset01Step04.png)

+ You should then see the results of the `PyUnit` test. Since this is an
example of a successful test, the word `OK` appears.

![Successful test](/csp/img/pset01Step05.png)

## Submission
+ Upload the file `helloworld.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

