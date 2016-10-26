# Created on 12 oct 2016
# Created by Matthew
# this is the game scene
# Edited on 19 oct 2016
# Edited on 26 oct 2016: created missiles that leave the spaceship

from scene import *
import ui

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size = self.size
        self.center_of_screen = self.size / 2
        self.right_button_pressed = False
        self.left_button_pressed = False
        self.speed_of_spaceship = 20.0
        self.missiles = []
        
        self.background = SpriteNode('./assets/sprites/star_background.PNG',
                                     position = self.size / 2,
                                     parent = self,
                                     size = self.size)
        
        spaceship_position = self.center_of_screen
        spaceship_position.y = 100
        self.spaceship = SpriteNode('./assets/sprites/spaceship.PNG',
                                      parent = self,
                                      position = spaceship_position)
        
        left_button_position = self.center_of_screen
        left_button_position.x = 100
        left_button_position.y = 100
        self.left_button = SpriteNode('./assets/sprites/left_button.PNG',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5)
        
        right_button_position = self.center_of_screen
        right_button_position.x = 300
        right_button_position.y = 100
        self.right_button = SpriteNode('./assets/sprites/right_button.PNG',
                                      parent = self,
                                      position = right_button_position,
                                      alpha = 0.5)
        
        red_button_position = self.size
        red_button_position.x = red_button_position.x - 100
        red_button_position.y = 100
        self.red_button = SpriteNode('./assets/sprites/red_button.PNG',
                                      parent = self,
                                      position = red_button_position,
                                      alpha = 0.5)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        if self.left_button_pressed == True:
            self.spaceship.run_action(Action.move_by(-1*self.speed_of_spaceship, 0.0, 0.1))
        if self.right_button_pressed == True:
            self.spaceship.run_action(Action.move_by(self.speed_of_spaceship, 0.0, 0.1))
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_pressed = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_pressed = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        self.right_button_pressed = False
        self.left_button_pressed = False
        
        if self.red_button.frame.contains_point(touch.location):
            self.create_new_missile()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
    def create_new_missile(self):
        #creates new missile and adds it to an array when called
        
        missile_start_position = self.spaceship.position
        missile_end_position = self.size
        missile_end_position.x = self.spaceship.position.x
        self.missiles.append(SpriteNode('./assets/sprites/missile.PNG',
                                      parent = self,
                                      position = missile_start_position))
        
        missile_move_action = Action.move_to(missile_end_position.x,
                                             missile_end_position.y + 100,
                                             3.0)
        self.missiles[len(self.missiles) - 1].run_action(missile_move_action)
