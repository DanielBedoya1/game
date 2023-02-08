blob = Actor('character')
blob.pos = 100,100

WIDTH = 500
HEIGHT = 300
BACKGROUND_COLOR = (255,0,0)

def draw():
    screen.fill(BACKGROUND_COLOR)
    blob.draw()
def update():
    blob.left = blob.left + 2
    if blob.left > WIDTH:
        blob.right = 0




