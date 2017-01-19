#include <iostream>
using namespace std;

int main(){
    long c, r;
    cin >> r >> c;
    cout << ((r-1)/2)*10 + (c-1)*2 + (r-1)%2 << endl;
}    
