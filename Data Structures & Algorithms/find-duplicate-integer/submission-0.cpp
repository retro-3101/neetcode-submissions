class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        int n = nums.size();
        for(int i=0; i<n; i++){
            int num = nums[i]%n;

            if(nums[num-1]/n)return num;

            nums[num-1] = n + nums[num-1];
        }

        return -1;
    }
};
