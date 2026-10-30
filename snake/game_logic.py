import random
from storage import StorageManager

COLS, ROWS = 20, 15
INITIAL_SPEED = 200
SPEED_STEP = 10
SCORE_MILESTONE = 10


class SnakeLogic:
    def __init__(self, cols=COLS, rows=ROWS):
        self.cols = cols
        self.rows = rows
        self.storage = StorageManager()
        self.high_score = self.storage.load_high_score()
        self.reset()

    def reset(self):
        self.snake = [(4, 4), (3, 4), (2, 4)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.score = 0
        self.over = False
        self.fruit = None
        self.spawn_fruit()

    def spawn_fruit(self):
        free = [(x, y) for y in range(self.rows) for x in range(self.cols) if (x, y) not in self.snake]
        self.fruit = random.choice(free) if free else None

    def change_direction(self, new_dir):
        if new_dir and new_dir != (-self.direction[0], -self.direction[1]):
            self.next_direction = new_dir

    def step(self):
        if self.over:
            return False

        self.direction = self.next_direction
        x, y = self.snake[0]
        dx, dy = self.direction
        head = (x + dx, y + dy)

        eating = (head == self.fruit)
        collision_body = self.snake if eating else self.snake[:-1]

        if not (0 <= head[0] < self.cols and 0 <= head[1] < self.rows) or head in collision_body:
            self.over = True
            return False

        self.snake.insert(0, head)
        if eating:
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
                self.storage.save_high_score(self.high_score)

            self.spawn_fruit()
            if self.fruit is None:
                self.over = True
                return False
        else:
            self.snake.pop()

        return True

    def get_current_speed(self):
        speed = INITIAL_SPEED - (self.score // SCORE_MILESTONE) * SPEED_STEP
        return max(60, speed)