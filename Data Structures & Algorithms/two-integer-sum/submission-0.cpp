class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> diff;

        diff[nums[0]] = 0;

        for(int i=1;i<nums.size(); i++){

            if(diff.find(target - nums[i]) != diff.end())return {diff[target-nums[i]], i};

            diff[nums[i]] = i;
        }

        return {0,0};
    }
};
