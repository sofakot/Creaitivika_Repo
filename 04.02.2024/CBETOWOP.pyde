def setup():
    size(300,300)
    background(3,249,255)
    
    fill(255,255,0)
    ellipse(50,50,100,100)
    
    fill(61,62,62)
    rect(120,20,60,160)
    
    fill(82,82,82)
    rect(0,250,500,100)
    rect(145,120,10,100)
    fill(130,131,131)
    rect(100,200,100,50)
    
def draw():
    
    if mousePressed and (mouseButton == LEFT):
        push()
        fill(255,0,0)
        ellipse(150,50,50,50)
        pop()
        ellipse(150,100,50,50)
        ellipse(150,150,50,50)
    elif mousePressed and (mouseButton == RIGHT):
        push()
        fill(3,255,12)
        ellipse(150,150,50,50)
        pop()
        ellipse(150,50,50,50)
        ellipse(150,100,50,50)
    elif mousePressed and (mouseButton == CENTER):
        push()
        fill(250,255,3)
        ellipse(150,100,50,50)
        pop()
        ellipse(150,50,50,50)
        ellipse(150,150,50,50)
    else:
        fill(255)
        ellipse(150,150,50,50)
        ellipse(150,100,50,50)
        ellipse(150,50,50,50)
