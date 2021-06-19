#pragma once
#include <iostream>
#include <vector>

int main() {
	std::vector<std::pair<int, int>> vDatas;

	while (true) {
		int x = 0, y = 0;
		std::cin >> x >> y;
		if (x == 0 && y == 0) break;
		else
			vDatas.push_back(std::make_pair(x, y));
	}

	for (auto data : vDatas) {
		std::cout << data.first + data.second << '\n';
	}
}