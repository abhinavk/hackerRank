/*
 * Hackerrank - Algorithms - Warmup
 * Manasa and Stones
 * Author: Abhinav Kumar
 * Email: abhinavkumar@outlook.com
 */

#include <iostream>

using namespace std;

int main()
{
    int testcases,n,a,b,maxx,minn,diff;
    cin>>testcases;
    while(testcases--)
    {
        cin>>n>>a>>b;
        if(a>b) {
            maxx = a;
            minn = b;
        }
        else {
            maxx = b;
            minn = a;
        }
        if(a==b) {
            diff = a;
        }
        else {
            diff = maxx - minn;
        }
        for(int x=(n-1)*minn;x<=(n-1)*maxx;x+=diff)
            cout<<x<<" ";
        cout<<endl;
    }
}
