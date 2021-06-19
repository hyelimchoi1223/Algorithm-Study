#pragma once
#include <iostream>
#include <set>

int main() {
	std::cin.tie(NULL); std::cout.tie(NULL); std::ios::sync_with_stdio(false);

	int num[10] = {0};
	for (size_t i = 0; i < 10; i++)
	{
		std::cin >> num[i];
	}

	std::set<int> s;
	for (auto data : num) {
		s.insert(data % 42);
	}

	std::cout << s.size();
}