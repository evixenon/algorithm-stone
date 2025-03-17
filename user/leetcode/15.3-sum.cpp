// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include "commoncppproblem15.h"

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(),nums.end());
        int n = nums.size();
        for (int i=0; i<n-2; i++) {
            if (i>0 && nums[i]==nums[i-1]) continue;
            int j = i+1, k = n-1;
            while(j<k) {
                int s = nums[i] + nums[j] + nums[k];
                if (s < 0) {
                    j++;
                }
                else if (s > 0){
                    k--;
                }
                else {
                    ans.push_back({nums[i], nums[j], nums[k]});
                    // 跳过相同的值
                    for (j++; j<k && nums[j]==nums[j-1]; j++);
                    for (k--; j<k && nums[k]==nums[k+1]; k--);
                }
            }
        }
        return ans;
    }
};
// @lc code=end

