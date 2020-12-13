# read animals.txt
# and write animals_new.txt
animals = open('animals.txt', 'r')
animals_new = open('animals_new.txt', 'w')
for animal in animals:
    animals_new.write(animal.rstrip('\n') + ' ')
animals.close()
animals_new.close()
