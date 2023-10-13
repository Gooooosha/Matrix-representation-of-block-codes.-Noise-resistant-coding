# Matrix-representation-of-block-codes.-Noise-resistant-coding
Noise-resistant coding with a graphical pyqt interface. With the possibility of entering a matrix G or H, encoding and decoding text, with the introduction of a random error.

## Encoding 

The algorithm starts by determining whether the input matrix belongs to H 
or G 
H - verification 
G - generating 
If the input matrix is H, we find its systematic form
The unit diagonal is located at the end of the matrix
Transpose systematic H - get HsysT (for decoding)
From systematic H we find systematic G 
We discard the unit diagonal, transpose the remainder and assign to the 
the unit matrix. Count the number of rows and columns 
n - columns
k - rows 
Assign the value i = k and select all possible combinations.
Number of combinations = 2**k (2, because the possible characters are 0 and 1).
Combinations i
For each vector of the array i we get the value of c 
To get c we must multiply vector i by Gsys 
Examples:
when i = 001 - rewrite the last row of the matrix 00110011
at i = 101 - 2 rows (add the first and the last rows modulo 2 (XOR))
0011011
1001001
1010010 - result
We got an array of values c 
Then we count the parameter d (the number of units in each line c). 
Find d min - the minimum natural value of the array d
Using d min we find t and p
t - number of corrected errors 
p - number of detected errors  
p = dmin - 1
t = (p) // 2
t is always rounded down 
We split the source text in binary form into blocks of length k (parameter k 
from Gsys). In case of missing elements in the last block we add 
zeros up to the size k. The number of added characters should be memorized 
Then we turn to the table of information and codewords (table i : c).
If the block and the value i match, we change the block to the corresponding value c. 
value c 
c at i = 001 equals 0011011.
If the first block = 001 it becomes 0011011
In each block we add errors, number = t. 
In this case we inverted the characters from the beginning with length t = 1.

## Decoding 

We use the already transposed systematic matrix HsysT
Read its dimensions
Length e - number of rows 
Length S - number of columns

Build a table e | S
The primary vector e consists of 0 with length equal to the number of rows
Then the value 1 appears, the number of units depends on t, it can be 2, 3, etc. 
etc. All combinations must be taken into account. The values drift from the end to the 
beginning.

Each vector e is multiplied by the matrix HsysT - we get S
The multiplication is done in the same way as in the table i : c

For each block with an error we need to find this location.
To do this, we multiply the block with error by HsysT 
We get the value of S and identify it with the table
S = 1001 
With this S value e 1000000
So the error is in the first bit. 

Change it, go to the next block. 

When we have corrected all the blocks we must get the values equal to c from the 
table of information and codewords. We replace these c back to i. 
We get the sequence after splitting into blocks. 
We refer to the data about adding zeros to the last block. All 
added zeros we must remove and then we will get the binary form 
of the source text.

![img](https://github.com/Gooooosha/Matrix-representation-of-block-codes.-Noise-resistant-coding/blob/main/img_for_readme/1.png)

![img](https://github.com/Gooooosha/Matrix-representation-of-block-codes.-Noise-resistant-coding/blob/main/img_for_readme/2.png)
