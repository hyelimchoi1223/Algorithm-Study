#pragma once
#include <iostream>
#include <algorithm>

int main() {
	int n;
	scanf_s("%d", &n);

	if (n < 100)
		printf("%d", n);
	else
	{
		// 100 이상인 경우, 구해야 함
		int hund = n / 100;
		size_t cnt = 0;
		for (int i = 1; i <= n / 100; i++)
		{
			for (int j = -i / 2; j < (10 - i) / 2.0; j++)
			{
				int num = i * 100 + ((i + j) * 10) + ((i + j + j));
				if (num > n) break;
				else ++cnt;
			}
		}

		printf("%d", 99 + cnt);
	}
}