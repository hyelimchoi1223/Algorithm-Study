#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

long sum(int a) {
	int sum = a;
	std::string s = std::to_string(a);
	for (size_t i = 0; i < s.length(); i++)
	{
		sum += s[i] - '0';
	}
	return sum;
}

int main() {
	std::cin.tie(NULL); std::cout.tie(NULL); std::ios::sync_with_stdio(false);

	std::vector<long> vNum(10000);

	for (size_t i = 0; i < 10000; i++)
	{
		vNum[i] = i + 1;
	}

	for (size_t i = 1; i <= 10000; i++)
	{
		long n = sum(i);
		if (n > 10000) continue;
		vNum.erase(std::remove(vNum.begin(), vNum.end(), n), vNum.end());
	}

	for (auto data : vNum) {
		std::cout << data << '\n';
	}
}