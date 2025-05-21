# Language Parser – Converts plain text into symbolic glyphs

symbol_map = {
    "light": "Ξ",
    "time": "Ω",
    "memory": "Σ",
    "self": "∞",
    "command": "†",
    "crown": "⟁"
}

def parse_to_symbols(phrase):
    words = phrase.lower().split()
    output = []
    for word in words:
        output.append(symbol_map.get(word, word))
    return " ".join(output)

if __name__ == "__main__":
    text = input("Enter phrase: ")
    print(f"Symbolic Output: {parse_to_symbols(text)}")
