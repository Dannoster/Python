





#include <iostream>
#include <algorithm>

using namespace std;

int ball_fall(int eggs, int floors) {
    // if we have only one egg
    // then we have to check all the floors below
    if (eggs == 1)
        return floors;

    // in case only 2 or less floors left
    // we also have to check all
    if (floors <= 2)
        return floors;

    int min_drops = -1;
    for (int floor = 1; floor < floors; ++floor) {
        int max_drop_below = ball_fall(eggs - 1, floor - 1);
        int max_drop_above = ball_fall(eggs, floors - floor);
        int max_k = max(max_drop_below, max_drop_above);

        if (min_drops == -1 || min_drops > max_k) {
            min_drops = max_k;
        }
    }

    return min_drops + 1;
}

int main() {
    const int balls = 2;
    int n;

    cin >> n;
    cout << ball_fall(balls, n - 1) << endl;

    return 0;
}