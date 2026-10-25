class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<float> time;
        int n = speed.size();
        vector<pair<int, int>> pos_time;

        for(int i=0; i<n; i++){
            pos_time.push_back({position[i], speed[i]});
        }
        sort(pos_time.begin(), pos_time.end());

        for(int i=0; i<n; i++){
            time.push_back((float)(target-pos_time[i].first)/pos_time[i].second);
        }

        int fleets = 0;
        float max_time = 0;

        for(int i=n-1; i>=0; i--){
            if(time[i] > max_time)fleets++;

            max_time = max(time[i], max_time);
        }

        return fleets;

    }
};
