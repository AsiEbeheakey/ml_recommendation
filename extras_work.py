first_name = 'ransben'
last_name = 'barnor'
full_name = f"{first_name} {last_name}"
print(f"Happy birthday, {full_name.title()}!")
cars = ['honda', 'audi', 'toyota', 'nissan']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("Here is the orginal list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
cars.reverse()
print(cars)
