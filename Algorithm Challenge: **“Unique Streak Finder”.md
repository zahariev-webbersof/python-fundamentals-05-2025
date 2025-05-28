# 🧠 Algorithm Challenge: **“Unique Streak Finder” 🌈✨**

---

## 🌀 Task Summary

You're given a **list of integers**.
Your task is to **find and return all the longest *non-repeating* sublists** from the list.

This challenge will help you practice **list slicing**, **tracking unique values**, and using **loops and conditionals** to maintain sequences dynamically.

---

### 📥 Example Input

```python
[1, 2, 3, 1, 2, 4, 5]
```

### 📤 Expected Output

```python
[[1, 2, 3], [2, 4, 5]]
```

These are the longest sublists that do **not** contain duplicate numbers.

---

## 🧠 Algorithm Description

1. **Start with an empty list** to hold the current non-repeating streak.
2. **Loop through the input list**:

   * If the current number is **not in the current streak**, add it.
   * If it **is already in**, the streak is broken:

     * Save the streak if it's the longest so far.
     * Start a new streak from the next element **after the previous duplicate**.
3. Use a **second list to store all longest streaks**.
4. Return **all streaks that are longest** in length.

---

## 🚀 Why This Is Challenging

* Requires **list tracking and memory**.
* Students must think about how to **reset a streak** correctly.
* They’ll need to **compare streak lengths** dynamically.

---

## 🧠 Use AI Smartly

Ask focused questions like:

* “How do I check if an element exists in a list?”
* “How do I slice a list in Python?”
* “How do I compare lengths of lists?”

---

## 🧩 Bonus Challenges (Optional)

* Track the **starting index** of each streak.
* Modify the logic to return only the **first** longest non-repeating sequence.
* Count how many unique streaks are found in total.

---

## 🛠️ Starter Code (With Comments)

```python
# 🌈 Unique Streak Finder

# Step 1: Define the input list
data = [1, 2, 3, 1, 2, 4, 5]

# Step 2: Create a list to store the current streak
current_streak = []

# Step 3: Create a list to store all the longest streaks found
longest_streaks = []

# Step 4: Initialize a variable for the max length found so far
max_length = 0

# Step 5: Loop through each number in the data list
# TODO: If number is not in current_streak, add it
# TODO: If it is in current_streak:
#         - Check if current_streak is longer than max_length
#         - If so, update max_length and reset longest_streaks list
#         - If equal, just add it to longest_streaks
#         - Reset current_streak starting from the element after the duplicate

# Step 6: After the loop, check the final current_streak again

# Step 7: Print all longest streaks
# TODO: Output the longest_streaks list
```

---

## 🎯 Learning Goals

* Use **Python lists** to manage sequences.
* Practice **if-else logic**, **slicing**, and **loop state tracking**.
* Apply algorithmic problem solving without using dictionaries or sets.

---

## 🔍 Real-World Connection

This kind of logic is used in:

* **Music streaming** (tracking unique song streaks)
* **Fitness tracking apps** (finding longest exercise streaks without rest)
* **Game mechanics** (detecting combo streaks)

You're building an algorithm that learns to **recognize unique patterns**—a foundational skill in software development.
