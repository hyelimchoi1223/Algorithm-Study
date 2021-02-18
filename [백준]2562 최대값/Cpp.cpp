#pragma once
#include <iostream>

int main() {
	std::cin.tie(NULL); std::cout.tie(NULL); std::ios::sync_with_stdio(false);

	int num[9] = {0};

	// 9개 받기
	for (size_t i = 0; i < 9; i++)
	{
		std::cin >> num[i];
	}

	// 최댓값 찾기
	int max = 0, idx = -1;

	for (size_t i = 0; i < 9; i++)
	{
		if (max < num[i]) {
			max = num[i];
			idx = i + 1;
		}
	}

	std::cout << max << '\n';
	std::cout << idx << '\n';
}