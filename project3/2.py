class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max = 0
        a = []
        n = len(s)
        for i in range(n):
            while s[i] in a:
                del a[0]
            a.append(s[i])
            max = len(a) if len(a)>max else max
        return max
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))


