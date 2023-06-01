class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                flag,val = 1,0
                if nums1[i]==nums2[j]:
                    val = nums2[j]
                    for k in range(j+1,len(nums2)):
                        if nums2[k] > val:
                            ans.append(nums2[k])
                            flag = 0
                            break
                    if flag == 1:
                        ans.append(-1)
        return ans