from torpedo import *
from asteroid import *
from spaceship import *
from gameMaster import *
from math import *


class GameRunner:

    def __init__(self, amnt = 3):
        self.game = GameMaster()
        self.screenMaxX = self.game.get_screen_max_x()
        self.screenMaxY = self.game.get_screen_max_y()
        self.screenMinX = self.game.get_screen_min_x()
        self.screenMinY = self.game.get_screen_min_y()
        shipStartX = (self.screenMaxX-self.screenMinX)/2 + self.screenMinX
        shipStartY = (self.screenMaxY-self.screenMinY)/2 + self.screenMinY
        self.game.set_initial_ship_cords( shipStartX, shipStartY )
        self.game.add_initial_astroids(amnt)

    def run(self):
        self._do_loop()
        self.game.start_game()


    def _do_loop(self):
        self.game.update_screen()
        self.game_loop()
        # Set the timer to go off again
        self.game.ontimer(self._do_loop,1)

    def game_loop(self):
        self._moveAsteroids()
        self._moveShip()
        self._addTorpedo()
        self._moveTorpedo()
        self._updateDeadTorpedos()
        self._torpedoHitsAsteroids()
        self._loseLife()
        self._finishGame()

    def _moveObject(self, some_object):
        speed_x = some_object.get_speed_x()
        speed_y = some_object.get_speed_y()
        x = some_object.get_x_cor()
        y = some_object.get_y_cor()
        max_x = self.game.get_screen_max_x()
        max_y = self.game.get_screen_max_y()
        min_x = self.game.get_screen_min_x()
        min_y = self.game.get_screen_min_y()
        newcord_x = (speed_x + x - min_x) % (max_x - min_x) + min_x
        newcord_y = (speed_y + y - min_y) % (max_y - min_y) + min_y
        some_object.move(newcord_x, newcord_y)

    def _moveAsteroids(self):
        asteroids_list = self.game.get_asteroids()
        for asteroids in asteroids_list:
            self._moveObject(asteroids)


    def _moveShip(self):
        ship = self.game.get_ship()
        left = self.game.is_left_pressed()
        right = self.game.is_right_pressed()
        up = self.game.is_up_pressed()
        if left:
            ship.increase_angle()
        if right:
            ship.decrease_angle()
        angle = ship.get_angle()
        radian = math.radians(angle)
        if up:
            speed_x = ship.get_speed_x()
            new_speed_x = speed_x + math.cos(radian)
            speed_y = ship.get_speed_y()
            new_speed_y = speed_y + math.sin(radian)
            ship.set_speed_x(new_speed_x)
            ship.set_speed_y(new_speed_y)
        self._moveObject(ship)

    def _addTorpedo(self):
        fire = self.game.is_fire_pressed()
        if fire:
            ship = self.game.get_ship()
            speed_x = ship.get_speed_x()
            speed_y = ship.get_speed_y()
            cor_x = ship.get_x_cor()
            cor_y = ship.get_y_cor()
            angle = ship.get_angle()
            radian = math.radians(angle)
            torpedo_speed_x = speed_x+2*math.cos(radian)
            torpedo_speed_y = speed_y+2*math.sin(radian)
            self.game.add_torpedo(cor_x,cor_y,torpedo_speed_x,torpedo_speed_y,angle)
        torpedo_list = self.game.get_torpedos()
        if len(torpedo_list) > 20:
            self.game.remove_torpedos([torpedo_list[0]])

    def _moveTorpedo(self):
        torpedo_list = self.game.get_torpedos()
        dead_torpedos = []
        for i in range(len(torpedo_list)):
            self._moveObject(torpedo_list[i])
   
    def _updateDeadTorpedos(self):
        torpedo_list = self.game.get_torpedos()
        remove_list = []
        for i in range(len(torpedo_list)):
            if torpedo_list[i].get_life_span() <= 0:
                remove_list.append(i)
        self._removeTorpedos(remove_list)

    def _removeTorpedos(self, listIdx):
        torpedo_list = self.game.get_torpedos()
        remove_torpedos=[]
        for i in listIdx:
            remove_torpedos.append(torpedo_list[i])
        self.game.remove_torpedos(remove_torpedos)


    def _torpedoHitsAsteroids(self):
        torpedo_list = self.game.get_torpedos()
        asteroids_list = self.game.get_asteroids()
        for torpedo in torpedo_list:
            for asteroid in asteroids_list:
                if self.game.intersect(torpedo,asteroid):
                    x = asteroid.get_x_cor()
                    y = asteroid.get_y_cor()
                    speed_x_asteroid = asteroid.get_speed_x()
                    speed_y_asteroid = asteroid.get_speed_y()
                    speed_x_torpedo = torpedo.get_speed_x()
                    speed_y_torpedo = torpedo.get_speed_y()
                    self.game.remove_torpedos([torpedo])
                    asteroid_size = asteroid.get_size()
                    if asteroid_size == 1:
                        self.game.add_to_score(100)
                        self.game.remove_asteroid(asteroid)
                    if asteroid_size == 2:
                        self.game.add_to_score(50)
                        x_speed=(speed_x_torpedo + speed_x_asteroid) / (math.sqrt(math.pow(speed_x_asteroid, 2) + math.pow(speed_x_torpedo, 2)))
                        y_speed=(speed_x_torpedo + speed_x_asteroid) / (math.sqrt(math.pow(speed_x_asteroid, 2) + math.pow(speed_x_torpedo, 2)))
                        self.game.add_asteroid(x, y, x_speed, y_speed,1)
                        self.game.add_asteroid(x, y, -x_speed, -y_speed,1)
                        self.game.remove_asteroid(asteroid)
                    if asteroid_size == 3:
                        self.game.add_to_score(20)
                        x_speed = (speed_x_torpedo + speed_x_asteroid) / (math.sqrt(math.pow(speed_x_asteroid, 2) + math.pow(speed_x_torpedo, 2)))
                        y_speed = (speed_x_torpedo + speed_x_asteroid) / (math.sqrt(math.pow(speed_x_asteroid, 2) + math.pow(speed_x_torpedo, 2)))
                        self.game.add_asteroid(x, y, x_speed, y_speed, 2)
                        self.game.add_asteroid(x, y, -x_speed, -y_speed, 2)
                        self.game.remove_asteroid(asteroid)


    def _loseLife(self):
        ship = self.game.get_ship()
        asteroid_list = self.game.get_asteroids()
        title = "You got hit!"
        msg = "You lost one life :("
        for asteroid in asteroid_list:
            if self.game.intersect(asteroid,ship):
                self.game.show_message(title,msg)
                self.game.remove_asteroid(asteroid)
                self.game.ship_down()


    def _finishGame(self):
        asteroid_list = self.game.get_asteroids()
        if self.game.get_num_lives()==0:
            self.game.show_message("You lost!", "Pathatic... Now earth is ruined")
            self.game.end_game()
            return
        if len(asteroid_list)==0:
            self.game.show_message("You won!", "Great job you destroyed all the asteroids!")
            self.game.end_game()
        if self.game.should_end():
            self.game.show_message("Bye", "See you next time!")
            self.game.end_game()






        



   

            




def main():
    runner = GameRunner()
    runner.run()

if __name__ == "__main__":
    main()
