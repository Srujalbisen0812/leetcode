public class Solution {

    public static int maxSubArray(int[] nums) {
        int maxSum = nums[0]; // initialize with the first element
        int currentSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            // decide whether to add to current sum or start fresh from current element
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum); // update maxSum if needed
        }

        return maxSum;
    }

    public static void main(String[] args) {
        // Example inputs
        int[] nums1 = {-2,1,-3,4,-1,2,1,-5,4};
        int[] nums2 = {1};
        int[] nums3 = {5,4,-1,7,8};

        System.out.println(maxSubArray(nums1)); // Output: 6
        System.out.println(maxSubArray(nums2)); // Output: 1
        System.out.println(maxSubArray(nums3)); // Output: 23
    }
}
