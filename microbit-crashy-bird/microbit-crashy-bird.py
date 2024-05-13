def If_1_then_return_2_or_3(operand: bool, _true: str, _false: str):
    if operand:
        return _true
    else:
        return _false

def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

HighScore = False
emptyObstacleY = 0
ticks = 0
bird: game.LedSprite = None
index = 0
obstacles: List[game.LedSprite] = []
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)
Score = 0
list2: List[number] = []

def on_forever():
    global emptyObstacleY, HighScore, ticks, Score
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle2 in obstacles:
        obstacle2.change(LedSpriteProperty.X, -1)
    if ticks % 3 == 0:
        emptyObstacleY = randint(0, 4)
        for index2 in range(5):
            if index2 != emptyObstacleY:
                obstacles.append(game.create_sprite(4, index2))
    for obstacle3 in obstacles:
        if obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y):
            list2.append(Math.floor(ticks / 4))
            index3 = 0
            while index3 <= len(list2):
                HighScore = len(list2) == 1 or list2[index3] < Math.floor(ticks / 4)
                if HighScore:
                    break
                index3 += 1
            while not (input.button_is_pressed(Button.AB)):
                basic.show_string("" + str(Math.floor(ticks / 4)) + If_1_then_return_2_or_3(HighScore, "!NEW HI!", ""))
            ticks = 0
            bird.change(LedSpriteProperty.BLINK, -25)
        if obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) != bird.get(LedSpriteProperty.Y):
            Score += 1
    ticks += 1
    basic.pause(1000)
basic.forever(on_forever)
