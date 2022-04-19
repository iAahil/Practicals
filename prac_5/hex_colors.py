COLOR_NAMES = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
               "Alizarin Crimson": "#e32636", "Amaranth": "e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
               "Apricot": "#fbceb1", "Aqua": "#00ffff", "Carnelian": "#b31b1b"}

color = input("Enter a colour name: ")
while color != "":
    print(color, "is", COLOR_NAMES.get(color))
    color = input("Enter a colour name: ")
