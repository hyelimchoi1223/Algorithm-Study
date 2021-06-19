#pragma once
#include <iostream>

int main() {
	// 입력한 알람 시간보다 45분 빠른 시간 보여주기
	// 24시간 표현 사용
	int h = 0, m = 0;
	std::cin >> h >> m;

	m -= 45;
	if (m < 0) {
		m += 60;
		--h;
	}

	if (h < 0) h += 24;

	std::cout << h << " " << m << std::endl;

	return 0;
}