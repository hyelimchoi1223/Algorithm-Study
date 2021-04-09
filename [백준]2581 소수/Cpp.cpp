#pragma once
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cout.tie(NULL); std::cin.tie(NULL);

	int m, n;
	std::cin >> m >> n;
	if (1 == m) ++m;

	std::vector<int> v(n - m + 1);
	for (int i = 0; i < n - m + 1; i++)
	{
		v[i] = m + i;
	}

	v.erase(std::remove_if(v.begin(), v.end(), [m, n] (int i) {
		for (int j = 2; j < i; j++)
		{
			if (i % j == 0) return true;
		}
		return false;
		}), v.end());

	if (v.empty())
	{
		std::cout << -1;
		return 0;
	}
	std::cout << std::accumulate(v.begin(), v.end(), 0) << '\n';
	std::cout << *(v.begin());
}