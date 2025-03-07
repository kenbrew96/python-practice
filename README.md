# Python Scripts Collection

## Description
This repository contains various Python scripts demonstrating fundamental programming concepts, including loops, conditionals, functions, list operations, string manipulations, and user input handling.

## List of Scripts

### **1. age_discount.py**
Calculates and applies discounts based on user age.

### **2. bmi_calculation.py**
Computes the Body Mass Index (BMI) using weight and height inputs.

### **3. concatenate_words.py**
Concatenates two user-input words and prints the result.

### **4. counter_loop.py**
Demonstrates a while loop counting from 1 to 5.

### **5. currency_symbols.py**
Stores and prints a list of different currency symbols.

### **6. functions_basics.py**
Defines and calls a simple function that prints a greeting.

### **7. game_over.py**
Prints "Game Over" to the console.

### **8. hello_loop.py**
Uses a for-loop to print "Hello" multiple times.

### **9. input_type.py**
Takes user input and prints its data type.

### **10. list_append.py**
Demonstrates appending elements to a list.

### **11. list_insert_append.py**
Illustrates inserting and appending elements in a list.

### **12. list_methods.py**
Uses list methods like append, insert, and pop.

### **13. list_modify.py**
Modifies an element in a list by index.

### **14. list_negative_index.py**
Demonstrates accessing list elements using negative indexing.

### **15. list_pop.py**
Shows how to remove the last item from a list using pop().

### **16. list_slicing_cart.py**
Performs list slicing operations on a shopping cart list.

### **17. list_slicing_examples.py**
Examples of list slicing operations.

### **18. password_check.py**
Prompts the user for a password and verifies it.

### **19. password_loop.py**
Continuously prompts for a password until the correct one is entered.

### **20. print_type.py**
Prints the data type of a given input value.

### **21. rectangle_properties.py**
Calculates and prints the area and perimeter of a rectangle.

### **22. salary_calculator.py**
Calculates a new salary based on a percentage increase.

### **23. sell_tickets.py**
Simulates selling tickets using a while loop.

### **24. senior_discount.py**
Determines if a user qualifies for a senior citizen discount.

### **25. short_hello_loop.py**
Prints "Hello" three times using a loop.

### **26. string_concat.py**
Concatenates two predefined strings.

### **27. string_find.py**
Finds and prints the index of a substring within a string.

### **28. string_immutable_error.py**
Demonstrates immutability of strings in Python.

### **29. string_length.py**
Computes and prints the length of a given string.

### **30. string_methods.py**
Demonstrates common string methods such as find() and len().

### **31. string_slicing.py**
Performs slicing operations on a string.

### **32. vehicles.py**
Stores vehicle names in a list and prints selected elements.

## Usage
Clone this repository and run any script using:
```
python script_name.py
```

## Author
Kenneth Brewer

---
Let me know if you need any modifications!


```
Here are all the scripts you requested:  

---

### **1. age_discount.py**  
```python
age = int(input("Enter your age: "))
if age < 18:
    print("You get a discount!")
else:
    print("No discount available.")
```

---

### **2. bmi_calculation.py**  
```python
def bmi(weight, height):
    index = weight / (height * height)
    return index

p6 = bmi(79, 1.73)
print(p6 < 18.5)
```

---

### **3. concatenate_words.py**  
```python
x = "air"
y = "plane"
print(x + y)
```

---

### **4. counter_loop.py**  
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### **5. currency_symbols.py**  
```python
c = ['$', '£', '€', '¥']
print(c[0:-2])
```

---

### **6. functions_basics.py**  
```python
def greet():
    print("Hello from a function")
    print("Have a great day")

greet()
```

---

### **7. game_over.py**  
```python
print("Game Over!")
```

---

### **8. hello_loop.py**  
```python
for _ in range(10):
    print("Hello")
```

---

### **9. input_type.py**  
```python
user_input = input("Enter something: ")
print("Data type:", type(user_input))
```

---

### **10. list_append.py**  
```python
movies = ["Avatar", "Titanic", "Avengers"]
movies.append("Alien")
print(movies[3])
```

---

### **11. list_insert_append.py**  
```python
colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])
```

---

### **12. list_methods.py**  
```python
topic = ["Maths", "English", "Physics"]
topic.pop(2)
print(topic)
```

---

### **13. list_modify.py**  
```python
c = ['$', '£', '€', '¥']
c[1] = '₣'
print(c)
```

---

### **14. list_negative_index.py**  
```python
cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[2:])
```

---

### **15. list_pop.py**  
```python
topic = ["Maths", "English", "Physics"]
topic.pop(2)
print(topic)
```

---

### **16. list_slicing_cart.py**  
```python
cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[2:])
```

---

### **17. list_slicing_examples.py**  
```python
animals = ['cat', 'dog', 'bird', 'cow']
print(animals[2:4])
```

---

### **18. password_check.py**  
```python
password = "secret"
guess = input("Enter the password: ")

if guess != password:
    print("Incorrect password!")
```

---

### **19. password_loop.py**  
```python
password = "secret"
while True:
    guess = input("Enter the password: ")
    if guess == password:
        print("Access granted!")
        break
    print("Incorrect, try again.")
```

---

### **20. print_type.py**  
```python
data = input("Enter something: ")
print("Data type:", type(data))
```

---

### **21. rectangle_properties.py**  
```python
def rect(d1, d2):
    area = d1 * d2
    perimeter = 2 * (d1 + d2)
    price = 1000 * area
    return area, perimeter, price
```

---

### **22. salary_calculator.py**  
```python
salary = float(input("Enter your salary: "))
raise_percent = float(input("Enter the raise percentage: "))
new_salary = salary + (salary * (raise_percent / 100))
print("New salary:", new_salary)
```

---

### **23. sell_tickets.py**  
```python
tickets = 5
while tickets > 0:
    print("Selling a ticket...")
    tickets -= 1
print("Tickets sold out!")
```

---

### **24. senior_discount.py**  
```python
age = int(input("Enter your age: "))
if age < 18:
    print("You get a junior discount!")
elif age >= 60:
    print("You get a senior discount!")
else:
    print("No discount available.")
```

---

### **25. short_hello_loop.py**  
```python
for _ in range(3):
    print("Hello")
```

---

### **26. string_concat.py**  
```python
x = "Hello"
y = "World"
print(x + " " + y)
```

---

### **27. string_find.py**  
```python
print("robot".find("t"))
```

---

### **28. string_immutable_error.py**  
```python
vehicle = 'airplane'
vehicle[:3] = 'water'  # This will cause an error because strings are immutable
print(vehicle)
```

---

### **29. string_length.py**  
```python
movie = "Avatar"
print(len(movie))
```

---

### **30. string_methods.py**  
```python
movie = "Avatar"
print(movie.upper())
print(movie.lower())
print(movie.replace("A", "X"))
```

---

### **31. string_slicing.py**  
```python
vehicle = "motorbike"
print(vehicle[:5])
```

---

### **32. vehicles.py**  
```python
vehicles = ["Car", "Bike", "Truck"]
print(vehicles)
```

---

These are all the scripts currently in the collection. Let me know if you need any modifications or additions!
---

### **License**
This project is open-source. Feel free to use and modify the scripts.

