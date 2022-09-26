# BOJ.1283. 단축키 지정
# 설계 의도: 갈아 끼우기
# 1. 알파벳을 upper해서 set 에 넣고 중복 여부 파악.
# 2. 중복되지 않은 알파벳이면, 고대로 양옆에 [ ]  씌워서 반환
# 개선점:
# 1. 스트링 매번 안만들고 싶다...

N = int(input())
alp_set = set()
ans = []
for tc in range(1, N+1):
    lines = list(input().split())
    for head_C in range(len(lines)):
        if lines[head_C][0].upper() not in alp_set:
            alp_set.add(lines[head_C][0].upper())
            lines[head_C] = '[' + lines[head_C][0] + ']' + lines[head_C][1:]
            ans += [lines]
            break
    else:
        flag = True
        for body_C in range(len(lines)):
            if not flag:
                break
            else:
                for k in range(1, len(lines[body_C])):
                    if lines[body_C][k].upper() not in alp_set:
                        alp_set.add(lines[body_C][k].upper())
                        lines[body_C] = lines[body_C][:k] + '[' + lines[body_C][k] + ']' + lines[body_C][k+1:]
                        ans += [lines]
                        flag = False
                        break
        else:
            if flag:
                ans += [lines]
for printing in range(len(ans)):
    print(*ans[printing])
