class Pet:
    def __init__(self, name: str, hunger: int, energy: int, hapiness: int):  
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(hunger, int) or not (max(0, min(hunger, 10))):
            raise ValueError("Hunger must be an integer between 0 and 10")
        if not isinstance(energy, int) or not (max(0, min(energy, 10))):
            raise ValueError("Energy must be an integer between 0 and 10")
        if not isinstance(hapiness, int) or not (max(0, min(hapiness, 10))):
            raise ValueError("Hapiness must be an integer between 0 and 10")
        
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.hapiness = hapiness
        self.tricks = []

    def get_hunger_level(hunger) -> str:
        hunger_level = {
            0: "full",
            1: "almost full",
            2: "almost full",
            3: "almost full",
            4: "almost full",
            5: "almost full",
            6: "hungry",
            7: "hungry",
            8: "hungry",
            9: "hungry",
            10: "very hungry"
        }

        return hunger_level.get(hunger, "unknown")
    
    def get_energy_level(energy) -> str:
        energy_level = {
            0: "tired",
            1: "almost tired",
            2: "almost tired",
            3: "almost tired",
            4: "almost tired",
            5: "rested",
            6: "rested",
            7: "rested",
            8: "rested",
            9: "rested",
            10: "fully rested"
        }

        return energy_level.get(energy, "unknown")
    
    def get_hapiness_level(hapiness) -> str:
        hapiness_level = {
            0: "sad",
            1: "almost sad",
            2: "almost sad",
            3: "almost sad",
            4: "almost sad",
            5: "happy",
            6: "happy",
            7: "happy",
            8: "happy",
            9: "happy",
            10: "very happy"
        }
        return hapiness_level.get(hapiness, "unknown")

    def eat(self):
        hunger_level = self.get_hunger_level(self.hunger + 3)
        hapiness_level = self.get_hapiness_level(self.hapiness - 1)
        return f"{self.name} is eating and is now {hunger_level} and {hapiness_level}."
    
    def sleep(self):
        energy_level = self.get_energy_level(self.energy + 5)
        return f"{self.name} is sleeping. Energy level is now {energy_level}."
    
    def playing(self):
        energy_level = self.get_energy_level(self.energy - 2)
        hapiness_level = self.get_hapiness_level(self.hapiness + 2)
        hunger_level = self.get_hunger_level(self.hunger + 1)
        return f"{self.name} is playing. Energy level is now {energy_level}, hapiness level is now {hapiness_level}, and hunger level is now {hunger_level}."
  
    def get_status(self):
        return f"{self.name}'s current status:\n" \
               f"Hunger: {self.hunger}\n" \
               f"Energy: {self.energy}\n" \
               f"Happiness: {self.hapiness}"
    
    def train(self, trick: str):
        if not isinstance(trick, str):
            raise TypeError("Trick must be a string")
        self.tricks.append(trick)
        return f"{self.name} has learned a new trick: {trick}!"
    
    def show_tricks(self):
        if not self.tricks:
            return f"{self.name} has not learned any tricks yet."
        return f"Tricks: {self.tricks}"