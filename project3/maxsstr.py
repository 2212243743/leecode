class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        s = list(s)
        for i in range(0,len(s)):
            a = []
            a.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in a:
                    a.append(s[j])
                else:
                    break
            if len(a) > n:
                n = len(a)
        return n
s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))