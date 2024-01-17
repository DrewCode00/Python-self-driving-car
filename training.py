from canvas import Canvas
from racetrack import Track
import os



track_image_path = os.path.join("images", "parkinglot.png")
car_image_paths =[os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(), car_image_paths)


canvas =Canvas(track_image_path, car_image_paths)

canvas.simulate_generation()