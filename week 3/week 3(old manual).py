#task 1
class ModelBasedAgent:

    def __init__(self):
        self.internal_state = {
            "ac": "off"
        }

    def perceive(self, temperature):

        if temperature > 26:
            self.internal_state["ac"] = "on"
        else:
            self.internal_state["ac"] = "off"

    def show_state(self):
        print("AC:", self.internal_state["ac"])

# Create agent
agent = ModelBasedAgent()

# Test 1
print("Temperature: 28°C")
agent.perceive(28)
agent.show_state()

# Test 2
print("\nTemperature: 24°C")
agent.perceive(24)
agent.show_state()

#task 2
class ModelBasedAgent:

    def __init__(self):
        self.internal_state = {
            "ac": "off"
        }

    def perceive(self, temperature):
        if temperature > 26:
            self.internal_state["ac"] = "off"
        else:
            self.internal_state["ac"] = "on"

        print("Temperature:", temperature, "°C -> AC",
              self.internal_state["ac"].upper())

agent = ModelBasedAgent()
temperatures = [18, 22, 25, 25, 19]

for temperature in temperatures:
    agent.perceive(temperature)