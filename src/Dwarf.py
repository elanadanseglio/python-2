from Character import Character

class Dwarf(Character):
    def __repr__(self):
        return f"Dwarf: {self.hit_points} hit points."