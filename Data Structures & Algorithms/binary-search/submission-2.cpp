class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int l=0, r=n-1;

        while(r-l > 1){

            int m = (l+r)/2;

            if(target == nums[m]){
                return m;
            }

            else if(target > nums[m]){
                l = m;
            }

            else {
                r = m;
            }
        }
        if(nums[l] == target)return l;
        else if(nums[r] == target)return r;
        
        return -1;
    }
};
