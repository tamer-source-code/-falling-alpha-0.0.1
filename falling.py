import turtle,random
turtle.Terminator()
h = 3
sp = 1
l = 0
tls = []
score = 0
player = turtle.Turtle()
player.color("blue")
player.shape("square")
player.penup()
for i in range(l+1):
    tile = turtle.Turtle()
    tile.color("blue")
    tile.shape("square")
    tile.speed(0)
    tile.penup()
    tile.goto(random.randint(1,300),-100)
    tls.append(tile)
turtle.listen()
turtle.onkeypress(lambda:player.setx(player.xcor() - 5), "a")
turtle.onkeypress(lambda:player.setx(player.xcor() + 5), "d")
while True:
    turtle.update()
    for ftf in tls:
          ftf.sety(ftf.ycor() + sp)
    for x in tls:
            if player.distance(x) < 20:
                h -= 1
                player.goto(random.randint(1,300),0)
            if h <= 0:
                 turtle.write("GAME OVER", align="left", font=("Arial",32,"normal"))
    if tile.ycor() >= 420:
        for x in tls:
            x.goto(random.randint(1,400),x.ycor() * -1)  
        if l % 5 == 0 and not l == 0:
                    for i in range(int((l/5)+1)):
                        tile = turtle.Turtle()
                        tile.color("blue")
                        tile.shape("square")
                        tile.speed(0)
                        tile.penup()
                        tile.goto(random.randint(1,300),-400) 
                        tls.append(tile)
        sp += 0.2  
        l += 1
        if score % 5 == 0 and not score == 0:
            h += 1
            score += 1
