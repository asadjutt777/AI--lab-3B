#task 1
for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)

#task 2
movies = [
    ("Movie A", 100),
    ("Movie B", 200),
    ("Movie C", 150),
    ("Movie D", 300),
    ("Movie E", 250)
]

# Calculate total budget
total = 0

for title, budget in movies:
    total += budget

# Calculate average budget
average = total / len(movies)

print("Average budget:", average)

# Find movies above average
count = 0

for title, budget in movies:
    if budget > average:
        difference = budget - average
        print(title, "exceeds average by", difference)
        count += 1

print("Number of movies above average:", count)

#task 3
class Vehicle:
    def start_engine(self):
        print("Vehicle engine is starting")


class Car(Vehicle):
    def start_engine(self):
        print("Car engine is starting")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine is starting")

# Create objects
car = Car()
motorcycle = Motorcycle()

# Call the overridden method
car.start_engine()
motorcycle.start_engine()