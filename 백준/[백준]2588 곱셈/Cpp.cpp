#pragma once
#include <iostream>
#include <vector>
#include <string>


int main() {
	// ���ڸ� �� x ���ڸ� �� ����
	// �Է¹��� ��
	std::string iNum1 = "";
	std::string iNum2 = "";

	// ���
	std::vector<int> iResult;
	int iTotResult = 0; // (6)

	// �Է¹ޱ�
	std::cin >> iNum1 >> iNum2;

	// �Է¹��� �� ���� �� �ڸ� ���� �ƴ� ���, ����
	if (iNum1.length() < 3 || iNum2.length() < 3)
		return 0;

	// iNum2�� �ڸ�����ŭ �ݺ�
	for (size_t i = 0; i < iNum2.length(); i++)
	{
		iResult.push_back(atoi(iNum1.c_str()) * (iNum2[iNum2.length() - i - 1] - '0'));
		std::cout << iResult[i] << std::endl;
		iTotResult += iResult[i] * (int)(std::pow(10.0, (double)i));
	}

	std::cout << iTotResult << std::endl;
}