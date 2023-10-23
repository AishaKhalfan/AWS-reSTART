# Preparing to Analyze Insulin with Python

## Lab overview
In information technology, Python works well as the programming language of choice for manipulating strings, sequences, and numbers. Python is especially preferred in scientific computing applications such as physics, chemistry, and biology.

In some of the labs for the Python modules, you will perform simple sequence manipulations and calculations on human insulin, which is a well-known hormone in the human body that is responsible for regulating sugars.

In this lab, you will:

- Retrieve the protein sequence of human insulin from human preproinsulin

## Exercise 1: Retrieving the protein sequence of human preproinsulin
The National Center for Biotechnology Information (NCBI) has information on many biological sequences.

- Access NCBI at [NCBI](https://ncbi.nlm.nih.gov.)

- Next to the search bar, choose the dropdown menu and select Protein. Next, in the search bar, enter human insulin and choose Search.
- Choose the following search result: insulin [Homo sapiens].
- At the bottom of the search record, copy the insulin sequence, which starts with the word ORIGIN and ends with //.
- In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as preproinsulin-seq.txt.

- Paste the insulin sequence into preproinsulin-seq.txt:

``
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
``
**Bonus: Cleaning preproinsulin-seq.txt programmatically**
Cleaning source data files is a common task in computer programming. You could programmatically clean preproinsulin-seq.txt in several ways—for example, by using Bash, Python, or another programming language of choice. Try using regex to programmatically strip the file of ORIGIN, its numbers, the two slashes (//), spaces, and line breaks or return carriages. You could also confirm programmatically that the file has 110 characters.

## Exercise 2: Obtaining the protein sequence of human insulin
Insulin is obtained from preproinsulin through a series of cut-and-paste procedures. Preproinsulin contains a 24aa signal sequence and an 86aa proinsulin molecule. Amino acids 25–54 and amino acids 90–110 are the processed insulin molecule. Use Python, Bash, or manual manipulation to retrieve only those amino acids in the sequence that compose insulin.

Manually or programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages.

- In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as preproinsulin-seq-clean.txt.

- In the file preproinsulin-seq-clean.txt, copy your results.

- Confirm that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin.

- In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as lsinsulin-seq-clean.txt.

- In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.

- In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as binsulin-seq-clean.txt.

- In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.

- In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as cinsulin-seq-clean.txt.

- In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.

- In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as ainsulin-seq-clean.txt.

- In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.

- Deciding when to automate and when to work manually: A discussion about scope versus time
Automating your work versus working manually is a dilemma for computer programmers. Too much automation wastes time on coding, whereas too little restricts the scope of your program. Try to balance your automation with working manually in an effort to create a program with the most scope for the least time spent coding. In this case, it is probably not worth the extra coding time to programmatically clean insulin-seq.txt to insulin-seq-clean.txt. However, if you needed to download thousands or millions of files and do the same task, automation would be good to explore.

Congratulations! You have prepared data for further processing. Manually preparing these files should help you appreciate the automation that Python can provide.


