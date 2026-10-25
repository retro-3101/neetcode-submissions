class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        map<vector<int>, vector<string>> anagrams;

        for(const string& str: strs){
            vector<int> freq(26, 0);

            for(const char& c: str){
                freq[c - 'a']++;
            }
            anagrams[freq].push_back(str);
        }

        vector<vector<string>> result;

        for(const auto& strings: anagrams){
            result.push_back(strings.second);
        }

        return result;
    }
};
