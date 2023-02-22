import a_PlantClass as pc

primrose = pc.Plant("Green")  # Superclass instance

sunflower = pc.Flower("Yellow", 12)  # Subclass instance

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


# print(primrose.get_petals())
