class Stats:
    def __init__(self):
        self.strength = 5
        self.intelligence = 5
        self.stamina = 5
        self.energy = 3
        self.day = 1

    def perform_activity(self, area_name):
        if self.energy <= 0:
            return
        if area_name == \"Gym\": self.strength += 1
        if area_name == \"Library\": self.intelligence += 1
        if area_name == \"Dorm\": self.stamina += 1
        if area_name == \"Field\": self.stamina += 2; self.strength += 1
        self.energy -= 1

    def new_day(self):
        self.day += 1
        self.energy = 3
