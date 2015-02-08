/*
 * HackerRank - Algorithms - Warmup
 * Lonely Integer
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <sstream>
#include <limits>

using namespace std;

int lonelyinteger(vector < int > a) {
    sort(a.begin(),a.end());

    for(vector<int>::iterator it=a.begin();it<=a.end();it+=2)
    {
        if(it == a.end() || *it != *(it+1))
            return *it;
    }
return 0;

}
int main() {
    int res;

    int _a_size;
    cin >> _a_size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
    vector<int> _a;
    int _a_item;
    for(int _a_i=0; _a_i<_a_size; _a_i++) {
        cin >> _a_item;
        _a.push_back(_a_item);
    }

    res = lonelyinteger(_a);
    cout << res;

    return 0;
}
