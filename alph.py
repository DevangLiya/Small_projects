import matplotlib.pyplot as plt

name = input("Enter file:")
handle = open(name)
l = []
container = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
for line in handle :
	line = line.strip('\n ')
	l = l + list(line)
	for alph in l :
		if alph in container :
			container[alph] = container.get(alph, 0) + 1
			
plt.bar(range(len(container)), container.values(), align='center')
plt.xticks(range(len(container)), list(container.keys()))

plt.show()