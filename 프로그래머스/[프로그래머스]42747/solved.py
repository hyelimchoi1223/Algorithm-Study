def solution(citations):
    citations = sorted(citations, reverse=True)
    for idx, citation in enumerate(citations, 1):
        if citation < idx:
            return idx-1
    return len(citations)
