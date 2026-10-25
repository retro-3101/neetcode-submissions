class Solution {
private:
    vector<string> result;

public:
    void generator(int curr_opens, int used, string temp, int n){
        
        if(temp.size() == n*2){
            result.push_back(temp);
            return;
        }

        if(used < n){
            generator(curr_opens+1, used+1, temp + "(", n);
        }

        if(curr_opens > 0){
            generator(curr_opens-1, used, temp + ")", n);
        }

        return;
    }

    vector<string> generateParenthesis(int n) {
        
        int curr_opens = 1, used = 1;

        string temp = "(";

        generator(curr_opens, used, temp, n);

        return result;
    }
};
