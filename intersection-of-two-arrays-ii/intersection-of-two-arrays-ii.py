class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in nums1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        list1=[]
        for i in nums2:
            if i in d and d[i]>0:
                list1.append(i)
                d[i]-=1
        return list1