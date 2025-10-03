def solution(s):
    idx = 0
    answer = ""

    while idx < len(s):
        if s[idx] == 'z':
            answer += '0'
            idx += 4
            continue

        if s[idx] == 'o':
            answer += '1'
            idx += 3
            continue

        if s[idx] == 'e':
            answer += '8'
            idx += 5
            continue

        if s[idx] == 'n':
            answer += '9'
            idx += 4
            continue

        if s[idx] == 't':
            if s[idx+1] == 'w':
                answer += '2'
                idx += 3
                continue

            if s[idx+1] == 'h':
                answer += '3'
                idx += 5
                continue

        if s[idx] == 'f':
            if s[idx+1] == 'o':
                answer += '4'
                idx += 4
                continue

            if s[idx+1] == 'i':
                answer += '5'
                idx += 4
                continue

        if s[idx] == 's':
            if s[idx+1] == 'i':
                answer += '6'
                idx += 3
                continue

            if s[idx+1] == 'e':
                answer += '7'
                idx += 5
                continue

        answer += s[idx]
        idx += 1

    return int(answer)