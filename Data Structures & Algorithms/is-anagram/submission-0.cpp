class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> count;

        for(int i=0;i<s.size();i++){
            count[s[i]]++;
        }

        for(int i=0;i<t.size();i++){
            count[t[i]]--;
        }

        for(auto pair: count){
            if(pair.second != 0)return false;
        }

        return true;
    }
};
