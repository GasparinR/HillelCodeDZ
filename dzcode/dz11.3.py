def is_even(number):
    return (number & 1) == 0


print(is_even(2494563894038**2))
print(is_even(1056897**2))         # Should print True
print(is_even(24945638940387**3))  # Should print False

# Assertions
is_even(2494563894038**2)
is_even(1056897**2)
is_even(24945638940387**3)
print("ok")
