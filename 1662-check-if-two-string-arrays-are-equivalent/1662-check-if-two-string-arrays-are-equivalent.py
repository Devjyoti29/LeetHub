class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        for st in word1:
            s1+=st
        s2=""
        for st in word2:
            s2+=st
        return s1==s2
        