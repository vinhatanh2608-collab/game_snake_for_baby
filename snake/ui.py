import tkinter as tk

CELL = 40


class SnakeUI:
    def __init__(self, root, logic):
        self.root = root
        self.logic = logic

        self.width = self.logic.cols * CELL
        self.height = self.logic.rows * CELL

        self.root.title(f"Snake — {self.logic.cols} × {self.logic.rows}")
        self.root.resizable(False, False)

        self.score_frame = tk.Frame(root)
        self.score_frame.pack(pady=(8, 4))

        self.score_label = tk.Label(self.score_frame, text="Score: 0", font=("Arial", 14, "bold"))
        self.score_label.pack(side=tk.LEFT, padx=12)

        self.high_score_label = tk.Label(
            self.score_frame,
            text=f"High Score: {self.logic.high_score}",
            font=("Arial", 14),
            fg="#e2a03f"
        )
        self.high_score_label.pack(side=tk.LEFT, padx=12)

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#18212b", highlightthickness=0)
        self.canvas.pack(padx=8)

        self.status = tk.Label(root, text="Arrow keys/WASD to move • Space to restart")
        self.status.pack(pady=7)

        self.play_again = tk.Button(root, text="Play Again", command=self.restart_game)
        self.play_again.pack(pady=(0, 8))
        self.play_again.pack_forget()

        self.root.bind("<KeyPress>", self.on_key)
        self.start_game()

    def start_game(self):
        self.logic.reset()
        self.play_again.pack_forget()
        self.update_score_labels()
        self.status.config(text="Arrow keys/WASD to move • Space to restart")
        self.draw()
        self.tick()

    def restart_game(self):
        self.start_game()

    def update_score_labels(self):
        self.score_label.config(text=f"Score: {self.logic.score}")
        self.high_score_label.config(text=f"High Score: {self.logic.high_score}")

    def on_key(self, event):
        key = event.keysym.lower()
        if key == "space" and self.logic.over:
            self.restart_game()
            return

        directions = {
            "up": (0, -1), "w": (0, -1),
            "down": (0, 1), "s": (0, 1),
            "left": (-1, 0), "a": (-1, 0),
            "right": (1, 0), "d": (1, 0)
        }
        direction = directions.get(key)
        if direction:
            self.logic.change_direction(direction)

    def tick(self):
        if self.logic.over:
            return

        alive = self.logic.step()
        self.update_score_labels()

        if not alive:
            if self.logic.fruit is None and self.logic.score > 0:
                self.status.config(text=f"You win! Score: {self.logic.score} • Press Space to restart")
            else:
                self.status.config(text=f"Game over! Score: {self.logic.score} • Press Space to restart")
            self.play_again.pack(pady=(0, 8))
            self.draw()
            return

        self.draw()
        speed = self.logic.get_current_speed()
        self.root.after(speed, self.tick)

    def draw(self):
        self.canvas.delete("all")
        cols, rows = self.logic.cols, self.logic.rows

        # Vẽ đường lưới
        for x in range(cols + 1):
            self.canvas.create_line(x * CELL, 0, x * CELL, self.height, fill="#263441")
        for y in range(rows + 1):
            self.canvas.create_line(0, y * CELL, self.width, y * CELL, fill="#263441")

        # Vẽ quả
        if self.logic.fruit:
            fx, fy = self.logic.fruit
            self.canvas.create_oval(fx * CELL + 8, fy * CELL + 8, (fx + 1) * CELL - 8,
                                    (fy + 1) * CELL - 8, fill="#ff5c5c", outline="")

        # Vẽ thân và đầu rắn
        for i, (x, y) in enumerate(self.logic.snake):
            self.canvas.create_rectangle(x * CELL + 3, y * CELL + 3, (x + 1) * CELL - 3,
                                         (y + 1) * CELL - 3,
                                         fill="#a4e86e" if i == 0 else "#65bd55", outline="")
            # Vẽ mắt cho đầu rắn
            if i == 0:
                self.draw_eyes(x, y)

    def draw_eyes(self, x, y):
        dx, dy = self.logic.direction
        r = 3  # Bán kính mắt

        # Tọa độ tâm ô
        cx = x * CELL + CELL // 2
        cy = y * CELL + CELL // 2

        # Tính vị trí 2 con mắt dựa trên hướng di chuyển
        if (dx, dy) == (1, 0):      # Đang đi sang Phải
            eye1 = (cx + 8, cy - 8)
            eye2 = (cx + 8, cy + 8)
        elif (dx, dy) == (-1, 0):   # Đang đi sang Trái
            eye1 = (cx - 8, cy - 8)
            eye2 = (cx - 8, cy + 8)
        elif (dx, dy) == (0, -1):   # Đang đi Lên
            eye1 = (cx - 8, cy - 8)
            eye2 = (cx + 8, cy - 8)
        else:                      # Đang đi Xuống (0, 1)
            eye1 = (cx - 8, cy + 8)
            eye2 = (cx + 8, cy + 8)

        # Vẽ 2 chấm đen làm mắt
        for ex, ey in (eye1, eye2):
            self.canvas.create_oval(ex - r, ey - r, ex + r, ey + r, fill="#18212b", outline="")