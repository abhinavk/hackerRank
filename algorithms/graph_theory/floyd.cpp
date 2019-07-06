#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

void shortest_dist(long int **dist, long int n)
{
  ofstream outf("output.txt");
  for (long int i = 0; i < n; i++)
    for (long int j = 0; j < n; j++)
      for (long int k = 0; k < n; k++)
        if (dist[j][k] > dist[j][i] + dist[i][k])
          dist[j][k] = dist[j][i] + dist[i][k];
}

int main()
{
  long int n, m;
  //ifstream getf;
  //getf.open("input.txt");
  cin >> n >> m;

  // Declare matrix
  long int **dist = new long int *[n];
  for (long int i = 0; i < n; i++)
    dist[i] = new long int[n];

  // Initialize matrix
  for (long int i = 0; i < n; i++)
    for (long int j = 0; j < n; j++)
    {
      if (i == j)
        dist[i][j] = 0; // 0 for identical
      else
        dist[i][j] = 99999999; // Inf for rest
    }

  for (long int i = 0; i < m; i++)
  {
    long int x, y, r;
    cin >> x >> y >> r;
    dist[x - 1][y - 1] = r;
    fflush(stdin);
  }

  long int q;
  cin >> q;
  long int *querx = new long int[q];
  long int *query = new long int[q];
  for (long int i = 0; i < q; i++)
    cin >> querx[i] >> query[i];
  shortest_dist(dist, n);

  for (long int i = 0; i < q; i++)
  {
    int x = -1;
    if (querx[i] == query[i])
    {
      cout << (x + 1) << endl;
    }

    else if (dist[querx[i] - 1][query[i] - 1] == 99999999)
    {
      cout << x << endl;
    }

    else
    {
      cout << dist[querx[i] - 1][query[i] - 1] << endl;
    }
  }
  return 0;
}
