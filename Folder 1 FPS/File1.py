from ursina import *

from ursina.prefabs.first_person_controller import FirstPersonController

import random



app = Ursina()

grid = Entity(model=Grid(20, 20), scale=50, color=color.white, rotation_x= 90, y=-1, collider= "box")

player = FirstPersonController(model= None, collider= "box", position=(0.5, 1, 0.5), speed= 8, jump_height= 4, gravity= 1)

start= Entity(model= "cube", scale= (2,1,2), color= color.red, collider= "box", x= 0, z= 0)

finish= Entity(model= "cube", scale= (2,1,2), color= color.green, collider= "box", x= 0, z= 20)

def create_blocks():

    global blocks, original_block_position

    blocks= []

    original_block_position= []

    z= 0

    for i in range(6):

        z += 3

        for u in range(3):

            x= random.randrange(-8, 8, 3)

            original_block_position.append((x, z))

            b = Entity(model= "cube", scale= (2, 1, 2), color= color.orange, texture= "stone.jpg", collider= "box", x=x, z=z)

            blocks.append(b)

create_blocks()

player.visible = False

water = Entity(

    model=Plane(subdivisions=(2, 8)),

    scale=50,

    color=color.white,

    texture="water.jpg",

    rotation_x=0,

    y=0.5

)

wall1= Entity(model= "cube", scale=(20, 12, 1), texture= "stone.jpg", color= color.rgb(100, 110, 120), collider= "box", x=0, z= -2, )

wall2= Entity(model= "cube", scale=(20, 12, 1), texture= "stone.jpg", color= color.rgb(100, 110, 120), collider= "box", x=0, z= 22, )

wall3= Entity(model= "cube", scale=(20, 12, 1), texture= "stone.jpg", color= color.rgb(100, 110, 120), collider= "box", x=-10, z= 10, rotation_y= 90)

wall4= Entity(model= "cube", scale=(20, 12, 1), texture= "stone.jpg", color= color.rgb(100, 110, 120), collider= "box", x=10, z= 10,rotation_y= 90 )


def update():
    # 1. Quit Game
    if held_keys["escape"]:
        application.quit()

    # 2. Lose Condition (Falling in Water)
    # Since water is at y=0.5, if player falls below y=0, they hit the water.
    if player.y < 0:
        player.position = (0.5, 5, 0.5) # Respawn at start
        print("You fell! Try again.")

    # 3. Win Condition (Distance check to finish block)
    # We check if player is close to the finish block on the X and Z plane
    dist = distance_xz(player.position, finish.position)
    if dist < 1.5:
        finish.color = color.yellow # Visual feedback
        print("YOU WIN!")
        # Optional: application.quit() or restart level




if __name__ == "__main__":

    app.run()