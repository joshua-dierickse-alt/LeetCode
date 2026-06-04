int waviness(int num) {
    int c = 0;
    int num1 = num % 10;
    int num2 = num % 10;
    int num3 = num % 10;

    int og = num;

    while (num > 0) {
        num1 = num2;
        num2 = num3;
        num3 = num % 10;
        num /= 10;

        if ((num1 < num2 && num2 > num3) || (num1 > num2 && num2 < num3))
            ++c;
    }

    return c;
}

class Solution {
public:
    int totalWaviness(int num1, int num2) {
        int c = 0;

        for (int i = num1; i <= num2; ++i)
            c += waviness(i);

        return c;
    }
};