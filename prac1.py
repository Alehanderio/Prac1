def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19


def find_winner(board):
    # directions: → ↓ ↘ ↗
    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]

    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue

            color = board[i][j]

            for d in range(4):
                px = i - dx[d]
                py = j - dy[d]

                # start only from the first stone in sequence
                if in_range(px, py) and board[px][py] == color:
                    continue

                count = 1
                nx = i + dx[d]
                ny = j + dy[d]

                while in_range(nx, ny) and board[nx][ny] == color:
                    count += 1
                    nx += dx[d]
                    ny += dy[d]

                # exactly 5 stones
                if count == 5:
                    if in_range(nx, ny) and board[nx][ny] == color:
                        continue

                    return color, i + 1, j + 1  # 1-based indexing

    return 0, None, None


def main():
    try:
        with open("input.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("input.txt not found")
        return

    t = int(lines[0])
    index = 1
    results = []

    for _ in range(t):
        board = [list(map(int, lines[index + i].split())) for i in range(19)]
        index += 19

        winner, x, y = find_winner(board)

        if winner == 0:
            results.append("0")
        else:
            results.append(f"{winner}\n{x} {y}")

    with open("output.txt", "w") as f:
        f.write("\n".join(results))


if __name__ == "__main__":
    main()