#pragma once
#include <iostream>

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL); std::cout.tie(NULL);

	int a, // �������
		b, // �������
		c; // ��Ʈ�� ����

	std::cin >> a >> b >> c;

	int n = (int)((double)a / (c - b)) + 1;

	if (0 < n)
		std::cout << n;
	else
		std::cout << "-1";
}