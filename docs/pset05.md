# Problem Set 5: Water Meter

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Wednesday, October 16, 2019
+ **Total Points:** 10
+ Implement a `Python` program that calculates the amount of money that a customer
will be billed, based on their water usage.

## Background Theory
+ A water utility is responsible for supplying clean, fresh water to its customers in a
given geographical area.
+ The water utility will typically charge different rates for each category of customer.
Supplying water to individual households is relatively straightforward, so they are charged
minimal rates. However, commercial and industrial factories may require massive amounts of
water, so they are charged more for the necessary supporting infrastructure.
+ A customer's water bill depends on how many gallons of water they consumed during a particular
billing period.
+ A water meter is used to determine a customer's water consumption. It consists of a dial that
has nine digits. However, note that the **final digit** in the dial records **one-tenth of a gallon**.
+ In other words, if the water meter reads `923874345` then this corresponds to 92387434.5 gallons.
+ The water meter is read once at the beginning of the billing period, and then once and the end. A customer's water consumption, in gallons, is computed from the difference in these two meter readings.

## Customer Categories
+ There are three categories of customer: **residential**, **commercial**, and **industrial**.
The following is the fee schedule for each of these categories:

### `residential`
+ A base rate of $5.00, plus $0.0005 per gallon used.

### `commercial`
+ A base rate $1000.00 for 40000 gallons or less, plus $0.00025 for each additional gallon used.

### `industrial`
+ A base rate of $1000.00 for 40000 gallons or less. A base rate of $2000.00 if usage exceeds 40000 gallons, but does not exceed 80000 gallons. A base rate of $3000.00 plus $0.00025 for each additional gallon if usage exceeds 80000 gallons.

## Hints
+ Note that the meter's dial has nine digits and records the tenths of a gallon. For example, if the beginning reading was `444400003` and the ending reading was `444400135`, then the customer used 13.2 gallons of water during that billing period.
+ We won't consider the case where the water meter "flips over" from `999999999` to `000000000`.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Water Meter | 1.4KB | [pset05.zip](/csp/zip/pset05.zip)

**Contents of `pset05.zip`:**
```bash
PSet05WaterMeter/
├── testwaterbilling.py
└── waterbilling.py
```

## Specification
+ Write a `Python` program in the file `watermeter.py` that determines the amount of money
that a customer must pay for their water usage during a particular billing period.
+ You will write your solution in a function called `calculatebill(customer, begin, end)`
right below the place where it says: `YOUR CODE HERE`
+ When the function call `calculatebill("residential", 444400003, 444400135)` is executed, the
output of the program should be: `5.0066`

## Testing
+ Run the file `testwatermeter.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `watermeter.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.
