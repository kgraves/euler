#include <iostream>
#include <cmath>
using namespace std;

const int MAX = 1000;

int find_triple();

int main() {
    cout << find_triple() << endl;
    return 0;
}

int find_triple() {
    for (int b=1; b<=1000; ++b) {
        double res = (500000 - 1000 * b) / (1000 - b);

        // check for fractional part
        if (res == floor(res)) {
            // solution found, solve for c
            int a = (int)res;
            int c = 1000 - a - b;

            int ab = pow(a,2) + pow(b,2);

            if (a < b && b < c && ab == pow(c,2)) {
                cout << a << " " << b << " "  << c << endl;
                return a * b * c;
            }
        }
    }
}
