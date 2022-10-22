class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(ht):
            for k in ht.keys():
                if ht[k]>0:
                    return False
            return True
                
        
        ht1={}
        for  e in t:
            if e not in ht1:
                ht1[e]=0
            ht1[e]+=1
            
        st=0
        ans_len=10**20
        ans=""
        win_string=""
        for ed in range(len(s)):
            ch=s[ed]
            win_string+=ch
            if ch in ht1:
                ht1[ch]-=1
            while(check(ht1)):
                l=ed-st+1
                ch2=s[st]
                if l<ans_len:
                    ans_len=l
                    ans=win_string
                if ch2 in ht1:
                    ht1[ch2]+=1
                win_string=win_string[1:len(win_string)]
                st+=1
                
        return ans
                
                
            
                
                
        