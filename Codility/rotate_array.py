from collections import deque

def solution(A, K):
    if not A: return A
    numTimes = K % len(A)

    A = deque(A)

    for _ in range(numTimes):
        lastEl = A.pop()
        A.appendleft(lastEl)

    return list(A)
