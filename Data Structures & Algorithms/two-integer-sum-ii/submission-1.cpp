class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // two pointer

        int i=0, j = numbers.size()-1;

        while(j>i){
            int sum = numbers[i] + numbers[j];

            if(sum == target)return {i+1,j+1};

            else if(sum > target)j--;

            else i++;
        }

        return {-1,-1};
    }
};
