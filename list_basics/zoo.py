animal_list = []
for i in range(3):
    animal_list.append(input())
animal_list[0], animal_list[2] = animal_list[2], animal_list[0]
print(animal_list)