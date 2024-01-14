x=600

def setup():
    size(400,400)
    background(0)
    
def draw():
    
    stroke(random (255),random (255),random (255))
    fill(0,0,0)
    global x
    ellipse(200,200,x,x)
    x=x-1
    print("hello")
    if x==0:
        noLoop()
