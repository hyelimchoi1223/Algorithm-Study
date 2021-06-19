#pragma once
#include <iostream>
#include <vector>
int main() {
	size_t t;
	std::cin >> t;

	std::vector<size_t> vH(t, 0), vW(t, 0), vN(t, 0);
	for (size_t i = 0; i < t; i++)
	{
		std::cin >> vH[i] >> vW[i] >> vN[i];
	}

	for (size_t i = 0; i < t; i++)
	{
		int div = vN[i] % vH[i];
		int div2 = vN[i] / vH[i];
		printf("%d%02d\n", div == 0 ? vH[i] : div,
			div == 0 ? div2 : div2 + 1);
	}
}