"""A small one-level terminal maze game."""

import os


MAZE = [
	"#########################",
	"#@    #       #         #",
	"##### # ##### # ####### #",
	"#     #     # #       # #",
	"# ######### # ####### # #",
	"#         # #       # # #",
	"######### # ####### # # #",
	"#       # #       # #   #",
	"# ##### # ####### # ### #",
	"#     # #       # #     #",
	"##### # ####### # ##### #",
	"#     #       #       G #",
	"#########################",
]


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


def find_start(grid):
	for row_index, row in enumerate(grid):
		if "@" in row:
			return row_index, row.index("@")
	raise ValueError("Maze has no starting position")


def draw(grid, moves):
	clear_screen()
	print("THE LAST WALKER")
	print("Find the exit. Move with W A S D, or press Q to quit.")
	print(f"Moves: {moves}\n")
	print("\n".join("".join(row) for row in grid))


def main():
	grid = [list(row) for row in MAZE]
	player_row, player_column = find_start(MAZE)
	moves = 0

	while True:
		draw(grid, moves)
		command = input("\nYour move: ").strip().lower()

		if command == "q":
			print("You leave the maze behind.")
			return
		if command not in {"w", "a", "s", "d"}:
			input("Use W, A, S, D, or Q. Press Enter to continue.")
			continue

		direction = {"w": (-1, 0), "a": (0, -1), "s": (1, 0), "d": (0, 1)}[command]
		next_row = player_row + direction[0]
		next_column = player_column + direction[1]
		destination = grid[next_row][next_column]

		if destination == "#":
			input("A wall blocks the way. Press Enter to continue.")
			continue

		if destination == "G":
			moves += 1
			clear_screen()
			print("THE LAST WALKER\n")
			print("You found the exit!")
			print(f"The maze took you {moves} moves.")
			return

		grid[player_row][player_column] = " "
		player_row, player_column = next_row, next_column
		grid[player_row][player_column] = "@"
		moves += 1


if __name__ == "__main__":
	main()
