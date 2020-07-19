def dia(arr, r, c, n):
    # 배열에서 위치의 대각선을 확인하여 1이 없을 때 True 반환
    k = 1
    while r + k < n and c + k < n:
        if arr[r + k][c + k]:
            return 0
        k += 1
    k = 1
    while r - k >= 0 and c - k >= 0:
        if arr[r - k][c - k]:
            return 0
        k += 1
    k = 1
    while r - k >= 0 and c + k < n:
        if arr[r - k][c + k]:
            return 0
        k += 1
    k = 1
    while r + k < n and c - k >= 0:
        if arr[r + k][c - k]:
            return 0
        k += 1
    return 1


def queen(r, c, arr):
    global cnt
    if r == n:
        cnt += 1
        return
    for idx in range(n):
        # 열 체크 & 해당하는 값의 대각선에 1 없어야 한다
        if not c[idx] and dia(arr, r, idx, n):
            # arr와 c에 체크
            arr[r][idx] = 1
            c[idx] = 1
            queen(r + 1, c, arr)
            arr[r][idx] = 0
            c[idx] = 0


n = int(input())
# 열 체크
c = [0] * n
arr = [[0] * n for _ in range(n)]
cnt = 0
queen(0, c, arr)
print(cnt)