The girl named Masha was walking in the forest and found a complete binary tree of height n
 and a permutation p
 of length m=2n
.

A complete binary tree of height n
 is a rooted tree such that every vertex except the leaves has exactly two sons, and the length of the path from the root to any of the leaves is n
. The picture below shows the complete binary tree for n=2
.

A permutation is an array consisting of n
 different integers from 1
 to n
. For example, [2,3,1,5,4
] is a permutation, but [1,2,2
] is not (2
 occurs twice), and [1,3,4
] is also not a permutation (n=3
, but there is 4
 in the array).

Let's enumerate m
 leaves of this tree from left to right. The leaf with the number i
 contains the value pi
 (1≤i≤m
).

For example, if n=2
, p=[3,1,4,2]
, the tree will look like this:


Masha considers a tree beautiful if the values in its leaves are ordered from left to right in increasing order.

In one operation, Masha can choose any non-leaf vertex of the tree and swap its left and right sons (along with their subtrees).

For example, if Masha applies this operation to the root of the tree discussed above, it will take the following form:


Help Masha understand if she can make a tree beautiful in a certain number of operations. If she can, then output the minimum number of operations to make the tree beautiful.

Input
The first line contains single integer t
 (1≤t≤104
) — number of test cases.

In each test case, the first line contains an integer m
 (1≤m≤262144
), which is a power of two  — the size of the permutation p
.

The second line contains m
 integers: p1,p2,…,pm
 (1≤pi≤m
) — the permutation p
.

It is guaranteed that the sum of m
 over all test cases does not exceed 3⋅105
.

Output
For each test case in a separate line, print the minimum possible number of operations for which Masha will be able to make the tree beautiful or -1, if this is not possible.

Example
input
4
8
6 5 7 8 4 3 1 2
4
3 1 4 2
1
1
8
7 8 4 3 1 2 6 5
output
4
-1
0
-1