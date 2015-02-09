/*
 * HackerRank - Algorithms - Warmup
 * Maximizing XOR
 *
 * Abhinav Kumar
 * abhinavk.me
 */

#include <iostream>

using namespace std;

int main()
{
    int l,r;
    cin>>l>>r;
    int maxxor = 0;
    for(int i=l;i<=r;i++)
        for(int j=i;j<=r;j++)
            if((i^j) > maxxor)
                maxxor = i^j;
    cout<<maxxor;
    return 0;
}
