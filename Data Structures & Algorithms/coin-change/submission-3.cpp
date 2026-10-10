class Solution {
public:
    int dfs(vector<int>& coins, int amount, unordered_map<int, int>& minCoinsNeeded) {
        if (minCoinsNeeded.contains(amount)) {
            return minCoinsNeeded[amount];
        }
        int coinsNeeded = -1;
        for (int i = 0; i < coins.size(); i++) {
            if (amount - coins[i] >= 0) {
                int rec = dfs(coins, amount - coins[i], minCoinsNeeded);
                if (rec == -1) {
                    continue;
                }
                int arec = 1 + rec;
                if (coinsNeeded == -1) {
                    coinsNeeded = arec;
                } else {
                    coinsNeeded = min(arec, coinsNeeded);
                }
            }
        }
        minCoinsNeeded[amount] = coinsNeeded;
        return coinsNeeded;
    }
    int coinChange(vector<int>& coins, int amount) {
        unordered_map<int, int> minCoinsNeeded;
        minCoinsNeeded[0] = 0;
        for (int i = 0; i < coins.size(); i++) {
            minCoinsNeeded[coins[i]] = 1;
        }
        return dfs(coins, amount, minCoinsNeeded);
    }
};
