# 🧠 Algorithm Challenge: **“Sequence Compression” 📉🧮**

---

## 🌀 Task Summary

You're given a **sequence of numbers**.
Your task is to **compress** the sequence by counting how many times each number repeats *consecutively* and output a compressed version of the sequence.

This challenge requires you to **analyze patterns**, use **loops and conditions**, and apply algorithmic thinking to **track state over time**.

---

### 📥 Example Input

```python
[1, 1, 1, 2, 2, 3, 1, 1]
```

### 📤 Expected Output

```python
[(1, 3), (2, 2), (3, 1), (1, 2)]
```

Each tuple represents a number and how many times it appears **in a row**.

---

## 🧠 Algorithm Description

1. **Start with the first number** in the list.
2. **Initialize a counter** to track how many times it appears consecutively.
3. **Loop through the list**:

   * If the current number is the same as the previous one, increment the counter.
   * If it's different, **store the previous number and its count**, then reset the counter for the new number.
4. At the end of the loop, don’t forget to **store the last number and its count**.
5. Return the compressed result.

---

## 🚀 Why This Is Challenging

* You must **track state across iterations** (current value and count).
* You need to **handle the last element** after the loop.
* The solution must work for **any list length**, including edge cases like `[]` or `[7]`.

---

## 🧠 Use AI Smartly

If you're stuck, use AI to **ask focused questions**, like:

* “How do I track values while looping in Python?”
* “How can I handle the last element in a loop?”
* “How do I append a tuple to a list?”

AI is here to **guide your reasoning**, not just give answers. Learn how to **translate ideas into code**.

---

## 🧩 Bonus Challenge (Optional)

* Compress **characters** instead of numbers: e.g., `['a', 'a', 'b', 'b', 'b'] → [('a', 2), ('b', 3)]`
* Expand the compressed list back to its original form.
* Create a **function** and test it with multiple inputs.

---

## 🛠️ Starter Code (With Comments)

```python
# 📉 Sequence Compression

# Step 1: Define the sequence
sequence = [1, 1, 1, 2, 2, 3, 1, 1]

# Step 2: Create an empty list to hold compressed result
compressed = []

# Step 3: Initialize variables to track the current number and count
# TODO: Set 'current' to the first element, and 'count' to 1

# Step 4: Loop through the rest of the sequence
# TODO: If the number is the same as 'current', increase 'count'
# TODO: If different, append (current, count) to 'compressed', update 'current', reset 'count'

# Step 5: Don’t forget to add the last group
# TODO: Append the final (current, count) to the result

# Step 6: Print the compressed sequence
# TODO: Output the 'compressed' list
```

---

## 🎓 Learning Goals

* Understand how to **design and trace an algorithm**.
* Practice **loop logic**, **comparison**, and **data structure manipulation**.
* Learn to **break a problem into steps**, then implement and test.

---

## 🔍 Real-World Connection

This concept is called **Run-Length Encoding (RLE)** — used in **data compression**, **image processing**, and **network protocols**. You're applying a real algorithm!
