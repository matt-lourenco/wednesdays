# Created on 12 oct 2016
# Created by Matthew
# this is the game scene
# Edited on 19 oct 2016
# Edited on 26 oct 2016: created missiles that leave the spaceship
# Edited on 2 Nov 2016: added aliens that move towards the bottom of the screen
# Edited on 16 Nov 2016: made spaceship dissapear when touched by alien

from scene import *
import ui
from numpy import random
from copy import deepcopy

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen = deepcopy(self.size)
        self.center_of_screen = deepcopy(self.size) / 2
        self.right_button_pressed = False
        self.left_button_pressed = False
        self.speed_of_spaceship = 20.0
        self.missiles = []
        self.aliens = []
        self.alien_attack_rate = 1
        self.alien_attack_speed = 20.0
        self.scale_of_object = 0.75
        
        self.background = SpriteNode('./assets/sprites/star_background.PNG',
                                     position = self.size / 2,
                                     parent = self,
                                     size = self.size)
        
        spaceship_position = deepcopy(self.center_of_screen)
        spaceship_position.y = 100
        self.spaceship = SpriteNode('./assets/sprites/spaceship.PNG',
                                      parent = self,
                                      position = spaceship_position,
                                      scale = self.scale_of_object)
        
        left_button_position = deepcopy(self.center_of_screen)
        left_button_position.x = 100
        left_button_position.y = 100
        self.left_button = SpriteNode('./assets/sprites/left_button.PNG',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5,
                                      scale = self.scale_of_object)
        
        right_button_position = deepcopy(self.center_of_screen)
        right_button_position.x = 250
        right_button_position.y = 100
        self.right_button = SpriteNode('./assets/sprites/right_button.PNG',
                                      parent = self,
                                      position = right_button_position,
                                      alpha = 0.5,
                                      scale = self.scale_of_object)
        
        red_button_position = deepcopy(self.size_of_screen)
        red_button_position.x = red_button_position.x - 100
        red_button_position.y = 100
        self.red_button = SpriteNode('./assets/sprites/red_button.PNG',
                                      parent = self,
                                      position = red_button_position,
                                      alpha = 0.5,
                                      scale = self.scale_of_object)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        if self.left_button_pressed == True:
            self.spaceship.run_action(Action.move_by(-1*self.speed_of_spaceship, 0.0, 0.1))
        if self.right_button_pressed == True:
            self.spaceship.run_action(Action.move_by(self.speed_of_spaceship, 0.0, 0.1))
        
        # This should create an alien every 1/60 to 2 seconds
        alien_create_chance = random.randint(1, 120)
        if alien_create_chance <= self.alien_attack_rate:
            self.add_alien()
        
        for missile in self.missiles:
            if missile.position.y > self.size_of_screen.y + 100:
                missile.remove_from_parent()
                self.missiles.remove(missile)
        
        for alien in self.aliens:
            if alien.position.y < - 100:
                alien.remove_from_parent()
                self.aliens.remove(alien)
        
        if len(self.missiles) > 0 and len(self.aliens) > 0:
            for missile in self.missiles:
                for alien in self.aliens:
                    if alien.frame.contains_rect(missile.frame):
                        missile.remove_from_parent()
                        self.missiles.remove(missile)
                        alien.remove_from_parent()
                        self.aliens.remove(alien)
        
        for alien_hit in self.aliens:
            if alien_hit.frame.intersects(self.spaceship.frame):
                self.spaceship.remove_from_parent()
                alien_hit.remove_from_parent()
                self.aliens.remove(alien_hit)
    
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
        missile_end_position = deepcopy(self.size_of_screen)
        missile_end_position.x = self.spaceship.position.x
        self.missiles.append(SpriteNode('./assets/sprites/missile.PNG',
                                      parent = self,
                                      position = missile_start_position,
                                      scale = self.scale_of_object))
        
        missile_move_action = Action.move_to(missile_end_position.x,
                                             missile_end_position.y + 100,
                                             3.0)
        self.missiles[len(self.missiles) - 1].run_action(missile_move_action)
    
    def add_alien(self):
        # When this is called it creates a ned alien
        
        alien_start_position = deepcopy(self.size_of_screen)
        alien_start_position.x = random.randint(100, alien_start_position.x - 100)
        alien_start_position.y = alien_start_position.y + 100
        
        alien_end_position = deepcopy(self.size_of_screen)
        alien_end_position.x = random.randint(100, alien_end_position.x - 100)
        alien_end_position.y = -100
        
        self.aliens.append(SpriteNode('./assets/sprites/alien.PNG',
                                      parent = self,
                                      position = alien_start_position))
        
        alien_move_action = Action.move_to(alien_end_position.x,
                                           alien_end_position.y,
                                           self.alien_attack_speed,
                                           TIMING_SINODIAL)
        
        self.aliens[len(self.aliens) - 1].run_action(alien_move_action)
