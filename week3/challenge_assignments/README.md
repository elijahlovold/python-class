In this file are some more challenges to help practice our content


1. Print out a multiplication table up to some number N that the user chooses. 
    bonus: make the grid print perfectly square regardless of number range.

2. input some string from user and count the number of vowels.

3. make a function for computing the factorial of a number.

4. make a number guessing game where the user can input a range of numbers to 
    guess between and it guides them with too low/high until they guess it.
    Note, you can use `randint(min, max)` from the random module to generate the number. 
    import the function like: `from random import randint`

5. input a list of items from the user util they type \n or some escape sequence.   
    Calculate the following statistics of the list:
    * number of elements
    * if a list of ints: 
        * sum
        * average
        * min
        * max
    * if not ints: 
        * num of words
        * num of characters

Note, in my solutions, i put some commonly used functions in a file called 
utils in the same directory. Of course, I haven't explained how to import 
functions from other files, basically, type:
`'from' name_of_file 'import' name_of function` 
just like the format above for importing randint. 
Of course, there are other ways to import, I'll cover these shortly.
