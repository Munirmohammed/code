public class Solution {
    public int MinPatches(int[] nums, int n) {
        long miss = 1;  // The smallest sum we haven't achieved yet
        int patches = 0, i = 0;

        while (miss <= n)
        {
            if (i < nums.Length && nums[i] <= miss)
            {
                // If the current num can extend our reach, use it
                miss += nums[i++]; 
            }
            else
            {
                // Otherwise, patch with the 'miss' value
                miss += miss;
                patches++;
            }
        }

        return patches;
    }
}