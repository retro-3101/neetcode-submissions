class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        vector<int> result(temperatures.size(), 0);
        stack<pair<int, int>> temps;

        for(int i=0; i<temperatures.size(); i++){

            while(!temps.empty() and temperatures[i] > temps.top().first){
                pair<int,int> temp = temps.top(); temps.pop();

                result[temp.second] = i - temp.second;
            }

            temps.push({temperatures[i], i});
        }

        return result;
    }
};
