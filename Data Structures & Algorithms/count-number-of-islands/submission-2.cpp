class Solution {
public:
    void bfs(int i, int j, unordered_set<string>& seen, vector<vector<char>>& grid) {
        queue<pair<int, int>> q;
        q.push({i, j});
        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            int cy = cur.first;
            int cx = cur.second;
            vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
            for (auto& [sy, sx] : dirs) {
                int ny = cy + sy;
                int nx = cx + sx;
                if (
                    ny >= 0 && ny < grid.size() && nx >= 0 && nx < grid[0].size() &&
                    grid[ny][nx] == '1' and !seen.contains(to_string(ny) + '-' + to_string(nx))
                ) {
                    seen.insert(to_string(ny) + '-' + to_string(nx));
                    q.push({ny, nx});
                }
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        unordered_set<string> seen;
        int num_islands = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j ++) {
                if (grid[i][j] == '1' and !seen.contains(to_string(i) + '-' + to_string(j))) {
                    num_islands += 1;
                    seen.insert(to_string(i) + '-' + to_string(j));
                    bfs(i, j, seen, grid);
                }
            }
        }
        return num_islands;
    }
};
