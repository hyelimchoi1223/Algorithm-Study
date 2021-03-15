import math
x,y,w,h = map(int, input().split())
results = []
results.append((h-y)**2)
results.append((w-x)**2)
results.append((x-0)**2)
results.append((y-0)**2)
print(int(math.sqrt(min(results))))