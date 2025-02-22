Got it! Here are the instructions for uploading each script to GitHub, as well as updating the **README.md** file:

### **Instructions for Uploading Each Script to GitHub**

1. **Ensure You’re in Your Project Directory**  
   If you haven’t already, navigate to the project folder:
   ```bash
   cd path_to_your_project
   ```

2. **Create the New Script**  
   Add your new script to the project directory, e.g., `hello_loop.py`, and write the code.

3. **Track the Script with Git**  
   Stage the script for commit:
   ```bash
   git add hello_loop.py
   ```

4. **Commit the Changes**  
   Add a commit message to describe what you’ve added:
   ```bash
   git commit -m "Added hello_loop.py script"
   ```

5. **Push to GitHub**  
   Push the changes to your repository on GitHub:
   ```bash
   git push origin main
   ```

6. **Update the README.md File**  
   - Open the `README.md` file in a text editor.
   - Add the new script under the **Scripts Included** section.
   - Add a description and the code for the new script under **Script Details**.
   - Save and commit the changes:
     ```bash
     git add README.md
     git commit -m "Updated README.md with hello_loop.py"
     git push origin main
     ```

---
Here's your updated **README.md** with script #6 added:

---

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
6. `hello_loop.py` - Prints "Hello" 100 times.

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

## **Script Details**
### `game_over.py`
```python
message = "Game over"
print(message)
```
*Displays "Game over" on the screen.*

---

### `salary_calculation.py`
```python
salary = 1000
pay_raise = 100
new_salary = salary + pay_raise
print(new_salary)
```
*Calculates the new salary after a pay raise.*

---

### `string_concatenation.py`
```python
a = "basket"
b = "ball"
print(a + b)
```
*Concatenates two strings to form "basketball".*

---

### `check_data_type.py`
```python
birth_year = input("Enter your birth year: ")
print(type(birth_year))
```
*Displays the data type of the input (which is always a string unless converted).*

---

### `convert_int_to_float.py`
```python
a = 3
b = float(a)
print(b)
```
*Converts an integer (`3`) into a floating-point number (`3.0`).*

---

### `hello_loop.py`
```python
for i in range(100):
  print("Hello")
```
*Prints "Hello" 100 times.*

---

### **License**
This project is open-source. Feel free to use and modify the scripts.

---
