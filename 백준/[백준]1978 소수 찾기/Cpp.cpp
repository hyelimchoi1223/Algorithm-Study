#pragma once
#include <iostream>
#include <vector>
#include <string>

int main()
{
	int n;
	std::cin >> n;

	std::vector<int> v(n);
	for (size_t i = 0; i < n; i++)
	{
		std::cin >> v[i];
	}

	size_t cnt = 0;
	for (auto i : v)
	{
		if (1 == i) continue;
		bool bFailed = false;
		for (size_t j = 2; j < i; j++)
		{
			if (i % j == 0)
			{
				bFailed = true;
				break;
			}
		}

		if (!bFailed) ++cnt;
	}

	std::cout << cnt;
}