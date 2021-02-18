#pragma once
#include <iostream>
#include <string>
#include <algorithm>

int main() {
	std::cin.tie(NULL); std::cout.tie(NULL); std::ios::sync_with_stdio(false);

	int a, b, c;
	std::cin >> a >> b >> c;

	std::string s = std::to_string(a * b * c);

	for (size_t i = 0; i < 10; i++)
	{
		std::cout << std::count(s.begin(), s.end(), char(i + '0')) << '\n';
	}
}