#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> window(nums.begin(), nums.begin() + k);
        auto mid = next(window.begin(), k / 2);
        vector<double> medians;

        for (int i = k; ; ++i) {
            // Determine and store the current median
            if (k % 2 == 0) {
                // Cast to double before addition to prevent integer overflow
                medians.push_back(((double)*mid + (double)*prev(mid)) / 2.0);
            } else {
                medians.push_back(*mid);
            }

            if (i == nums.size()) break;

            // Insert the incoming element
            window.insert(nums[i]);
            // If the incoming element is smaller than the median, it pushes the median left
            if (nums[i] < *mid) {
                mid--;
            }

            // Deal with the outgoing element
            // If the outgoing element was on or to the left of the median, shift median right
            if (nums[i - k] <= *mid) {
                mid++;
            }
            // Safely erase the outgoing element
            window.erase(window.lower_bound(nums[i - k]));
        }

        return medians;
    }
};