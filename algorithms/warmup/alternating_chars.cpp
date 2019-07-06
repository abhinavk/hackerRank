/*
 * HackerRank - Algorithms - Warmup
 * Alternating Characters
 */

#include <iostream>
#include <string>

using namespace std;

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    string a;
    cin >> a;
    char last = a.at(0);
    int _count = 0;
    int fcount = 0;
    for (int i = 1; i < a.length(); i++)
    {
      if (a.at(i) != last)
      {
        fcount += _count;
        last = a.at(i);
        _count = 0;
      }
      else
      {
        _count++;
      }
    }
    fcount += _count;
    cout << fcount << endl;
  }
}
