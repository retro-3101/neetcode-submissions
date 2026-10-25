class Solution {
public:
    bool isValid(string s) {
        
        stack<char> brackets;

        for(int i=0; i<s.size(); i++){
            char temp = s[i];

            if(temp == '(' or temp == '{' or temp == '['){
                brackets.push(temp);
            }

            else{
                if(brackets.size() == 0)return false;

                char open_bracket = brackets.top();
                brackets.pop();

                if(open_bracket == '[')open_bracket = ']';
                else if(open_bracket == '{')open_bracket = '}';
                else open_bracket = ')';

                if(open_bracket == temp)continue;
                else return false;
            }
        }

        if(brackets.size())return false;

        return true;
    }
};
