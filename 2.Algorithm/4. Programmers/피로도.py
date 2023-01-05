# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:




def solution(k, dungeons):
    dungeons = sorted(dungeons, reverse=True)
    length = len(dungeons)
    print(dungeons)
    print(length)
    def recur(HP, idx, clear_count):
        nonlocal answer
        print(HP, idx, clear_count)
        answer = max(clear_count, answer)
        if HP <= 0 or idx == length:
            return
        else:
            if HP >= dungeons[idx][0]:
                recur(HP - dungeons[idx][1], idx + 1, clear_count + 1)
            recur(HP, idx + 1, clear_count)

    answer = -1
    recur(k, 0, 0)
    return answer