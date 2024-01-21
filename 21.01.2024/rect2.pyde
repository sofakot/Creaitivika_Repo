x=50
y=50
q=0

mode="увеличить"

def setup():
    size(500,500)
    background(0)
    
def draw():
    
    global x,y,q,mode
    
    translate(250,250)
    rotate(radians(q))
    background(0)
    fill(0,0,0)
    stroke(random(255),random(255),random(255))

    q=q+1
    
    rectMode(CENTER)
    rect(0,0,x,y)
    
    if mode=="увеличить":
        x=x+1
        y=y+1
    
    if mode=="уменьшить":
        x=x-1
        y=y-1
    
    if x <= 0:
        mode = "увеличить"
        
    if x >= 400:
        mode = "уменьшить"

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
