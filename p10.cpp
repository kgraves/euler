#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
using namespace std;

const int MAX = 2000000;
// const int MAX = 50;

// finds all primes under max and sums them
long long sieve(bool *arr, int max) {
    long long sum = 0;

    // int upper = sqrt(max) + 1;
    for (int i=0; i<max; ++i) {
        // if current value is true, then it's a prime
        if (arr[i]) {
            sum += i;

            // mark all multiples of current as non-prime
            for (int j=i<<1; j<max; j+=i) {
                arr[j] = false;
            }
        }
    }

    return sum;
}

int main() {
    bool *arr = new bool[MAX];
    memset(arr, 1, MAX);

    // set 0 and 1 to false
    arr[0] = false;
    arr[1] = false;

    long long sieve_sum = sieve(arr, MAX);

    cout << "sieve_sum: " << sieve_sum << endl;

    return 0;
}

