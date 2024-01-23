import random
import itertools

class Evolution:

    def __init__(self, population_count, keep_count):
        self.population_count = population_count
        self.keep_count = keep_count
        self.networks = [Network(network_dimensions) for _ in range(population_count)]

        def execute(self, rankablle_chromosome):
            # selection
            sorted_chromosomes = [w.cgromosome for w in sorted(weighted_chromosomes)]
            keep_chromosommes = sorted_chromosomes[:self.keep_count]

            # Cross Over
            reproduction_times =(self.population_count - self.keep_count) / slef.keep_count
            offspring =[c for c in keep_chromosomes]
            for i in range(int(reproduction_times)):
                for c1, c2 in itertools.batched(keep_chromosomes, 2):
                    split_index =random.ranint(0, len(c1) -1)
                    offspring.append(c1[:split_index] + c2[split_index:])
                    offspring.append(c1[split_index] + c1[split_index])

                    # Mutations
            for chromosome in offspring[self.keep_count:]:
                for i in range(len(chromosome)):
                    if random.randint(0,4) == 1:
                        chromosome[i] = random.random() * 2 -1

            assert len(offsprong) == self.population_count, "offspriing count is  not population_count"
            return offspring