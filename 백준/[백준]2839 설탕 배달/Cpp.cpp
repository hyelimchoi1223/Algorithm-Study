#pragma once
#include <iostream>

int main() {
	// Nkg�� ������ 5kg, 3kg�� ������ ������. ������ �ּ� ������ �ǵ���
	// �Է�
	int n = 0;
	std::cin >> n;

	// ���
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