import pyglet
import os
import sys

os.chdir(os.path.dirname(__file__))

from DataTypes.LeapFrog import LeapFrog_Gravity_Sim
from DataTypes.gravitational_object import MassObject
import Tests

class GUI():
    def __init__(self, width, height, simulation) -> None:
        self.window = pyglet.window.Window(width, height, "Gravity Sim")
        self.scale = 0
        self.pixel_size = 0
        self.screen_center = [width // 2, height // 2]
        self.sim = simulation
        self.window.push_handlers(
            on_mouse_scroll=self.on_mouse_scroll,
            on_mouse_drag=self.on_mouse_drag
        )
        self.predict = True
        self.calc_init_pixel_size(width, height, self.sim.get_body_positions())
        pyglet.clock.schedule_interval(self.update, 1/60)  # Update at 60Hz

    def calc_init_pixel_size(self, width, height, positions):
        max_y = 0
        max_x = 0
        for pos in positions:
            x, y = pos
            max_x = max(abs(x), max_x)
            max_y = max(abs(y), max_y)

        factor_x = max_x / (width // 2)
        factor_y = max_y / (height // 2)

        factor = max(factor_x, factor_y)
        self.pixel_size = factor * 1.5

    def calc_screen_coords(self, x, y):
        x = (x // self.pixel_size) + self.screen_center[0]
        y = (y // self.pixel_size) + self.screen_center[1]
        return x, y

    def draw(self):
        batch = pyglet.graphics.Batch()
        positions = self.sim.get_body_positions()
        objects = []

        for pos in positions:
            x, y = pos
            x, y = self.calc_screen_coords(x, y)
            obj = pyglet.shapes.Circle(x, y, 5, color=(0, 0, 0), batch=batch)
            objects.append(obj)

        if self.predict:
            positions = self.sim.predict(1000, 1)
            for body in positions:
                body = [[int((x // self.pixel_size) + self.screen_center[0]),
                         int((y // self.pixel_size) + self.screen_center[1])]
                          for x, y in body]
                obj = pyglet.shapes.MultiLine(*body, color=(100,100,100), batch=batch)
                objects.append(obj)

        pyglet.gl.glClearColor(1, 1, 1, 1.0)  # RGB values between 0 and 1
        self.window.clear()
        batch.draw()

    def step_physics(self, dt):
        self.sim.step()

    def update(self, dt):
        self.draw()
        self.step_physics(dt)

    def zoom(self, scale_factor):
        scale_factor = 1.1 ** (-scale_factor)
        self.pixel_size *= scale_factor

    def move(self, x, y):
        self.screen_center[0] += x
        self.screen_center[1] += y

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if scroll_y > 0:
            self.zoom(1)
        elif scroll_y < 0:
            self.zoom(-1)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.move(dx, dy)

STEP_SIZE = 1
W = 400
H = 600

bodies = [
    {"m": 1.898e30, "r": 2, "v": [0, 0], "pos": [0, 0]},
    {"m": 5.9772e24, "r": 2, "v": [29.78, 0], "pos": [0, 149600000000]}

]

mass_bodies = []
for body in bodies:
    mass_bodies.append(MassObject(body["m"], body["r"], body["v"], body["pos"]))

sim = LeapFrog_Gravity_Sim(mass_bodies, STEP_SIZE)

gui = GUI(W, H, sim)

pyglet.app.run()
