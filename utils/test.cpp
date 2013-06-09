#include <iostream>
using namespace std;

int main() {
    const int res = 232792560;
    

    for (int i=2; i<=10; ++i) {
        cout << res << "/" << i << " = " << res/i << endl;
        //if ((i % j) != 0) {
            //break;
        //}
    }

    return 0;
}

