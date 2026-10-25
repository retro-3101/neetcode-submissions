class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> truth;
        unordered_map<char, int> slider;

        for(char s: s1){
            truth[s]++;
        }

        if(s1.size() > s2.size())return false;

        int i=0;
        for(; i<s1.size(); i++){
            slider[s2[i]]++;
        }

        for(int j=0;(j+i)<s2.size(); j++){

            if(slider == truth)return true;

            slider[s2[j]]--;
            if(slider[s2[j]] == 0)slider.erase(s2[j]);

            slider[s2[j+i]]++;
        }

        if(slider == truth)return true;

        return false;
    }
};
