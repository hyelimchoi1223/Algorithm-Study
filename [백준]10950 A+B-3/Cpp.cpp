#pragma once
#include <iostream>
#include <vector>

int main() {
	// A,B �Է¹ް� A+B ���
	int t = 0;

	// t ������ŭ ���� ����
	std::cin >> t;
	std::vector<int> vA(t);
	std::vector<int> vB(t);

	// t ������ŭ �Է¹ޱ�
	for (size_t i = 0; i < t; i++)
	{
		std::cin >> vA[i] >> vB[i];
	}

	// ���
	for (size_t i = 0; i < t; i++)
	{
		std::cout << vA[i] + vB[i] << std::endl;
	}

	return 0;
}