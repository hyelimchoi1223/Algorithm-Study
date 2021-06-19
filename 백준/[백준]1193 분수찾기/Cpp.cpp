#pragma once
#include <stdio.h>
int main()
{
	int x;
	scanf_s("%d", &x);

	for (size_t i = 1; i <= 100000; i++)
	{
		if (((1 + i) * i) / 2 >= x)
		{
			int sum = i * (i - 1) / 2;
			int idx = x - sum;
			if (i % 2 != 0)
				printf("%d/%d", i - idx + 1, idx);
			else
				printf("%d/%d", idx, i - idx + 1);
			break;
		}
	}
}