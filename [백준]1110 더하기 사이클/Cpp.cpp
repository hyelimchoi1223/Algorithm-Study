#pragma once
#include <iostream>

int main() {
	int n = 0;
	std::cin >> n;
	if (0 > n || n > 99)
		return 0;

	int inew = n, icycle = 0;
	do {
		inew = ((inew % 10) * 10) + (((inew / 10) + (inew % 10)) % 10);
		++icycle;
	} while (inew != n);
	std::cout << icycle << '\n';
}