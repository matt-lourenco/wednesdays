# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows a main menu screen
# Edited by: Matthew Lourenco
# Edited on: 12 Oct 2016
# Added help and game scenes as well as buttons for navigation

from scene import *
import ui

from help_scene import *
from game_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.background = SpriteNode(position = self.size / 2,
                                     color = 'white',
                                     parent = self,
                                     size = self.size)
        self.start_button = SpriteNode('./assets/sprites/start_button.PNG',
                                       parent = self,
                                       position = self.size / 2)
                                       
        help_button_position = self.size / 2
        help_button_position.y = help_button_position.y - 150
        self.help_button = SpriteNode('./assets/sprites/help_button.PNG',
                                      parent = self,
                                      position = help_button_position)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
        
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
    
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
