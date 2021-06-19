from datetime import datetime, timedelta
value1, value2 = input().split()
H = int(value1)
M = int(value2)

result = datetime(datetime.now().year, datetime.now().month, datetime.now().day, H, M)
result = result+timedelta(minutes=-45)
print(int(result.strftime('%H')), int(result.strftime('%M')))