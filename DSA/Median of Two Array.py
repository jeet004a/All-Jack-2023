#Median of Two array in leetCode
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p=nums1+nums2
        n=len(p)
        p.sort()
        if n%2==0:
            men1=p[n//2]
            men2=p[n//2 - 1]
            x=(men1+men2)/2
        else:
            x=p[n//2]

        return x