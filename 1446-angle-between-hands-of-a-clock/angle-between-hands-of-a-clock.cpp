class Solution {
public:
    double angleClock(int hour, int minutes) {
        double x = abs((hour + minutes / 60.0) / 12.0 - minutes / 60.0) * 360;
        return abs(x < 180 ? x : 360 - x);
    }
};