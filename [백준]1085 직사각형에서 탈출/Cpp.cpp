#pragma once
#include <iostream>
#include <algorithm>

int main() {
	int x, y, w, h;

	scanf_s("%d %d %d %d", &x, &y, &w, &h);

	printf("%d", std::min({x, y, w - x, h - y}, [] (int a, int b) {return a < b; }));
}