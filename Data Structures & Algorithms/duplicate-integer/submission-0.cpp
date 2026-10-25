class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int,int> count;

        for(int i=0;i<nums.size();i++){
            if(count[nums[i]] > 0)return true;
            else count[nums[i]]++;
        }

        return false;
    }
};
