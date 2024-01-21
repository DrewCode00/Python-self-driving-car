class Evolution:

    def __init__(self, population_count, keep_count):
        self.population_count = population_count
        self.keep_count = keep_count
        self.networks = [Network(network_dimensions) for _ in range(population_count)]

        def execute(self, rankablle_chromosome):



            offspring =[]



            assert len(offsprong) == self.population_count, "offspriing count is  not population_count"
            return offspring_chrom