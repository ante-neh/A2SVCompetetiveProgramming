​The main idea is simple - Go through each character, if we meet a special character, check whether the next character is one that is of interest to us (comment tokens) and then toggle some states that will determine whether we append the character to the final source.

Some insights:

There are three important tokens we want to identify within the source code //, /* and */.
We use a variable called buffer that acts as a buffer to store the characters that will definitely go into the final source code. This buffer can contain characters from multiple lines because of block comments.
We use another variable block_comments_open to keep track of whether we are inside a block comment or not.
At the end of each source line, we simply have to check whether we are inside of a block comment or not (i.e. block_comments_open is True) to decide whether we want to flush the buffer and append it to the results.
In each loop, we have to check that:

// - If it is a line comment and not part of a block comment, skip the rest of the line by shifting the pointer to the end of the line.
/* - If it is an opening block comment token and not part of a block comment, set block_comments_open to True.
*/ - If it is a closing block comment token and part of a block comment, set block_comments_open to False.
Else append to buffer if not part of a block comment.
Bonus

There are many parsing/compiler type questions in LeetCode, and here are some tips on handling them:

Use a pointer to read each character so that you can skip characters if the current token is made by more than one character, such as //, /* and */.
For Python, use a while loop. You can't skip characters if you used for i in range(...) unlike in C++ or Java where you can have control of how you want to increment i at the end of each loop.
