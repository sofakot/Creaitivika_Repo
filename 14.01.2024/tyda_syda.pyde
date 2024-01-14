x=0+60
mode=1
q=350-1
mode1=1
w=0+1
mode2=1
e=350-1
mode3=1


def setup():
    size(400,400)
    background(0)
    frameRate(10)
    
    
def draw():
    background(0)
    fill(0,0,0)
    stroke(random (255),random (255),random (255))
    global x,mode,q,mode1,w,mode2,e,mode3
    ellipse(x,200,50,50)
    ellipse(x,100,50,50)
    ellipse(x,300,50,50)
    
    ellipse(q,200,50,50)
    ellipse(q,100,50,50)
    ellipse(q,300,50,50)
    
    ellipse(100,w,50,50)
    ellipse(200,w,50,50)
    ellipse(300,w,50,50)
    
    ellipse(100,e,50,50)
    ellipse(200,e,50,50)
    ellipse(300,e,50,50)
    
    x=x+10*mode
    q=q-10*mode1
    w=w+11
    e=e-11
    print(x, q, w, e)
    
    if x >=350:
       mode=-1
    if x <=50:
       mode=1
    
    if q >=339:
       mode1=1
    if q <=50:
       mode1=-1
       
    if w >=350:
        w=50
        
    if e <=50:
        e=350
