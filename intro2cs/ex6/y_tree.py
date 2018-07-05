def draw_tree(length):
    import turtle
    turtle.up()
    if (length<10):
        break        
    turtle.right(30)
    turtle.down()
    turtle.forward(length*0.6)
    draw_tree(length*0.6)
    turtle.backward(length*0.6)
    turtle.left(60)
    turtle.forward(length*0.6)
    draw_tree(length*0.6)
    turtle.backward(length*0.6)
    turn.right(30)
    turtle.backward(length)
    
    
    
    
    
