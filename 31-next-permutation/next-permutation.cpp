class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;

        // find the first pair of adjacent elements that are in decreasing order
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        // if no such pair is found, reverse the whole array and return
        if (i < 0) {
            std::reverse(nums.begin(), nums.end());
            return;
        }

        // find the first element that is greater than the first element of the pair
        int j = n - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }

        // swap the first element of the pair with the found element
        std::swap(nums[i], nums[j]);

        // reverse the remaining part of the array
        std::reverse(nums.begin() + i + 1, nums.end());
    }
};