class Solution {
    int xCenter_;
    int yCenter_;
    int radius_squared_;

    bool within_distance(int x, int y) {
        return pow(x - xCenter_, 2) + pow(y - yCenter_, 2) <= radius_squared_;
    }

public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        if (x1 <= xCenter && xCenter <= x2) {
            return (y1 <= yCenter && yCenter <= y2) || abs(y1 - yCenter) <= radius || abs(y2 - yCenter) <= radius;
        }
        if (y1 <= yCenter && yCenter <= y2) {
            return (x1 <= xCenter && xCenter <= x2) || abs(x1 - xCenter) <= radius || abs(x2 - xCenter) <= radius;
        }

        xCenter_ = xCenter;
        yCenter_ = yCenter;

        radius_squared_ = pow(radius, 2);

        return within_distance(x1, y1) || within_distance(x1, y2) || within_distance(x2, y1) || within_distance(x2, y2);
    }
};