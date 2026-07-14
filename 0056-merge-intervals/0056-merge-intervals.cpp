class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {

        vector<vector<int>> result;

        // Sort intervals based on start value
        sort(intervals.begin(), intervals.end());

        // Take first interval
        int start = intervals[0][0];
        int end = intervals[0][1];


        for(int i = 1; i < intervals.size(); i++) {

            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];


            // If intervals overlap
            if(currentStart <= end) {

                // Merge intervals
                end = max(end, currentEnd);

            } 
            else {

                // Store previous interval
                result.push_back({start, end});

                // Update current interval
                start = currentStart;
                end = currentEnd;
            }
        }


        // Add the last interval
        result.push_back({start, end});


        return result;
    }
};