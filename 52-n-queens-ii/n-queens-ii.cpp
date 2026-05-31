int acc;
int N;

void recursion(vector<bool> &board, int row) {
    if (row >= N) {
        acc += 1;
        return;
    }

    vector<uint8_t> revert;
    uint8_t temp;

    for (size_t i = 0; i < N; ++i) {
        if (!board[row * N + i]) {
            for (uint8_t h = row + 1, d = 1; h < N; ++h, ++d) {
                temp = h * N + i;
                if (!board[temp]) revert.push_back(temp);
                board[temp] = true;

                if (i >= d) {
                    temp = h * N + i - d;
                    if (!board[temp]) revert.push_back(temp);
                    board[temp] = true;
                }

                if (i + d < N) {
                    temp = h * N + i + d;
                    if (!board[temp]) revert.push_back(temp);
                    board[temp] = true;
                }
            }

            recursion(board, row + 1);

            for (int old : revert) board[old] = false;

            revert.clear();
        }
    }
}

class Solution {
public:
    int totalNQueens(int n) {
        acc = 0;
        N = n;

        vector<bool> board(N * N, false);

        recursion(board, 0);

        return acc;
    }
};