class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"

        send = target != self.previous_mode
        self.previous_mode = target
        return target, send

agent = ClassroomAgent()
percepts = [(29, True), (29, True), (20, True),
 (26, True), (19, True), (29, False)]

for step, percept in enumerate(percepts, 1):
 print(step, percept, "target mode", agent.act(*percept))