### **README.md**  
# Python Scripts Collection

This repository contains basic Python scripts to demonstrate fundamental programming concepts. Each script includes instructions on how to run it.
```
## **Scripts Included**
1. `game_over.py` - Displays a "Game over" message.  
2. `salary_calculation.py` - Calculates new salary after a pay raise.  
3. `string_concatenation.py` - Combines two words to form a single string.  
4. `check_data_type.py` - Displays the data type of a user input.  
5. `convert_int_to_float.py` - Converts an integer to a floating-point number.  
6. `hello_loop.py` - Prints "Hello" multiple times.  
7. `short_hello_loop.py` - Prints "Hello" a few times.  
8. `sell_tickets.py` - Simulates selling tickets.  
9. `counter_loop.py` - Prints numbers using a `while` loop.  
10. `password_check.py` - Checks if a guessed password is incorrect.  
11. `password_loop.py` - Repeatedly asks for the correct password until entered.  
12. `age_discount.py` - Determines if a person gets a discount based on age.  
13. `senior_discount.py` - Determines if a person qualifies for a junior or senior discount before proceeding to payment.  
14. `games_list.py` - Stores a list of games in an array.  
15. `animals_list.py` - Stores a list of animals in an array and prints a specific one.  
16. `product_list.py` - Modifies a product list by replacing an item.  
17. `list_slicing.py` - Demonstrates list slicing and indexing.  
18. `string_operations.py` - Demonstrates string slicing and concatenation.  
19. `list_modification.py` - Modifies lists by replacing and inserting elements.  
20. `string_methods.py` - Uses string methods like `find()` and `len()`.  
21. `list_methods.py` - Demonstrates list methods like `append()`, `insert()`, and `pop()`.  
22. `functions_basics.py` - Defines functions with and without parameters.  
23. `bmi_calculation.py` - Computes BMI and returns values for further operations.  
24. `rectangle_properties.py` - Computes area, perimeter, and price of a rectangle.  
25. `currency_symbols.py` - Demonstrates list slicing and modifying currency symbols.  
26. `vehicles.py` - Demonstrates string slicing and string immutability.  
27. `list_slicing_examples.py` - Demonstrates different list slicing techniques.  

---
```

### **How to Run the Scripts**
### **1. Clone the Repository**
If you haven’t already cloned this repository, run:
```bash
git clone https://github.com/kenbrew96/game-over-message.git
cd game-over-message
```
### **2. Run a Python Script**
To execute any of the scripts, use the following command:
```bash
python script_name.py
```
For example, to run the `game_over.py` script:
```bash
python game_over.py
```

### **3. Add a New Script**
If you want to add a new script:
1. Create a new Python file, e.g., `new_script.py`
2. Write your Python code in the file.
3. Save and track the file in Git:
   ```bash
   git add new_script.py
   git commit -m "Added new_script.py"
   git push origin main
   ```

### **4. Updating the Repository**
If you modify an existing script, commit and push the changes:
```bash
git add .
git commit -m "Updated scripts"
git push origin main
```

---
## Scripts

### **1. List Slicing (`list_slicing.py`)**
```python
animals = ['cat', 'dog', 'bird', 'cow']
print(animals[2:4])
```

### **2. String Slicing (`string_slicing.py`)**
```python
vehicle = 'motorbike'
print(vehicle[:5])
```

### **3. List Slicing (`list_slicing_cart.py`)**
```python
cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[2:])
```

### **4. List Negative Indexing (`list_negative_index.py`)**
```python
c = ['$', '£', '€', '¥']
print(c[0:-2])
```

### **5. List Modification (`list_modify.py`)**
```python
c = ['$', '£', '€', '¥']
c[1] = '₣'
print(c)
```

### **6. String Immutability Error (`string_immutable_error.py`)**
```python
vehicle = 'airplane'
vehicle[:3] = 'water'  # This will cause an error because strings are immutable
print(vehicle)
```

### **7. String Concatenation (`string_concat.py`)**
```python
x = "air"
y = "plane"
print(x + y)
```

### **8. Finding a Character (`string_find.py`)**
```python
print("robot".find("t"))
```

### **9. String Length (`string_length.py`)**
```python
movie = "Avatar"
print(len(movie))
```

### **10. List Append (`list_append.py`)**
```python
movies = ["Avatar", "Titanic", "Avengers"]
movies.append("Alien")
print(movies[3])
```

### **11. List Insertion and Appending (`list_insert_append.py`)**
```python
colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])
```

### **12. Removing an Item from a List (`list_pop.py`)**
```python
topic = ["Maths", "English", "Physics"]
topic.pop(2)
print(topic)
```

### **13. Simple Function (`function_greet.py`)**
```python
def greet():
    print("Hello from a function")
    print("Have a great day")

greet()
```

### **14. BMI Calculation (`function_bmi.py`)**
```python
def bmi(weight, height):
    index = weight / (height * height)
    print(index)

bmi(79, 1.73)
```

### **15. BMI with Return Value (`function_bmi_return.py`)**
```python
def bmi(weight, height):
    index = weight / (height * height)
    return index

p6 = bmi(79, 1.73)
print(p6 < 18.5)
```

### **16. Rectangle Calculation (`function_rectangle.py`)**
```python
def rect(d1, d2):
    area = d1 * d2
    perimeter = 2 * d1 + 2 * d2
    price = 1000 * area
    return area, perimeter, price
```

### **17. Function with Default Parameter (`function_greet_default.py`)**
```python
def greet(name="Guest"):
    print("Welcome", name)

greet()
```

### **18. Function with Argument (`function_greet_argument.py`)**
```python
def greet(name="Guest"):
    print("Welcome", name)

greet("Anna")
```

### **19. Inserting Item at Beginning of List (`list_insert_first.py`)**
```python
colors = ["Red", "Blue", "Yellow"]
colors.insert(0, "Green")
print(colors)
```

### **20. Multiplication Function (`function_multiply.py`)**
```python
def multiply(a, b):
    return a * b

print(multiply(5, 3))
```

### **21. List Sorting (`list_sort.py`)**
```python
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)
```

### **22. Checking if Item Exists (`list_check.py`)**
```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
```

### **23. Removing Item by Value (`list_remove.py`)**
```python
colors = ["Red", "Blue", "Yellow", "Green"]
colors.remove("Blue")
print(colors)
```

### **24. Dictionary Operations (`dict_operations.py`)**
```python
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])
```
```

---
```
### **License**
This project is open-source. Feel free to use and modify the scripts.
```
