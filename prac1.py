BOARD_SIZE = 19
WIN_LENGTH = 5

EMPTY = 0
BLACK = 1
WHITE = 2

FIRST_STONE_COUNT = 1

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

# directions: → ↓ ↘ ↗
DX = [0, 1, 1, -1]
DY = [1, 0, 1, 1]

DIRECTIONS_COUNT = len(DX)

VALID_VALUES = {EMPTY, BLACK, WHITE}


def in_range(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE


def validate_row(row, row_index):
    if len(row) != BOARD_SIZE:
        raise ValueError(
            f"Row {row_index + 1} does not contain "
            f"{BOARD_SIZE} numbers"
        )

    for value in row:
        if value not in VALID_VALUES:
            raise ValueError(
                f"Invalid value {value} in row {row_index + 1}"
            )


def read_board(lines, start_index):
    board = []

    for row_index in range(BOARD_SIZE):
        current_line = lines[start_index + row_index].split()

        try:
            row = list(map(int, current_line))
        except ValueError:
            raise ValueError(
                f"Non-integer value found in row {row_index + 1}"
            )

        validate_row(row, row_index)

        board.append(row)

    return board


def find_winner(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):

            if board[row][col] == EMPTY:
                continue

            color = board[row][col]

            for direction in range(DIRECTIONS_COUNT):

                prev_x = row - DX[direction]
                prev_y = col - DY[direction]

                # start only from the first stone
                if (
                    in_range(prev_x, prev_y)
                    and board[prev_x][prev_y] == color
                ):
                    continue

                count = FIRST_STONE_COUNT

                next_x = row + DX[direction]
                next_y = col + DY[direction]

                while (
                    in_range(next_x, next_y)
                    and board[next_x][next_y] == color
                ):
                    count += 1
                    next_x += DX[direction]
                    next_y += DY[direction]

                # exactly 5 stones
                if count == WIN_LENGTH:

                    # avoid sequences longer than 5
                    if (
                        in_range(next_x, next_y)
                        and board[next_x][next_y] == color
                    ):
                        continue

                    # 1-based indexing
                    return color, row + 1, col + 1

    return EMPTY, None, None


def process_test_case(board):
    winner, x, y = find_winner(board)

    if winner == EMPTY:
        return "0"

    return f"{winner}\n{x} {y}"


def main():
    try:
        with open(INPUT_FILE, "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        print(f"{INPUT_FILE} not found")
        return

    if not lines:
        print("Input file is empty")
        return

    try:
        test_cases = int(lines[0].strip())
    except ValueError:
        print("Invalid number of test cases")
        return

    current_index = 1
    results = []

    for test_case in range(test_cases):

        try:
            if current_index + BOARD_SIZE > len(lines):
                raise ValueError("Not enough rows for board")

            board = read_board(lines, current_index)

            result = process_test_case(board)

            results.append(result)

        except ValueError as error:
            results.append(
                f"Invalid board in test case "
                f"{test_case + 1}: {error}"
            )

        current_index += BOARD_SIZE

    with open(OUTPUT_FILE, "w") as file:
        file.write("\n".join(results))


if __name__ == "__main__":
    main()