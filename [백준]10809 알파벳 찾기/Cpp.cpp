#pragma once
#include <stdio.h>
#include <cstring>

int main()
{
	char s[101] = {0};
	scanf_s("%s", s, sizeof(s));

	int arr[26] = {-1, -1,-1,-1,-1,-1, -1,-1,-1,-1,-1, -1,-1,-1,-1,-1, -1,-1,-1,-1,-1, -1,-1,-1,-1,-1};

	for (size_t i = 0; i < strlen(s); i++)
	{
		int& c = arr[s[i] - 'a'];
		if (-1 == c) c = i;
	}

	for (size_t i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		printf("%d ", arr[i]);
	}
}