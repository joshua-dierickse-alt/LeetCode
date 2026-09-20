class SummaryRanges {
    set<pair<int, int>> ranges;

public:
    SummaryRanges() {}
    
    void addNum(int value) {
        if (ranges.size() == 0) {
            ranges.insert({value, value});
            return;
        }

        auto it_r = ranges.upper_bound({value, INT_MAX});

        if (it_r == ranges.begin()) {
            if (it_r->first - 1 == value) {
                ranges.insert({value, it_r->second});
                ranges.erase(it_r);
            } else {
                ranges.insert({value, value});
            }
            return;
        }

        auto it_l = it_r;
        --it_l;

        if (value <= it_l->second) return;

        if (it_l->second + 1 == value && value == it_r->first - 1) {
            ranges.insert({it_l->first, it_r->second});
            ranges.erase(it_r);
            ranges.erase(it_l);
        } else if (it_l->second + 1 == value) {
            ranges.insert({it_l->first, value});
            ranges.erase(it_l);
        } else if (value == it_r->first - 1) {
            ranges.insert({value, it_r->second});
            ranges.erase(it_r);
        } else {
            ranges.insert({value, value});
        }
    }
    
    vector<vector<int>> getIntervals() {
        vector<vector<int>> result;

        for (const pair<int, int> &range: ranges) {
            result.push_back({range.first, range.second});
        }

        return result;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(value);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */