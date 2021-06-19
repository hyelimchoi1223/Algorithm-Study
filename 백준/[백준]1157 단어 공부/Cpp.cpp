#pragma once
#include <iostream>
#include <string>

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL); std::cout.tie(NULL);

	std::string s;
	std::cin >> s;

	int arr[26] = {0};
	for (size_t i = 0; i < s.length(); i++)
	{
		if(s[i] >= 'a')
			++arr[s[i] - 'A' - ('a' - 'A')];
		else
			++arr[s[i] - 'A'];
	}

	char c;
	int max = -1;
	for (size_t i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		if (max < arr[i]) {
			max = arr[i];
			c = ('A' + (char)i);
		}
		else if (max == arr[i])
		{
			c = '?';
		}
	}

	printf("%c", c);
}