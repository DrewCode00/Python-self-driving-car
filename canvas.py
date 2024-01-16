from pyglet.window import Window
from pyglet.window import key
from pyglet import image
from pyglet.graphics import Batch
from pyglet.sprite import Sprite
import time
import random
from car import Car

class Canvas(Window):
    frame_duration = 1/60

    def __init__(self, track_image_path, car_image_paths):
        super().__init__()
    self.is_simulating = True
    self.width =960
    self.height =540
    self.background_batch = Batch()
    self.cars_batch =Batch()
    self.track_image_sprite = Sprite(image.load(track_image_path), batch=self.background_batch)
    self.keyboard = key.keyStateHandler() # TODO: Remove Keyboard Control
    self.push_handlers(self.keyboard) # TODO: remove keyboard control

    def simulate_generation(self):
        self.car_sprite =[]
        self.car_sprite.append(Car(random.choice(self.car_images),self.cars_batch))

        last_time = time.perf_counter()
        while self.is_simulating:
            elapsed_time = time.perf_counter() - last_time
            if elapsed_time > self.frame_duration:
                last_time =time.perf_counter()
                self.dispatch_event()
                self.update(elapsed_time)
                self.draw()

    def update(self, delta_time):
        pass
    def draw(self):
        self.clear()
        self.background_batch.draw()
        self.cars_batch.draw()
        self.flip()


    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.is_simulating = False
            print("Simulation aborted")


