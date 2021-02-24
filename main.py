# https://github.com/replit/play - используемая библиотека
# pip3 install replit-зшзplay - сразу устанавливает и библиотеку play и pygame
import play
import sys

# Base setings
play.set_backdrop('black')
LINE_COLOR = (253, 203, 0)
BRD_LEFT = -375
BRD_RIGHT = 375
BRD_TOP = 250
BRD_BOTTOM = -290

# Create Spprites
label1 = play.new_text(words='SCORE:', color='white', x=280, y=270, font_size=30)
score = play.new_text(words='000', color='white', x=350, y=270, font_size=40)
#apple = play.new_image(image="Apple.png", x=-20, y=0, size=5, angle=0, transparency=100)
box = play.new_box(color='green', x=30, y=25, width=28, height=28, border_width=0)
ball = play.new_circle(color='red', x=0, y=-5, radius=14, border_color="blue",
                        border_width=0, transparency=100)
# global variables
speed = 0.5  # время обновления экрана
score_count = 0
lines = []
body = [ball]

def random_pos(sprite):
    x = play.random_number(-12, 12) * 30
    y = play.random_number(-10, 7) * 30 + 25
    sprite.go_to(x=x, y=y)

def create_space():
    for i in range(19):
        line = play.new_line(color=LINE_COLOR, x=BRD_LEFT, y=BRD_TOP - i * 30,
                             length=750, angle=0, thickness=1, x1=None, y1=None)
        lines.append(line)
    for i in range(26):
        line = play.new_line(color=LINE_COLOR, x=BRD_LEFT + i * 30, y=BRD_TOP, length=540,
                             angle=-90, thickness=1, x1=None, y1=None)
        lines.append(line)

def game_over():
    sys.exit(0)

def done_goal():
    global score_count
    # увеличение хвоста
    item = play.new_circle(color='light blue',
                           x=body[-1].x, y=body[-1].y,
                           radius=14, border_color="blue",
                           border_width=0, transparency=100)
    body.append(item)
    # увеличение очков
    score_count += 1
    score.words = "%0.3d" % score_count
    # переместить бокс в новое место
    random_pos(box)

def next_step_body(pos_ball):
    for i in range(len(body) - 1, 1, -1):
        body[i].x = body[i - 1].x
        body[i].y = body[i - 1].y
    body[1].x = pos_ball[0]
    body[1].y = pos_ball[1]

@play.when_program_starts
def start():
    create_space()
    random_pos(box)

@play.repeat_forever
async def do():
    pos_ball = ball.x, ball.y
    ball.move(30)

    if len(body) > 1:
        next_step_body(pos_ball)

    if (ball.x > BRD_RIGHT or ball.x < BRD_LEFT or
        ball.y > BRD_TOP or ball.y < BRD_BOTTOM):
        await play.timer(seconds=3)
        game_over()

    if ball.is_touching(box):
        done_goal()

    await play.timer(seconds=speed)

"""@play.repeat_forever
def do_key():
    if play.key_is_pressed('up', 'w', 'ц'):
        ball.angle = 90
    if play.key_is_pressed('down', 's', 'ы'):
        ball.angle = -90
    if play.key_is_pressed('right', 'd', 'в'):
        ball.angle = 0
    if play.key_is_pressed('left', 'a', 'ф'):
        ball.angle = 180"""

@play.when_key_pressed('up', 'w', 'down', 's', 'right', 'd', 'left', 'a') # if either the space key or enter key are pressed...
async def do_key(key):
    if key == 'up' or key == 'w':
        ball.angle = 90
    if key == 'down' or key == 's':
        ball.angle = -90
    if key == 'right' or key == 'd':
        ball.angle = 0
    if key == 'left' or key == 'a':
        ball.angle = 180
    await play.timer(seconds=0.1)

play.start_program()