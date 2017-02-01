#include <iostream>
#include <cmath>
using namespace std;

long long sumsq(const long long &max) {
    long long res=1;
    for (long long i=2; i<=max; ++i) {
        res += pow(i, 2);
    }

    return res;
}

long long sqsum(const long long &max) {
    long long res=1;
    for (long long i=2; i<=max; ++i) {
        res += i;
    }

    return pow(res, 2);
}

int main() {
    //long long a=0, b=0;
    const long long max = 100;

    int a = sqsum(max);
    int b = sumsq(max);

    cout << a-b << endl;

    //cout << sqsum(max) - sumsq(max) << endl;

    return 0;
}

