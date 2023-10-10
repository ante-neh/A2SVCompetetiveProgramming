class Solution:
    def __init__(self):
        self.path=[]
        self.dp=[]
        for i in range(51):
            self.dp+=[[-1]*2]
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj=[]
        c1=[]
        for i in range(n):
            adj+=[[]]
            c1+=[[0]*n]
        for i in edges:
            adj[i[0]]+=[i[1]]
            adj[i[1]]+=[i[0]]
            c1[i[0]][i[1]]+=1
            c1[i[1]][i[0]]+=1
        c=[0]*n
        h={}
        for i in trips:
            v=[-1]*n
            self.solve(trips,adj,i[0],i[1],[i[0]],v)
            for i in self.path:
                c[i]+=1
            self.path=[]
        v=[-1]*n
        for i in range(n):
            c[i]*=price[i]
        l2=[]
        for i in range(n):
            l1=[]
            for j in range(n):
                if c1[i][j]==0:
                    l1+=[j]
            l2+=[l1]
        print(c)
        totpri=sum(c)
        a=self.maximum(adj,c,v,0,0)
        return totpri-a
    def maximum(self,adj,c,v,i,cur):
        v[cur]=1
        if self.dp[cur][i]!=-1:
            return self.dp[cur][i]
        if i==0:
            s=c[cur]//2
            for j in adj[cur]:
                if v[j]==-1:
                    s+=self.maximum(adj,c,v,1,j)
                    v[j]=-1
            s1=0
            for j in adj[cur]:
                if v[j]==-1:
                    s1+=self.maximum(adj,c,v,0,j)
                    v[j]=-1
            s=max(s,s1)
            self.dp[cur][i]=s
            return s
        else:
            s1=0
            for j in adj[cur]:
                if v[j]==-1:
                    s1+=self.maximum(adj,c,v,0,j)
                    v[j]=-1
            self.dp[cur][i]=s1
            return s1
    def solve(self,l,adj,i1,i2,l1,v):
        v[i1]=1
        if i1==i2:
            self.path=l1
        for i in adj[i1]:
            if v[i]==-1:
                self.solve(l,adj,i,i2,l1+[i],v)