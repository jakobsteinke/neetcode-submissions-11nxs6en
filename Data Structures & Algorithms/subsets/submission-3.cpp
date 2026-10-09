class Solution {
public:
    void dfs(vector<int>& nums, vector<vector<int>>& result, int index, vector<int>& cur) {
        if (index == nums.size()) {
            result.push_back(cur);
            return;
        }
        cur.push_back(nums[index]);
        index++;
        dfs(nums, result, index, cur);
        cur.pop_back();
        dfs(nums, result, index, cur);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> cur;
        dfs(nums, result, 0, cur);
        return result;
    }
};
