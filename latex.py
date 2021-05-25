if __name__ == "__main__":
    pass

string = input("Enter a LaTeX string to parse:")

components = string.split('\\')

for c in components:
    if c == 'frac':
        pass

print(components)
