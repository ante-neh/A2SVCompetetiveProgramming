A. Segment with Small Sum1 second1024 megabytesstandard inputstandard output
Given an array of n
 integers ai
. Let's say that the segment of this array a[l..r]
 (1≤l≤r≤n
) is good if the sum of elements on this segment is at most s
. Your task is to find the longest good segment.

Input
The first line contains integers n
 and s
 (1≤n≤105
, 1≤s≤1018
). The second line contains integers ai
 (1≤ai≤109
).

Output
Print one integer, the length of the longest good segment. If there are no such segments, print 0
.

Example
inputCopy
7 20
2 6 4 3 6 8 9
outputCopy
4