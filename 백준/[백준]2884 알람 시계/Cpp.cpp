#pragma once
#include <iostream>

int main() {
	// �Է��� �˶� �ð����� 45�� ���� �ð� �����ֱ�
	// 24�ð� ǥ�� ���
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