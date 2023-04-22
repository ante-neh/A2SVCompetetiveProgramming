class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort(i,j):
            nonlocal ans
            m=(i+j)//2
            a=i
            b=m+1
            z=[]
            while a<=m and b<=j:
                if nums[a]<=2*nums[b]:
                    ans+=b-m-1
                    a+=1
                else:
                    b+=1
            while a<=m:
                ans+=j-m
                a+=1
            nums[i:j+1]=sorted(nums[i:j+1])
        def merge(i,j):
            if i>=j:return
            m=(i+j)//2
            merge(i,m)
            merge(m+1,j)
            sort(i,j)
        ans=0
        merge(0,len(nums)-1)
        return ans