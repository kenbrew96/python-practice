### **README.md**  

```markdown
# Python Scripts Collection

This repository contains basic Python scripts to demonstrate fundamental programming concepts. Each script includes instructions on how to run it.

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

---

## **How to Run the Scripts**
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

## **New Scripts Added**

### `list_slicing.py`
```python
animals = ['cat', 'dog', 'bird', 'cow']
print(animals[2:4])
```
*Slices the list to print ['bird', 'cow'].*

### `string_operations.py`
```python
vehicle = 'motorbike'
print(vehicle[:5])

x = "air"
y = "plane"
print(x + y)
```
*Slices and concatenates strings.*

### `list_modification.py`
```python
cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[2:])

c = ['$', '£', '€', '¥']
print(c[0:-2])

c[1] = '₣'
print(c)
```
*Demonstrates modifying lists by slicing and replacing elements.*

### `string_methods.py`
```python
print("robot".find("t"))
movie = "Avatar"
print(len(movie))
```
*Uses `find()` to locate a character and `len()` to determine string length.*

### `list_methods.py`
```python
movies = ["Avatar", "Titanic", "Avengers"]
movies.append("Alien")
print(movies[3])

colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])

colors.insert(0, "Green")
print(colors)

topic = ["Maths","English","Physics"]
topic.pop(2)
print(topic)
```
*Demonstrates list methods like `append()`, `insert()`, and `pop()`.*

### `functions_basics.py`
```python
def greet():
    print("Hello from a function")
    print("Have a great day")

greet()
```
*Defines and calls a function.*

### `bmi_calculation.py`
```python
def bmi(weight, height):
    index = weight / (height * height)
    return index

p6 = bmi(79, 1.73)
print(p6 < 18.5)
```
*Calculates BMI and returns the value for further operations.*

### `rectangle_properties.py`
```python
def rect(d1, d2):
    area = d1 * d2
    perimeter = 2 * d1 + 2 * d2
    price = 1000 * area
    return area, perimeter, price
```
*Computes area, perimeter, and price of a rectangle.*

### **License**
This project is open-source. Feel free to use and modify the scripts.
```
*Determines if a person qualifies for a junior or senior discount before proceeding to payment.*

---

### **License**
This project is open-source. Feel free to use and modify the scripts.
