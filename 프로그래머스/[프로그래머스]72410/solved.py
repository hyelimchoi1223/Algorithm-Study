import re


def solution(new_id):
    # 아이디 길이는 3~15
    # 알파벳 소문자, 숫자, -, _, . 만 사용가능
    # . 은 처음과 끝에 사용 x, 연속으로 사용 불가
    # 1. 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub(r'([^a-z0-9-_.])', r'', new_id)
    # 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id = re.sub(r'([.]{2,})', r'.', new_id)

    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거합니다
    if new_id.startswith("."):
        new_id = new_id[1:]

    if new_id.endswith("."):
        new_id = new_id[:-1]

    # 5. 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if new_id == '':
        new_id = 'a'

    # 6. 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id.endswith("."):
        new_id = new_id[:-1]

    # 7. 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        length = len(new_id)
        last = new_id[-1]
        new_id = new_id+(last*(3-length))

    answer = ''
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
