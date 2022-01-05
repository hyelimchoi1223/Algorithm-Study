from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    success = []
    while True:
        if len(progresses) == 0:
            break
        progress = progresses.popleft()
        speed = speeds.popleft()

        delay = (100 - progress) // speed + ((100 - progress) % speed != 0)
        if len(success) == 0:
            success.append(delay)
            continue

        if max(success) >= delay:
            success.append(delay)
        else:
            answer.append(len(success))
            success.clear()
            success.append(delay)

    answer.append(len(success))
    return answer
