blob = Actor('character')
bloboc = Actor('character_clicked')
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

def on_mouse_down(pos):
    if blob.collidepoint(pos):
        set_blob_hurt()

def set_blob_hurt():
    blob.image = 'character_clicked'
    sounds.ouch.play()
    clock.schedule_unique(set_blob_normal, 1.0)


def set_blob_normal():
    blob.image = 'character'





