import json

class Storage:
    def __init__(self, filename):
        self.filename =filename
        def save(self, chromosomes):
            with open(self.filename, "w") as f:
                json.dump({"chromosomes": chromosomes}, file)


    def load(self):
        try:
            with open(self.filename, "r") as file:
                data =json.load(file)
                return data["chromosomes"]
        except Exception:
                # Something went worng. Return an empty list of Chromosomes
                return []
                