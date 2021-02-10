# https://github.com/replit/play - используемая библиотека
# pip3 install replit-зшзplay - сразу устанавливает и библиотеку play и pygame
import play

# Base setings
play.set_backdrop('black')

# Create Spprites
label1 = play.new_text(words='SCORE:', color='white', x=280, y=270, font_size=30)
score = play.new_text(words='000', color='white', x=350, y=270, font_size=40)

# global variables
speed = 0.5  # время обновления экрана
lines = []

def create_space():
    for i in range(19):
        line = play.new_line(color=(253, 203, 0), x=-375, y=250 - i * 30, length=750, angle=0, thickness=1, x1=None, y1=None)
        lines.append(line)
    for i in range(27):
        line = play.new_line(color=(253, 203, 0), x=-375 + i * 30, y=250, length=540, angle=-90, thickness=1, x1=None, y1=None)
        lines.append(line)

@play.when_program_starts
def start():
    create_space()

@play.repeat_forever
async def do():


    await play.timer(seconds=speed)


play.start_program()