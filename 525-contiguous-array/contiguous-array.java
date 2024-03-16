class Solution {
    public int findMaxLength(int[] nums) {
        Map map = new HashMap<>();
        int maxLength = 0, sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i] == 0 ? -1 : 1;
            if (sum == 0) {
                maxLength = Math.max(maxLength, i + 1);
            } else if (map.containsKey(sum)) {
                maxLength = Math.max(maxLength, i - (int) map.get(sum));
            } else {
                map.put(sum, i);
            }
        }
        return maxLength;
    }
}