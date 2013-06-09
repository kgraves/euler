#include <iostream>
#include <cmath>
using namespace std;

bool p(const int &n) {
    if (n < 2)  return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    int max = sqrt(n)+1;
    for (int i=3; i<max; ++i)
       if (n % i == 0) return false;

    return true;
}

int main() {
    int c=1, i;

    for (i=3; c<10001;i+=2)
        if (p(i))
            ++c;

    cout << i << endl;
    return 0;
}

