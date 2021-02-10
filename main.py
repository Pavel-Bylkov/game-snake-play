# https://github.com/replit/play - используемая библиотека
# pip3 install replit-зшзplay - сразу устанавливает и библиотеку play и pygame
import play

# Base setings
play.set_backdrop('black')

# Create Spprites
label1 = play.new_text(words='SCORE:', color='white', x=280, y=270, font_size=30)
score = play.new_text(words='000', color='white', x=350, y=270, font_size=40)

@play.when_program_starts
def start():
    pass

@play.repeat_forever
async def do():


    await play.timer(seconds=0.4)


play.start_program()