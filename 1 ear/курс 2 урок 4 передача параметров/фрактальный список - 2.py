def defractalize(fractal):
    while fractal in fractal:
        del fractal[fractal.index(fractal)]


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
defractalize(fractal)
print(fractal)


print()
print()


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)