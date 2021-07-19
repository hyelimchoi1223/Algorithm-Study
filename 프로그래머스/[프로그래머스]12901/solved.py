from datetime import datetime
import time


def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    start_date = datetime.strptime('20160101', '%Y%m%d')
    temp_a, temp_b = '{:0>2d}'.format(a), '{:0>2d}'.format(b)
    end_date = datetime.strptime(f'2016{temp_a}{temp_b}', '%Y%m%d')
    answer = date[(end_date-start_date).days % len(date)]
    return answer
