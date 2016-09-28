# Created by: Matthew Lourenco
# Created on: 28 Sept 2016
# This is a program that creates a movable image

import ui
from scene import *

class FirstScene(Scene):
    def setup(self):
        #add blue background of mt crest
        self.background = SpriteNode(position = self.size / 2,
                                     color = (0.61, 0.78, 0.87),
                                     parent = self,
                                     size = self.size)
        self.school_crest = SpriteNode('./assets/sprites/school_crest.jpg',
                                       parent = self,
                                       position = self.size / 2)
    def touch_moved(self, touch):
        #move image with finger
        self.school_crest.position = touch.location

main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = FirstScene()
main_view.present(hide_title_bar = True, animated = False)
