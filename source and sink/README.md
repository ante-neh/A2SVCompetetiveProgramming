The vertex of directed graph is called a source if no edge comes into it, and a sink if no edge comes out of it.

The directed graph is given with adjacency matrix. Find all its sources and sinks.

Input data
The first line contains the number of vertices in a graph n (1 ≤ n ≤ 100), then the adjacent matrix is given - n lines with n numbers, each of them equals to 0 or 1.

Output data
Print in the first line the number of sources in a graph, and then sources in increasing order. Print in the second line the information about sinks in the same format.


Examples
Input example #1 content_copy
5
0 0 0 0 0
0 0 0 0 1
1 1 0 0 0
0 0 0 0 0
0 0 0 0 0
Output example #1 content_copy
2 3 4
3 1 4 5