class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> seen_map;
        int l = 0, r = 0;
        int max_len = 0;
        while (r < s.size()) {
            if (seen_map.contains(s[r])) {
                l = max(l, seen_map[s[r]] + 1);
            }
            seen_map[s[r]] = r;
            max_len = max(max_len, r - l + 1);
            r++;
        }
        return max_len;
    }
};
