void debug(vector<vector<int>> &t) {
    for (auto &i : t)
        cout << i[0] << "," << i[1] << " ";
    cout << "\n";
}

template <typename Op>
bool abstract_truncation(vector<vector<int>> &t, int x, int y) {
    int i = t.size();
    return Op()(
        (y - t[i-2][1]) * (t[i-1][0] - t[i-2][0]),
        (t[i-1][1] - t[i-2][1]) * (x - t[i-2][0])
    );
}

bool top_truncation(vector<vector<int>> &t, int x, int y) {
    // cout << "TOP: " << abstract_truncation<greater<int>>(t, x, y) << "\n";
    return abstract_truncation<greater<int>>(t, x, y);
}

bool bottom_truncation(vector<vector<int>> &t, int x, int y) {
    // cout << "BOTTOM: " << abstract_truncation<less<int>>(t, x, y) << " - (" << x << ", " << y << ")\n";
    return abstract_truncation<less<int>>(t, x, y);
}

template <int skip>
vector<vector<int>>& append_vectors(vector<vector<int>> &a, vector<vector<int>> &b) {
    vector<vector<int>> &v1 = (a.size() > b.size()) ? a : b;
    vector<vector<int>> &v2 = (a.size() > b.size()) ? b : a;

    v1.reserve(v1.size() + v2.size());
    v1.insert(v1.end(), v2.begin() + skip, v2.end());

    return v1;
}

class Solution {
    double m;
    double b;

    double f(double x) {
        return m * x + b;
    }
public:
    vector<vector<int>> outerTrees(vector<vector<int>> &trees) {
        sort(
            trees.begin(),
            trees.end(),
            [](vector<int> &a, vector<int> &b) -> bool { if (a[0] == b[0]) return a[1] < b[1]; return a[0] < b[0]; }
        );

        double x_s = trees.front()[0];
        double y_s = trees.front()[1];
        double x_e = trees.back()[0];
        double y_e = trees.back()[1];

        if (x_s == x_e) return trees;

        m = (y_e - y_s) / (x_e - x_s);
        b = y_s - x_s * m;

        vector<vector<int>> top = {trees.front()};
        vector<vector<int>> bottom = {trees.front()};
        vector<vector<int>> middle;

        cout << x_s << " " << y_s << "\n"; 
        cout << x_e << " " << y_e << "\n"; 

        for (int i = 1; i < trees.size() - 1; ++i) {
            int x = trees[i].front();
            int y = trees[i].back();

            double y_line = f(x);

            // cout << x << " " << y << " - " << y_line << "\n";

            if (y > y_line) {
                // cout << "ABOVE: " << x << " " << y << "\n";
                while (top.size() >= 2 && top_truncation(top, x, y)) top.pop_back();
                top.push_back(trees[i]);
            } else if (y < y_line) {
                // debug(bottom);
                while (bottom.size() >= 2 && bottom_truncation(bottom, x, y)) bottom.pop_back();
                bottom.push_back(trees[i]);
            } else if (top.size() == 1 || bottom.size() == 1) middle.push_back(trees[i]);
        }

        // debug(top);
        // debug(bottom);
        // debug(middle);

        while (top.size() >= 2 && top_truncation(top, x_e, y_e)) top.pop_back();
        while (bottom.size() >= 2 && bottom_truncation(bottom, x_e, y_e)) bottom.pop_back();

        if (top.size() == 1 || bottom.size() == 1) {
            if (top.size() == 1 && bottom.size() == 1) return trees;
            vector<vector<int>> &f = append_vectors<0>((top.size() == 1) ? bottom : top, middle);
            f.push_back(trees.back());
            return f;
        }

        vector<vector<int>> &f = append_vectors<1>(bottom, top);
        f.push_back(trees.back());
        return f;
    }
};