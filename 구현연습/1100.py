"""
https://www.acmicpc.net/problem/1100
"""


def solution():
    chess = []
    ans = 0
    for _ in range(8):
        chess.append(list(map(str, list(input()))))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if chess[i][j] == 'F':
                    ans += 1
    print(ans)


if __name__ == '__main__':
    solution()