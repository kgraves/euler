#include <iostream>
#include <cmath>
using namespace std;

int gcpf(int n) {
    int g=0, p=0;

    for (int i=2; n!=1;) {
        if (n%i == 0) {
            if (g == i) {
                ++p;
                n /= i;
            }
            else {
                p = 1;
                g = i;
                n /= i;
            }
        }
        else
            ++i;
    }

    return pow(g, p);
}

int main() {
    int s = 1;
    int t = 0;

    for (int i=2; i<=20; ++i) {
        t = gcpf(i);
        cout << t << endl;
        s *= t;
        //s *= gcpf(i);
    }

    cout << s << endl;

    /*
    bool s;

    for (long i=20; i<9999999999; i+=2) {
        s = true;

        for (long j=20; j>=20; --j) {
            if ((i % j) != 0) {
                s = false;
                break;
            }
        }

        if (s) {
            cout << i << endl;
            return 0;
        }
    }

    cout << "not found" << endl;
    */

    return 0;
}

