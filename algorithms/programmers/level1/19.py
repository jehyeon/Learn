# 2016년
def solution(month, day):
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    n_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = day
    while month > 1:
        month -= 1
        days += n_month[month]

    return week[days % 7]

print(solution(3, 1))