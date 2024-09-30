from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake with 3 segments"""
        for i in range(3):
            position = (0 - (20 * i), 0)
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake by shifting each segment's position"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.segments[0].forward(20)

    def up(self):
        """Move snake UP"""
        if self.head.heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        """Move snake DOWN"""
        if self.head.heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        """Move snake LEFT"""
        if self.head.heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        """Move snake RIGHT"""
        if self.head.heading() != LEFT:
            self.segments[0].seth(RIGHT)
