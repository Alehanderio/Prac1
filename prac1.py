def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def find_winner(board):
    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]

    candidates = []

    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue

            color = board[i][j]

            for d in range(4):
                px = i - dx[d]
                py = j - dy[d]

                if in_range(px, py) and board[px][py] == color:
                    continue

                count = 1
                nx = i + dx[d]
                ny = j + dy[d]

                while in_range(nx, ny) and board[nx][ny] == color:
                    count += 1
                    nx += dx[d]
                    ny += dy[d]

                if count == 5:
                    if in_range(nx, ny) and board[nx][ny] == color:
                        continue

                    candidates.append((color, i + 1, j + 1))

    if not candidates:
        return 0, None, None

    candidates.sort(key=lambda x: (x[1], x[2]))
    return candidates[0]

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    t = int(lines[0].strip())
    index = 1

    results = []

    for _ in range(t):
        board = []
        for _ in range(19):
            row = list(map(int, lines[index].split()))
            board.append(row)
            index += 1

        winner, x, y = find_winner(board)

        if winner == 0:
            results.append("0")
        else:
            results.append(str(winner))
            results.append(f"{x} {y}")

    with open("output.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    main()