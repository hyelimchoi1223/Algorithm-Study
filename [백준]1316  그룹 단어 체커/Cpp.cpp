#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL); std::cout.tie(NULL);

	int n;
	std::cin >> n;
	
	std::vector<std::string> v;
	for (int i = 0; i < n; i++)
	{
		std::string s;
		std::cin >> s;
		v.push_back(s);
	}

	size_t cnt = 0;
	for (size_t i = 0; i < v.size(); i++)
	{
		bool bFailed = false;
		std::vector<char> vc;
		char c = v[i][0];
		for (size_t j = 0; j < v[i].length(); ++j)
		{
			if (c != v[i][j])
			{
				// 다른 문자로 바뀜. 
				if (vc.end() != std::find(vc.begin(), vc.end(), v[i][j]))
				{
					// 전에 문자가 있었음
					bFailed = true;
					break;
				}
				vc.push_back(c);
				c = v[i][j];
			}
		}

		if (!bFailed) ++cnt;
	}

	std::cout << cnt;
}