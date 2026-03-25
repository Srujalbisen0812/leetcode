import java.util.*;

class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        int n = heights.length;
        int[] res = new int[n];
        Stack<Integer> st = new Stack<>();

        for (int i = n - 1; i >= 0; i--) {
            int count = 0;

            while (!st.isEmpty() && heights[i] > st.peek()) {
                st.pop();
                count++;
            }

            if (!st.isEmpty()) {
                count++;
            }

            res[i] = count;
            st.push(heights[i]);
        }

        return res;
    }
}