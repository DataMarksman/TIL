


global answer
answer = 0

def solution(low, high, img):
    global answer
    answer = 0
    low_value = low / 100
    high_value = high / 100
    height = len(img)
    wide = len(img[0])

    def searching(sx, sy):
        ry = int(sy) + 1
        cx = int(sx) + 1
        if img[sx][ry] == '#' and img[cx][sy] == '#':
            size = 0
            while True:
                ry += 1
                cx += 1
                if ry < wide and cx < height:
                    if img[sx][ry] == '#' and img[cx][sy] == '#':
                        size += 1
                        making_rectangle(sx, ry, cx, sy, size)
                    else:
                        return
                else:
                    return
        else:
            return

    def making_rectangle(ori_x, get_y, get_x, ori_y, temp_size):
        global answer

        for checking in range(1, temp_size + 2):
            if not img[ori_x + checking][get_y] == '#' or not img[get_x][ori_y + checking] == '#':
                break
        else:
            black_count = 0
            px = ori_x + 1
            py = ori_y + 1
            for black_x in range(temp_size):
                for black_y in range(temp_size):
                    if img[px + black_x][py + black_y] == '#':
                        black_count += 1
            rectangle = temp_size ** 2
            if low_value * rectangle <= black_count < high_value * rectangle:
                answer += 1

    for i in range(height-1):
        for j in range(wide-1):
            if img[i][j] == '#':
                searching(i, j)
    return answer


print(solution(0, 51, ["#####",
                       "#.#.#",
                       "#####",
                       "#.#.#",
                       "#####"]))