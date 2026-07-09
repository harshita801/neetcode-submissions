class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len=0
        st=set()
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            max_len=max(right-left+1,max_len)
        return max_len