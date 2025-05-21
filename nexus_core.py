# Nexus Core Shell (Public Interface)
# Symbolic Recursive System Framework

class NexusCore:
    def __init__(self):
        self.state = "Symbolic Runtime Initialized"
        self.memory = []

    def input_signal(self, data):
        symbolic = f"⟁→ {data}"
        self.memory.append(symbolic)
        return symbolic

    def get_state(self):
        return self.state

    def dump_memory(self):
        return self.memory
