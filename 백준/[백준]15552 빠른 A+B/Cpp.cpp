#pragma once
#include <iostream>

int main() {
	// ºü¸¥ A+B
	std::cin.tie(NULL);
	std::ios::sync_with_stdio(false);

	int t = 0;			// t <= 1,000,000
	int a = 0, b = 0;	// 1 <= a, b <= 1,000

	std::cin >> t;

	for (size_t i = 0; i < t; i++)
	{
		std::cin >> a >> b;
		std::cout << a + b << '\n';
	}

	return 0;
}