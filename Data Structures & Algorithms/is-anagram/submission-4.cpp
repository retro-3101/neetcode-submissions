class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> freq(26, 0);

        for(auto chr: s){
            freq[chr - 'a']++;
        }
        for(auto chr: t){
            freq[chr - 'a']--;
        }

        for(auto num: freq){
            if(num != 0)return false;
        }

        return true;
    }
};
