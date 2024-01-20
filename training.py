from canvas import Canvas
from racetrack import Track
from network import Network
import os



track_image_path = os.path.join("images", "parkinglot.png")
car_image_paths =[os.path.join("images", f"car{i}.png") for i in range(5)]
canvas = Canvas(Track(1), car_image_paths)


# Network and genetic algorithm configuration

network_dimensions = 5, 4, 2 # input neurons, hidden layers neurons and output neurons

population_count = 3
networks = [Network(network_dimensions) for _ in range(population_count)]
canvas =Canvas(track_image_path, car_image_paths)

population_count =40
networks = [FirstNetwork() for _ in range(population_count)]

simulation_round =1
canvas.simulate_generation(networks, simulation_round)