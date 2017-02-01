#include <iostream>
#include <stack>
using namespace std;

bool ispal(int n) {
    stack<int> s;
    int o_n = n;
    int t = 0;

    do {
        t *= 10;
        t += n % 10;
        n /= 10;
    } while (n);

    if (o_n == t)
        return true;
    else
        return false;
}

int main() {
    int sol = 0, t = 0;

    for (int i=999; i>=100; --i) {
        for (int j=999; j>=100; --j) {
            t = i * j;
            if (ispal(t) && t > sol)
                sol = t;
        }
    }

    if (sol)
        cout << sol << endl;
    else
        cout << "none found" << endl;

    return 0;
}

