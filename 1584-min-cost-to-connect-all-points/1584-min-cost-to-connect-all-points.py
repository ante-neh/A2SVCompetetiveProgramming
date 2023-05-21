class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distance_pair=[]
        parent={}
        k=len(points)-1
        res=0
        for i in range(len(points)):
            for j in range(1,len(points)):
                displacement=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(distance_pair,[displacement,tuple(points[i]),tuple(points[j])])
        for point in points:parent[tuple(point)]=tuple(point)# set every point's parent to be itself at first
        def find(x):
            if parent[x]==x:return x
            return find(parent[x])
        def union(x,y):
            root_x,root_y=find(x),find(y)
            parent[root_x]=root_y
        while k>0:
            current_dis,point1,point2=heapq.heappop(distance_pair)
            if find(point1)!=find(point2):
                union(point1,point2)
                res+=current_dis
                k-=1
        return res