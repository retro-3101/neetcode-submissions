class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        stack<int> nums;

        for(string token: tokens){
            
            if(token == "+" or token == "-" or token == "*" or token == "/"){
                int a = nums.top(); nums.pop();
                int b = nums.top(); nums.pop();

                if(token == "+")nums.push(b + a);
                else if(token == "-")nums.push(b - a);
                else if(token == "*")nums.push(b * a);
                else nums.push(b / a);
            }

            else{
                nums.push(stoi(token));
            }
        }

        return nums.top();
    }
};
