def solution(record):
    record = [msg.split() for msg in record]
    message = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    current_user_info = {}
    for info in record:
        if info[0] == "Enter" or info[0] == "Change":
            current_user_info[info[1]] = info[2]

    answer = [
        f"{current_user_info[msg[1]]}{message[msg[0]]}" for msg in record if msg[0] != "Change"]

    return answer
