class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = list(itertools.permutations(nums))
        new_list = list(set(perm))
        print(new_list)
        return new_list