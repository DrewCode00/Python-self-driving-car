from canvas import Canvas
from racetrack import Track
from network import Network
from evolution import Evolution
from storage import Storage
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
max_generation_iterations = 50
keep_count = 4

networks = [Network(network_dimensions) for _ in range(population_count)]
evolution = Evolution(population_count, keep_count)
storage =Storage("brain.json")

best_chromosomes = storage.load()
for c, n in zip(best_chromosomes, networks):
    n.deserialize(c)



simulation_round =1
while simulation_round <= max_generation_iterations and canva.is_simulating:
    print(f"=== Round: {simulation_round} ===")
canvas.simulate_generation(networks, simulation_round)
simulation_round += 1
if canvas.is_simulation:
    print(f"-- Average Checkpoint reached:{sum(n.highest_checkpoint for n in network)/  len(networks):.2f}.")
    print(f"-- Average edge distance reached:{sum(n.smallest_edge_distance for n in networks)/ len(networks):.2f}.")
    print(f"-- Cars reached goal:{sum(n.speed for n in networks)/ len(networks):.2f}.")


    serialized = [network.serialize() for network in networks]
    offspring = evolution.execute(serialized)

    storage.save(offspring[:keep_count])  # Save the best Chromosomes

    # Create networks from offspring

    Networks =[]
    for chromosome in offspring:
        network = Network(network_dimensions)
        network.deserialize(chromosome)
        Networks.append(network)