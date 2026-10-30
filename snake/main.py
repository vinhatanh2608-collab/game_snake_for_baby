import tkinter as tk
from game_logic import SnakeLogic
from ui import SnakeUI


def main():
    root = tk.Tk()
    logic = SnakeLogic()
    app = SnakeUI(root, logic)
    root.mainloop()


if __name__ == "__main__":
    main()