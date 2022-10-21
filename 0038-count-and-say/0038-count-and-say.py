class Solution:
    def countAndSay(self, n: int) -> str:
        def solve(n):
            if(n==1):
                return "1"
            res=solve(n-1)
            c=1
            ans=""
            for i in range(1,len(res)):
                if(res[i]==res[i-1]):
                    c+=1
                else:
                    ans+=str(c)+res[i-1]
                    c=1
            ans+=str(c)+res[len(res)-1]
            return ans
        return solve(n)
                    
                
                
                
        
        
        