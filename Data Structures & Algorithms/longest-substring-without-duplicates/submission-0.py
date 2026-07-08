class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        for i in range(len(s)):
            sub={}
            for j in range(i,len(s)):
                if s[j] in sub:
                    break
                sub[s[j]]=1
                max_len=max(max_len,j-i+1)
        return max_len