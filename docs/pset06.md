# Problem Set 6: Vending Machine

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Wednesday, October 23, 2019
+ **Total Points:** 10
+ Implement a `Python` program that dispenses the correct amount of change, depending on
the stock of coins in the machine.

## Background Theory
+ You will write a program that simulates the behaviour of a coin-operated vending machine, a device that was in common use until recently.
+ A vending machine operates as follows: A customer selects an item for purchase, then inserts a certain amount of cash to cover the cost of the item. The product is then dispensed, and if change is due to the customer, it is provided in the form of coins.
+ The vending machine we will consider has a **finite stock** of the following coins: **25 cents(quarters)**, **10 cents(dimes)**, and **five cents(nickels)**. Note that pennies will be
excluded from consideration.
+ The amount of change due to a customer is calculated according to the following simple relation: `change = payment - cost`.
+ The vending machine should then dispense the **minimum quantity** of coins necessary to provide
the change to the customer.
+ However, what would happen if the machine completely ran out of a particular coin denomination, for instance, the quarter? In that case, the machine would have to fulfill its obligation by using its remaining stock of dimes and nickels.
+ Note that the output of this program should be the **quantity of coins** that are dispensed by the vending machine.

## Example Case
+ Consider the case where a customer deposits `200` cents into a vending machine, to purchase a product costing `70` cents. The change due to the customer is `130` cents.
+ Then, let's say that the vending machine has a coin stock of `3` quarters, `3` dimes and `10` nickels.
+ The vending machine will then dispense `3` quarters, `3` dimes and `5` nickels to the customer, which
is `11` coins in total. Your program should return `11` as its result.

## Hints
+ Assume that the customer always deposits paper currency as payment. In other words, the payment placed into the vending machine does not replenish the coin stocks.
+ Every time you dispense a coin to the customer, reduce that coin stock by one.
+ The `cost` of the products, and the `payment` deposited, are all denominated in **cents**.
This greatly simplifies the programming involved.
+ You must calculate the **minimum quantity** of coins possible to fulfill the amount of change due
to the customer.
+ We won't consider the case where the vending machine has an insufficient stock of coins
to cover the amount of change due to the customer. There will always be enough coins in each case.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Vending Machine | 1.3KB | [pset06.zip](/csp/zip/pset06.zip)

**Contents of `pset06.zip`:**
```bash
PSet06VendingMachine/
├── testvendingmachine.py
└── vendingmachine.py
```

## Specification
+ Write a `Python` program in the file `vendingmachine.py` that dispenses the correct amount of change, depending on the stock of coins in the machine.
+ You will write your solution in a function called `dispensechange(quarters, dimes, nickels, cost, payment)`
right below the place where it says: `YOUR CODE HERE`
+ When the function call `dispensechange(5, 5, 5, 160, 200)` is executed, the
output of the program should be: `3`

## Testing
+ Run the file `testvendingmachine.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `vendingmachine.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.

