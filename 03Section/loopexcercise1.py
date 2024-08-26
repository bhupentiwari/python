import random;
# Create a program that asks user for 8 names of people and store them in a list.
# When all the names have been given , pick a random one and print it

people = []

for p in range(0,8) :
    person = input("Type person name :")
    people.append(person)

random_person = random.randint(0,7)

print("Random person name:",people[random_person])

