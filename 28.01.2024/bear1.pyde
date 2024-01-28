angle=0

def setup():
    size(1000,1000)
    background(255,152,219)
    fill(152,252,255)
    stroke(152,252,255)
    ellipse(100,100,600,600)
    stroke(160,255,152)
    fill(160,255,152)
    rect(600,100,200,200)
    stroke(170,152,255)
    fill(170,152,255)
    ellipse(200,600,200,200)
    stroke(255,152,152)
    fill(255,152,152)
    rect(500,500,500,500)
    
    "мишка" 
    
    stroke(0,0,0)
    fill(209,106,38)
    ellipse(500,500,200,300)
    fill(165,72,13)
    ellipse(500,400,120,100)
    fill(250,162,162)
    ellipse(500,500,100,200)
    fill(88,36,4)
    ellipse(430,610,100,100)
    ellipse(540,610,100,100)
    fill(209,106,38)
    ellipse(420,620,100,100)
    ellipse(550,620,100,100)
    
    noStroke()
    fill(183,85,28)
    ellipse(420,620,70,70)
    ellipse(550,620,70,70)
    
    
    "голова"
    
    stroke(0,0,0)
    fill(165,72,13)
    ellipse(420,250,100,100)
    fill(165,72,13)
    ellipse(580,250,100,100)
    fill(250,162,162)
    ellipse(430,260,80,80)
    fill(250,162,162)
    ellipse(570,260,80,80)
    fill(209,106,38)
    ellipse(500,300,200,200)
    
    "глаза"
    
    fill(0,0,0)
    ellipse(450,300,50,50)
    ellipse(540,300,50,50)
    fill(88,36,4)
    ellipse(450,300,30,30)
    ellipse(540,300,30,30)
    stroke(255,255,255)
    fill(255,255,255)
    ellipse(445,295,10,10)
    ellipse(460,310,10,10)
    ellipse(530,295,10,10)
    ellipse(545,310,10,10)
    
    "нос"
    
    stroke(0,0,0)
    fill(0,0,0)
    ellipse(480,350,30,30)
    
    "рот"
    
    fill(88,36,4)
    ellipse(520,370,20,20)
    stroke(209,106,38)
    fill(209,106,38)
    ellipse(525,380,30,30)
    
    "брови"
    
    stroke(88,36,4)
    fill(88,36,4)
    ellipse(450,250,20,20)
    noStroke()
    fill(209,106,38)
    ellipse(443,245,30,30)
    fill(88,36,4)
    ellipse(530,250,20,20)
    fill(209,106,38)
    ellipse(540,245,30,30)
    
def draw():
    
    global angle
    
    "лапы"
    push()
    noStroke()
    ellipseMode(CORNER)
    translate(550,420)
    rotate(radians(angle))
    ellipse(0,0,70,200)
    pop()
    
    angle=angle+1
