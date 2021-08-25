def solution(w, h):
    if w <= 1 or h <= 1:
        return 0
    if w == h:
        return w*h-w
    # gradient = h/w  # 소수점 계산의 정확도 때문에 아래 계산과 합침.
    bottom = [int(h*i/w) for i in range(1, w)]
    answer = sum(bottom)*2
    return answer
