class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;

        for(auto num: nums){
            count[num]++;
        }

        vector<vector<int>> freq(nums.size()+1);

        for(auto key: count){
            freq[key.second].push_back(key.first);
        }

        vector<int> result;

        for(int i=freq.size()-1;i>0;i--){

            for(auto num: freq[i]){
                if(result.size() >= k)break;
                result.push_back(num);
            }
        }

        return result;
    }
};
