public class Solution {
    public int MinPatches(int[] nums, int n) {
        long miss = 1;  // Track the smallest missing sum
        int patches = 0, i = 0; // Count of patches and index in nums

        while (miss <= n) 
        {
            if (i < nums.Length && nums[i] <= miss)
            {
                // If the current num can be used to form sums, update miss
                miss += nums[i++];
            }
            else
            {
                // Need a patch to cover the missing sum
                miss += miss; 
                patches++;
            }
        }

        return patches;
    }
}