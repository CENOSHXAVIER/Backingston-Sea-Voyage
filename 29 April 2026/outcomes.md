# Python Basics – Day 1

## 🎯 Objective

The goal for this session was to:

* Set up Python on my local machine
* Execute basic Python programs
* Understand fundamental programming concepts required for backend development

---

## ⚙️ Environment Setup

* Installed Python from the official website
* Verified installation using:

```bash
python --version
```

### Key Learning:

* Python versioning is **critical**
* Different versions in development and production can cause:

  * Compatibility issues
  * Application crashes
  * Potential business impact (including financial loss)!!!!

---

## 🧠 Core Concepts Learned

### 1. Basic Syntax & Variables

* Declaring variables
* Understanding different data types (int, float, string, boolean)

---

### 2. Input & Output

* `input()` function is used to take user input
* `print()` function is used to display output

#### Important Insight:

* `input()` **always returns a string**, regardless of the input

---

### 3. Arithmetic Operations

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)

---

### 4. Logical Operators

* `and`
* `or`
* `not`

Used for combining and evaluating conditions

---

### 5. Conditional Statements

* Used `if-else` to control program flow
* Implemented a basic authentication check using conditions

---

### 6. Loops

#### For Loop:

* Used for iterating a fixed number of times

```python
for i in range(10):
    print(i + 1)
```

#### While Loop:

* Used for running a loop based on a condition

```python
i = 15
while i > 5:
    print("i love ronaldo")
    i -= 1
```

---

## 🧪 Practice

* Wrote and executed multiple small programs to apply:

  * Arithmetic operations
  * Logical conditions
  * Loops
  * Input handling

* Code has been committed to the repository for reference

---

## ⚠️ Errors Faced

* Python version confusion (multiple versions installed, wrong version showing initially)
* Indentation error due to incorrect spacing in `if`/loop blocks
* Confusion about syntax (initially thought colon `:` was not required)

### Corrections / Learnings:

* Python requires both:

  * `:` after statements like `if`, `elif`, `else`, `for`, `while`
  * Proper indentation to define code blocks
* Indentation is **not optional** — it defines program structure

---

## 📌 Summary

This session focused on building a strong foundation in Python basics, which is essential before moving into backend concepts like APIs and databases.

---
