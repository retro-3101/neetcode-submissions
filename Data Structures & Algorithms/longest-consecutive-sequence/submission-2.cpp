class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        map<int, int> checker;
        int max_count = 0;
        sort(nums.begin(), nums.end());

        for(int i=0; i<nums.size(); i++){
            checker[nums[i]] = checker[nums[i]-1] + 1;
            max_count = max(max_count, checker[nums[i]]);
        }

        return max_count;
    }
};
