class simulation():
    POSITIONS = [
        [0, [0,0], [100,200]],
        [0, [100,2000]]
    ]
    def __init__(self) -> None:
        pass
    def step(self):
        for pos in self.POSITIONS:
            pos[0] = (pos[0] + 1) % (len(pos) - 1) 

    def get_body_positions(self):
        return [pos[pos[0] + 1] for pos in self.POSITIONS]