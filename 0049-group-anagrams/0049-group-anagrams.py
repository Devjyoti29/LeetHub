class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht={}
        for s in strs:
            sorted_s=str(sorted(s))
            if sorted_s not in ht:
                ht[sorted_s]=[]
            ht[sorted_s].append(s)
        ans=[]
        for k in ht.keys():
            ans.append(ht[k])
        return ans
        