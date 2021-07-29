def solution(s):
    s = s.lower()
    if s.count('y') == s.count('p'):
        return True
    else:
        return False
