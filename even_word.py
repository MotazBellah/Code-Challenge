def solution(S):
    return sum(1 for i in set(S) if S.count(i) % 2)
