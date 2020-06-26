class Solution:
    def convert(self, s: str, numRows: int) -> str:
        re = ''
        arrays = [[] for i in range(numRows)]
        index = 0
        i = index-1
        j = 0
        if numRows == 1:
            return s
        while(j<len(s)):
            arrays[index].append(s[j])
            j = j+1
            if (index >i and index< numRows-1) or index == 0:
                i = index
                index = index+1
            elif (index < i and index>0) or index == numRows-1:
                i = index
                index = index-1
        for i in range(len(arrays)):
            for j in range(len(arrays[i])):
                re = re+arrays[i][j]
        return re
s = Solution()
print(s.convert("AB",2))