class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        while (pq.size() > 1) {
            int y = pq.top();
            pq.pop();
            int x = pq.top();
            pq.pop();
            if (x == y) {
                continue;
            } else if (x < y) {
                pq.push(y - x);
            }
        }
        if (pq.size() == 1) {
            return pq.top();
        }
        return 0;
    }
};
