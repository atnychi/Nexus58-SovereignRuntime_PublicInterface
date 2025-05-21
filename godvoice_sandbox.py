# GODVOICE Interface (Sandbox Mode Only)
# Symbolic interpreter of spoken command simulation

def godvoice(command):
    parsed = f"🗣️ '{command}' parsed → ⟁ΞΩ∞† Command Layer"
    print(parsed)

if __name__ == "__main__":
    while True:
        user_input = input("Speak: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        godvoice(user_input)
