class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def canInclude(s,ans_set):
            prev=set()
            for ch in s:
                if ch in prev or ch in ans_set:
                    return False
                prev.add(ch)
            return True    
        ans=set()
        def solve(a,l):
            if l==len(a):
                return len(ans) # iterate karte karte exhasted the array
            
            if canInclude(a[l],ans):
                for ch in a[l]:
                    ans.add(ch)
                includingL=solve(a,l+1)
                for ch in a[l]:
                    if ch in ans:
                        ans.remove(ch)
                excludingL=solve(a,l+1)
                
                return max(includingL,excludingL)
            else:
                return solve(a,l+1)
            
        return solve(arr,0)
                
                
                
                
                           
        