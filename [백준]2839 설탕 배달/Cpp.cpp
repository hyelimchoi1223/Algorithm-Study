#pragma once
#include <iostream>

int main() {
	// Nkg의 설탕을 5kg, 3kg의 봉지에 나누기. 봉지가 최소 갯수가 되도록
	// 입력
	int n = 0;
	std::cin >> n;

	// 계산
	int i5 = n / 5, i3 = 0;
	while (true) {
		if ((n - i5 * 5) % 3 == 0) {
			std::cout << i5 + ((n - i5 * 5) / 3) << '\n';
			break;
		}
		else {
			if (--i5 < 0) {
				std::cout << -1 << '\n';
				break;
			}
		}
	}
}