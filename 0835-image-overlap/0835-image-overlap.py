class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def solve(img1,img2):
            n=len(img1)
            ans=0
            l1=[]
            l2=[]
            for i in range(n):
                for j in range(n):
                    if img1[i][j]:
                        l1.append((i,j))
                    if img2[i][j]:
                        l2.append((i,j))
            m={}
            for y in l1:
                for x in l2:
                    a=y[0]-x[0]
                    b=y[1]-x[1]
                    if (a,b) not in m:
                        m[(a,b)]=0
                    m[(a,b)]+=1
                    ans=max(ans,m[(a,b)])
                    
            return ans
        return solve(img1,img2)
        