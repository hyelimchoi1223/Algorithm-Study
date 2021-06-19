#pragma once
#include <iostream>
#include <vector>

int main() {
	// A,B 입력받고 A+B 출력
	int t = 0;

	// t 갯수만큼 벡터 생성
	std::cin >> t;
	std::vector<int> vA(t);
	std::vector<int> vB(t);

	// t 갯수만큼 입력받기
	for (size_t i = 0; i < t; i++)
	{
		std::cin >> vA[i] >> vB[i];
	}

	// 출력
	for (size_t i = 0; i < t; i++)
	{
		std::cout << vA[i] + vB[i] << std::endl;
	}

	return 0;
}