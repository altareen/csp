# Lab 5: Gene Detection

!!! note ""
    [Web-CAT:](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) Submit `Python` programs to this automated grading platform.

## Task Outline
+ **Due Date:** Friday, October 18, 2019
+ **Total Points:** 10
+ Implement a `Python` program that determines which genes are present in a DNA sequence.

## Background Theory
+ DNA is often described as a double helix of molecules known as **nucleotides**. Only four DNA nucleotides exist, and they are known by the labels A, C, G, and T. This means that we can conveniently represent a DNA sequence with a Python text string.
+ A cluster of three nucleotides is called a **codon**, and they represent amino acids which are present in DNA. For example, ATG is a codon which occurs throughout a DNA sequence. Codons are significant, because they are markers which indicate the presence of a **gene**.
+ ATG is the **start codon** which marks the beginning of a gene sequence. All of the nucleotides which are present, right up to, and including the **stop codon** are part of the gene.

## Example Case
+ Consider the following DNA sequence: `ATATGTAGCTAGCATAATA`
+ The start codon is `ATG`, and the stop codon for this example is `TAA`. Note that there are 9 nucleotides between these codons: `AT` `ATG` `TAGCTAGCA` `TAA` `TA`
+ Therefore, the gene sequence which results from these codons is: `ATGTAGCTAGCATAA`

## Hints
+ Note that we will not consider the case where a gene is absent from a DNA sequence. All of the DNA sequences used in the test benches have exactly one gene for you to find.
+ Also, each of the DNA sequences will have exactly one stop codon for your program to locate. In other words, there will not be multiple stop codons in the gene sequences.

## Code Distribution
Description | File Size | File Name
----------- | --------- | ---------
`Python` Source Code for Gene Detection | 1.4KB | [lab05.zip](/csp/zip/lab05.zip)

**Contents of `lab05.zip`:**
```bash
Lab05GeneDetection/
├── genedetection.py
└── testgenedetection.py
```

## Specification
+ Write a `Python` program in the file `genedetection.py` that finds and displays a single gene which is present in a DNA sequence.
+ You will write your solution in a function called `findgene(dna, stopcodon)` right below the place where it says: `YOUR CODE HERE`
+ When the function call `findgene("ATATGTAGCTAGCATAATA", "TAA")` is executed, the output of the program should be: `ATGTAGCTAGCATAA`

## Testing
+ Run the file `testcoinchange.py` to execute the `PyUnit` test bench.
`PyUnit` indicates a successful test with an `OK` output, and an unsuccessful
test with a `FAIL` output.

## Submission
+ Upload the file `coinchange.py` to the [Web-CAT](http://ec2-54-65-207-33.ap-northeast-1.compute.amazonaws.com:8080/Web-CAT/WebObjects/Web-CAT.woa) automated grading platform.
