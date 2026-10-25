class Solution {
public:
    int characterReplacement(string s, int k) {
        
        unordered_map<char, int> count;
        map<int, unordered_set<char>> inv_count;
        int max_len = 1;

        int i=0;
        count[s[0]]++;
        inv_count[count[s[0]]].insert(s[0]);

        for(int j=1; j<s.size(); j++){

            count[s[j]]++;
            inv_count[count[s[j]]].insert(s[j]);

            int freq = inv_count.rbegin()->first;
            
            while((j-i+1-freq) > k){
                count[s[i]]--;
                inv_count[count[s[i]]+1].erase(s[i]);

                if(inv_count[count[s[i]]+1].empty()){
                    inv_count.erase(count[s[i]]+1);
                }

                inv_count[count[s[i]]].insert(s[i]);

                freq = inv_count.rbegin()->first;
                i++;
            }

            max_len = max(j-i+1, max_len);
        }

        return max_len;
    }
};
