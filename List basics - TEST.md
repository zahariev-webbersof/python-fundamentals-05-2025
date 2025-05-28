### **Python List Basics and Challenges 🐍**

---

#### 1️⃣ What is the correct way to create an empty list in Python? 🤔

- A: `empty_list = []`
- B: `empty_list = {}`
- C: `empty_list = list[]`
- D: `empty_list = new_list()`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `empty_list = []`

</p>
</details>

---

#### 2️⃣ What is the output of the following Python code? 🧮

```python
numbers = [1, 2, 3, 4, 5]
squared = []
for x in numbers:
    squared.append(x**2)
result = sum(squared)
```

- A: 55
- B: 30
- C: 15
- D: 25

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: 55

</p>
</details>

---

#### 3️⃣ Which method is used to add an element to the beginning of a list? 🏁

- A: `my_list.prepend()`
- B: `my_list.insert(0, element)`
- C: `my_list.add_first(element)`
- D: `my_list.insert_first(element)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `my_list.insert(0, element)`

</p>
</details>

---

#### 4️⃣ What is the result of `len([1, 2, 3] + [4, 5])`? 📏

- A: 2
- B: 15
- C: Error
- D: 5

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: 5

</p>
</details>

---

#### 5️⃣ What is the output of the following code snippet? 🖨️

```python
my_list = ['a', 'b', 'c']
result = my_list * 2
print(result)
```

- A: `['a', 'b', 'c', 'a', 'b', 'c']`
- B: `['a', 'a', 'b', 'b', 'c', 'c']`
- C: `['a', 'b', 'c', 2]`
- D: `['a', 'b', 'c', '2']`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `['a', 'b', 'c', 'a', 'b', 'c']`

</p>
</details>

---

#### 6️⃣ How do you check if a specific value exists in a list? 🔍

- A: `if my_list.contains(value):`
- B: `if my_list.has(value):`
- C: `if value in my_list:`
- D: `if my_list.index(value):`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `if value in my_list:`

</p>
</details>

---

#### 7️⃣ Which method is used to insert an element at a specific index in a list? 🧩

- A: `my_list.insert(index, element)`
- B: `my_list.add(index, element)`
- C: `my_list.insert_at(index, element)`
- D: `my_list.put(index, element)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `my_list.insert(index, element)`

</p>
</details>

---

#### 8️⃣ How do you create a list of numbers from 0 to 9 in a single line? 🔢

- A: `number_list = [0:9]`
- B: `number_list = range(10).to_list()`
- C: `number_list = list(range(10))`
- D: `number_list = [range(10)]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `number_list = list(range(10))`

</p>
</details>

---

#### 9️⃣ How do you check if a list is empty? 🛑

- A: `if my_list.empty():`
- B: `if len(my_list) == 0:`
- C: `if not my_list:`
- D: `if my_list.is_empty():`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `if not my_list:`

</p>
</details>

---

#### 🔟 What is the output of the following code? 🤯

```python
my_list = [1, 2, 3, 4, 5]
my_list.pop(2)
print(my_list)
```

- A: `[1, 2, 4, 5]`
- B: `[1, 2, 3, 4, 5]`
- C: `[1, 3, 4, 5]`
- D: `[2, 3, 4, 5]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `[1, 2, 4, 5]`

</p>
</details>

---

### **New Questions 🚀**

---

#### 1️⃣1️⃣ What happens when you multiply a list by 0? 😅

```python
my_list = [1, 2, 3]
result = my_list * 0
```

- A: `[]`
- B: `[0]`
- C: `[1, 2, 3]`
- D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `[]`

</p>
</details>

---

#### 1️⃣2️⃣ What is the output of the following code? 🐍

```python
numbers = [1, 2, 3, 4]
result = [x**3 for x in numbers if x % 2 == 0]
print(result)
```

- A: `[1, 8, 27, 64]`
- B: `[8, 64]`
- C: `[8]`
- D: `Error`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `[8, 64]`

</p>
</details>

---

#### 1️⃣3️⃣ Can a list in Python contain other lists? 🤔

- A: Yes
- B: No
- C: Only if lists are converted to tuples
- D: Only in Python 3+

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: Yes

</p>
</details>

---

#### 1️⃣4️⃣ DEVIL QUESTION 😈

```python
nested_list = [1, [2, [3, [4]]]]
result = nested_list[1][1][1][0]
```

- A: 1
- B: 2
- C: 3
- D: 4

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: 4

</p>
</details>

--- 
