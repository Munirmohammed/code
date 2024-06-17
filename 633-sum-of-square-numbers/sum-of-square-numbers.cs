using System;

public class Solution
{
    public bool JudgeSquareSum(int c)
    {
        // Two-pointer approach for efficient checking
        long left = 0; 
        long right = (long)Math.Sqrt(c); // Cast to long to handle potential overflow

        while (left <= right)
        {
            long sum = left * left + right * right;

            if (sum == c)
            {
                return true; // Found a valid pair of squares
            }
            else if (sum < c)
            {
                left++;  // Need a larger left square
            }
            else
            {
                right--; // Need a smaller right square
            }
        }

        return false; // No pair of squares found
    }
}
