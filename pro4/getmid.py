class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = []
        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        while(len(a) != l1+l2):
            if i == l1 and j !=l2:
                a.append(nums2[j])
                j = j+1
            elif i != l1 and j ==l2:
                a.append(nums1[i])
                i = i+1
            else:
                if nums1[i] <= nums2[j]:
                    a.append(nums1[i])
                    i= i+1
                else:
                    a.append(nums2[j])
                    j = j+1
        r = len(a)//2
        if (l1+l2)%2 ==0:
            return (a[r]+a[r-1])/2
        else:
            return a[r]