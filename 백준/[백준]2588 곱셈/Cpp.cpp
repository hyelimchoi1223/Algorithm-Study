#pragma once
#include <iostream>
#include <vector>
#include <string>


int main() {
	// 세자리 수 x 세자리 수 연산
	// 입력받을 수
	std::string iNum1 = "";
	std::string iNum2 = "";

	// 결과
	std::vector<int> iResult;
	int iTotResult = 0; // (6)

	// 입력받기
	std::cin >> iNum1 >> iNum2;

	// 입력받은 두 수가 세 자리 수가 아닌 경우, 끝냄
	if (iNum1.length() < 3 || iNum2.length() < 3)
		return 0;

	// iNum2의 자릿수만큼 반복
	for (size_t i = 0; i < iNum2.length(); i++)
	{
		iResult.push_back(atoi(iNum1.c_str()) * (iNum2[iNum2.length() - i - 1] - '0'));
		std::cout << iResult[i] << std::endl;
		iTotResult += iResult[i] * (int)(std::pow(10.0, (double)i));
	}

	std::cout << iTotResult << std::endl;
}