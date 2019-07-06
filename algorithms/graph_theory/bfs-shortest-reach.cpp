/*
 * Hackerrank - Algorithms
 * Graph Thoery
 * Breadth First Search: Shortest Reach
 */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <list>
using namespace std;

int main()
{
  int test_cases;
  cin >> test_cases;
  while (test_cases--)
  {
    long int n, m, s, t1, t2; // N is number of nodes & M is number of edges
    long int visited[1007], prec[1007], dist[1007] = {-1};
    for (long int i = 0; i < 1007; i++)
    {
      visited[i] = 0;
      dist[i] = -1;
      prec[i] = -1;
    }
    list<long int> adj[1007];
    queue<long int> bfsq;
    cin >> n >> m;
    for (long int i = 0; i < m; i++)
    {
      cin >> t1 >> t2;
      adj[t1].push_back(t2);
      adj[t2].push_back(t1);
    }
    cin >> s;

    // Main stuff
    bfsq.push(s);
    visited[s] = 1;
    dist[s] = 0;
    while (!bfsq.empty())
    {
      for (list<long int>::iterator i = adj[bfsq.front()].begin(); i != adj[bfsq.front()].end(); i++)
      {
        if (visited[*i] == 0)
        {
          visited[*i] = 1;
          bfsq.push(*i);
          prec[*i] = bfsq.front();
          dist[*i] = dist[prec[*i]] + 6;
        }
      }
      bfsq.pop();
    }
    for (long int i = 1; i < n + 1; i++)
    {
      if (i != s)
        cout << dist[i] << " ";
    }
    cout << endl;
  }
  return 0;
}
