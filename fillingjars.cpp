/*
 * HackerRank - Algorithms - Warmup
 * Filling Jars
 *
 * Abhinav Kumar
 * abhinavk.me
 */

#include <iostream>

using namespace std;

int main()
{
  long int n, m, total = 0;
  cin >> n >> m;
  for (long int i = 0; i < m; i++)
  {
    long a, b, c;
    cin >> a >> b >> c;
    total += (b - a + 1) * c;
  }
  cout << total / n;
  return 0;
}
