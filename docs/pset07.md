# Problem Set 7: Down Payment

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Monday, November 4, 2019
+ **Total Points:** 10
+ Implement a `Python` program that determines how many months it will take to save up enough money for a down payment on a house.

## Background Theory
+ Let's assume that you have grown weary of living in dormitories, and you wish to save up enough money for a down payment on a house. The down payment is 25% of the the total cost of the house.
+ Since housing is very expensive, it will probably take you several years to accomplish this task. In this program, we will measure this time duration in terms of months.
+ Let's also assume that you have a well-paying job, in which you earn a respectable annual salary. As well, you have a savings account which generates an annual rate of return.
+ Furthermore, your place of employment provides you with pay raises on a semi-annual basis. That is, your salary will increase by a certain decimal percentage after the 6th month, the 12th month, the 18th month, and so on.

## Parameters
+ The following is an explanation of the parameters used in the `savingsduration()` function:

#### `annualsalary`
+ This is the annual salary which you earn from your job.

#### `percentsaved`
+ This is the amount of your salary which you will dedicate towards saving for the down payment. It should be expressed in decimal form, for example: `0.1`

#### `totalcost`
+ This is the purchase price of your dream home.

#### `payraise`
+ This is the amount by which your salary is increased, and these raises occur every six months. This should be expressed in decimal form, for example: `0.1`

## Hints
+ You will need to determine the amount of the **down payment**, which can be calculated from: `totalcost*0.25`
+ Since the time duration is measured in months, you will need to determine your **monthly salary**. This can be calculated from: `annualsalary/12.0`
+ The amount that you have saved so far should be referred to as your **current savings**, and you begin with a current savings of: `0`
+ Assume that your savings account generates an annual **rate** of return of 4%. In other words, `rate = 0.04`
+ Create a variable that keeps track of the number of **months** that have occurred in this simulation, and set this variable to: `0`
+ Assume that you invest your current savings wisely, so at the end of each month, you receive an additional `currentsavings*rate/12.0` to be put into your savings.
+ Be careful about when you increase your salary due to the pay raise. This should only happen after the 6th month, 12th month, 18th month, and so on.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Down Payment | 1.4KB | [pset07.zip](/csp/zip/pset07.zip)

**Contents of `pset07.zip`:**
```bash
PSet07DownPayment/
├── downpayment.py
└── testdownpayment.py
```

## Specification
+ Write a `Python` program in the file `downpayment.py` that outputs the number of months that would be required to save enough money for a down payment on a house, given the annual salary that you earn, and the return on your investments.
+ You will write your solution in a function called `savingsduration(annualsalary, percentsaved, totalcost, payraise)` right below the place where it says: `YOUR CODE HERE`
+ When the function call `savingsduration(120000, 0.05, 500000, 0.03)` is executed, the output of the program should be: `142`

## Testing
+ Run the file `testdownpayment.py` to execute the `PyUnit` test bench. `PyUnit` indicates a successful test with an `OK` output, and an unsuccessful test with a `FAIL` output.

## Submission
+ Upload the file `downpayment.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.
