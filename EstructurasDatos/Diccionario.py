dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
print(dict.keys())

for key in dict.keys():
    print(key, "->", dict[key])

print("\nSorted")
print(sorted(dict.keys()))

print("\nDict")
print(dict)