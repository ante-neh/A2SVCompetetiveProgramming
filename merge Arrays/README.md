A. Merging Arrays
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
For educational purposes, in the problems of this block, the time limit is large enough for the solution to pass in O(nlogn)
 time, but try to write the solution in linear time, which we discussed in the lecture.

You are given two arrays, sorted in non-decreasing order. Merge them into one sorted array.

Input
The first line contains integers n
 and m
, the sizes of the arrays (1≤n,m≤105
). The second line contains n
 integers ai
, elements of the first array, the third line contains m
 integers bi
, elements of the second array (−109≤ai,bi≤109
).

Output
Print n+m
 integers, the merged array.

Example
inputCopy
6 7
1 6 9 13 18 18
2 3 8 13 15 21 25
outputCopy
1 2 3 6 8 9 13 13 15 18 18 21 25 