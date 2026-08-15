class Solution {
    public int longestConsecutive(int[] nums) {

        int longestLength = 0;

        // Store every number and mark it as unexplored
        Map<Integer, Boolean> checkedMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            checkedMap.put(nums[i], false);
        }

        // Process every number
        for (int i = 0; i < nums.length; i++) {

            // Current number itself is part of the sequence
            int currentLength = 1;

            // Mark current number as explored
            checkedMap.put(nums[i], true);

            // Check consecutive numbers in forward direction
            int nextNum = nums[i] + 1;

            while (checkedMap.containsKey(nextNum)
                    && checkedMap.get(nextNum) == false) {

                currentLength++;

                // Mark this number as explored
                checkedMap.put(nextNum, true);

                // Move to the next number
                nextNum++;
            }

            // Check consecutive numbers in backward direction
            int prevNum = nums[i] - 1;

            while (checkedMap.containsKey(prevNum)
                    && checkedMap.get(prevNum) == false) {

                currentLength++;

                // Mark this number as explored
                checkedMap.put(prevNum, true);

                // Move to the previous number
                prevNum--;
            }

            // Update the longest sequence found so far
            longestLength = Math.max(longestLength, currentLength);
        }

        return longestLength;
    }
}
