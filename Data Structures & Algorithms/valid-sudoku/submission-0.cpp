class Solution {
public:

    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<vector<int>>> checker(3, vector<vector<int>>(9, vector<int>(9, 0)));

        for(int i=0;i<board.size();i++){
            
            for(int j=0;j<board[0].size();j++){

                if(board[i][j] == '.')continue;

                int num = board[i][j] - '0';

                if(checker[0][i][num-1] + checker[1][j][num-1] + checker[2][(i/3)*3 + j/3][num-1] != 0)return false;

                checker[0][i][num-1]++;
                checker[1][j][num-1]++;
                checker[2][i/3 + j/3][num-1]++;
            }
        }

        return true;
    }
};
