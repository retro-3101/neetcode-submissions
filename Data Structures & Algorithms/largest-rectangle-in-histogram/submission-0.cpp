class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> stack;
        int maxArea = heights[0];
        int n = heights.size();

        for(int i=0; i<=n; i++){

            while(!stack.empty() and (i == n or heights[stack.top()] >= heights[i])){
                int height = heights[stack.top()];
                stack.pop();

                int width = stack.empty() ? i : i - stack.top() - 1;
                maxArea = max(maxArea, height * width);
            }
            stack.push(i);
        }

        return maxArea;
    }
};
