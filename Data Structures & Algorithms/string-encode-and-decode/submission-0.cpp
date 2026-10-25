class Solution {
public:

    string encode(vector<string>& strs) {
        string result;

        for(auto str: strs){
            result = result + to_string(str.size()) + "#" + str;
        }

        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;

        int i = 0;
        int j = i+1;

        while(i < s.size()){

            while(s[j] != '#')j++;

            int len = stoi(s.substr(i,j-i));

            result.push_back(s.substr(j+1,len));

            i = j + len + 1;
            j = i + 1;
        }

        return result;
    }
};
