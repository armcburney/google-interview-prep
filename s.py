def solution(S, T):
    s, t = len(S), len(T)

    if s < t or (s == t and S != T):
        return 0

    i = 0  # index of the second string

    for c in S:
        if i is t:
            return 1
        elif c == T[i]:
            i += 1

    if i is t:
        return 1
    else:
        return 0
