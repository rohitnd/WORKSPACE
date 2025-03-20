x = ["Now", "we", "are", "cooking!"]
print(x)
print(len(x))
print("are" in x)
print("Today" in x)
print(x[0])
print(x[3])
print(x[1:3])
print(x[2:])
print(x[:2])
print(" ".join(x))

fruits = ["Peach", "Banana", " Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits.remove("Peach")
print(fruits)

fruits.insert(0,"Orange")
print(fruits)

fruits.pop(3)
fruits[2] = "Pear"
print(fruits)

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
print("The total characters: {} and the Average length: {:.2f}".format(chars, chars/len(animal)))

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


losers = ["Freebu", "Ganes", "Tommy"]
for index, person in enumerate(losers):
    print("{} - {}".format(index + 1, person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@gmail.com", "Alex Diego")]))
