/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

// TODO(yan): TLE.

class Solution {
   public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        map<float, int> cars;
        for (int i = 0; i < position.size(); i++) {
            float p = float(position[i]);
            int s = speed[i];
            cars[p] = s;
        }

        for (;;) {
            auto it = cars.begin();
            float da = it->first;
            int sa = it->second;
            float db = 0;
            int sb = 0;

            vector<float> ps;
            vector<int> ss;
            float hit_time = -1;

            for (; it != cars.end(); ++it) {
                float db = it->first;
                int sb = it->second;
                if (sb < sa) {
                    float t = (db - da) / (sa - sb);
                    float meet = (sa * db - sb * da) / (sa - sb);
                    if ((meet <= target) && (hit_time < 0 || t < hit_time)) {
                        hit_time = t;
                        ps.clear();
                        ss.clear();
                        ps.push_back(da);
                        ps.push_back(db);
                        ss.push_back(sa);
                        ss.push_back(sb);
                    }
                }
                da = db;
                sa = sb;
            }

            if (hit_time < 0) break;

            da = ps[0];
            db = ps[1];
            sa = ss[0];
            sb = ss[1];
            cars.erase(da);
            cars.erase(db);
            float t = (db - da) / (sa - sb);
            float meet = (sa * db - sb * da) / (sa - sb) - (t * sb);
            it = cars.find(meet);
            if (it != cars.end()) {
                cars[meet] = min(it->second, sb);
            } else {
                cars[meet] = sb;
            }
            cout << "add (" << meet << ", " << sb << ")"
                 << " " << hit_time << endl;
            cout << "erase " << da << ", " << db << endl;
        }

        return cars.size();
    }
};

void test1() {
    Solution s;
    vector<int> position = {10, 8, 0, 5, 3};
    vector<int> speed = {2, 4, 1, 1, 3};
    int target = 12;
    int ans = s.carFleet(target, position, speed);
    cout << "ans = " << ans << endl;
}

void test2() {
    Solution s;
    vector<int> position = {6, 8};
    vector<int> speed = {3, 2};
    int target = 10;
    int ans = s.carFleet(target, position, speed);
    cout << "ans = " << ans << endl;
}

void test3() {
    Solution s;
    int target = 12;
    vector<int> position = {4, 0, 5, 3, 1, 2};
    vector<int> speed = {6, 10, 9, 6, 7, 2};
    int ans = s.carFleet(target, position, speed);
    cout << "ans = " << ans << endl;
}

int main() {
    test1();
    test2();
    test3();
}
