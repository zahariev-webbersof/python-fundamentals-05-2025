### **Advanced Python List Challenges 🐍**

---

#### 1️⃣ What is the output of the following code? 🧐

```python
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)
```

- A: `[1, 2, 3]`
- B: `[1, 2, 3, 4]`
- C: `Error`
- D: `[4, 1, 2, 3]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `[1, 2, 3, 4]`

*Explanation:* `list2` is just a reference to `list1`, so modifying `list2` also affects `list1`.

</p>
</details>

---

#### 2️⃣ What is the output of the following code? 🤯

```python
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[::-2])
```

- A: `[5, 3, 1]`
- B: `[0, 2, 4]`
- C: `[4, 2, 0]`
- D: `[5, 3, 1, 0]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `[5, 3, 1]`

*Explanation:* `[::-2]` reverses the list and skips every second element.

</p>
</details>

---

#### 3️⃣ What happens when you sort a list containing both integers and strings? 🚨

```python
my_list = [1, 'a', 3, 'b']
my_list.sort()
```

- A: The list is sorted as `[1, 3, 'a', 'b']`
- B: The list remains unchanged
- C: RuntimeError occurs
- D: TypeError occurs

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: TypeError occurs

*Explanation:* Python cannot compare integers and strings when sorting.

</p>
</details>

---

#### 4️⃣ What does the following list comprehension do? 🧐

```python
[x for x in range(10) if x % 3 == 0 if x % 2 == 0]
```

- A: `[0, 6]`
- B: `[0, 3, 6, 9]`
- C: `[0, 2, 4, 6, 8]`
- D: `[0, 6, 9]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `[0, 6]`

*Explanation:* The condition filters numbers divisible by both 3 and 2, leaving only `[0, 6]`.

</p>
</details>

---

#### 5️⃣ What is the difference between `list.remove(x)` and `del list[x]`? ⚡

- A: `remove(x)` removes by value, `del list[x]` removes by index
- B: `remove(x)` and `del list[x]` both remove by index
- C: `remove(x)` is faster than `del list[x]`
- D: `del list[x]` works only on sorted lists

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `remove(x)` removes by value, `del list[x]` removes by index

*Explanation:* `remove(x)` finds and deletes the first occurrence of `x`, while `del` removes an element at a specific index.

</p>
</details>

---

#### 6️⃣ What is the output of this Python snippet? 🧠

```python
list1 = [[]] * 3
list1[0].append(5)
print(list1)
```

- A: `[[], [], []]`
- B: `[[5], [], []]`
- C: `[[5], [5], [5]]`
- D: `[[5]]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `[[5], [5], [5]]`

*Explanation:* `list1 = [[]] * 3` creates three references to the same list object. Modifying one affects all.

</p>
</details>

---

#### 7️⃣ How do you remove duplicates from a list while maintaining order? 📌

- A: `list(set(my_list))`
- B: `sorted(set(my_list))`
- C: `[x for i, x in enumerate(my_list) if x not in my_list[:i]]`
- D: `my_list.remove_duplicates()`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `[x for i, x in enumerate(my_list) if x not in my_list[:i]]`

*Explanation:* The set method removes duplicates but does not preserve order.

</p>
</details>

---

#### 8️⃣ What does `list1.extend(list2)` do differently from `list1.append(list2)`? 🧐

- A: `extend` merges lists, `append` adds the whole list as a single element
- B: `extend` sorts elements, `append` does not
- C: They behave the same way
- D: `append` modifies the original list, `extend` does not

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `extend` merges lists, `append` adds the whole list as a single element

*Explanation:* `extend()` iterates through `list2` and adds elements individually, while `append()` adds the entire list as a single element.

</p>
</details>

---

#### 9️⃣ What is the output of this tricky list operation? 😵‍💫

```python
list1 = [1, 2, 3]
list2 = list1[::-1]
list1[0] = 99
print(list2)
```

- A: `[99, 2, 3]`
- B: `[3, 2, 1]`
- C: `[3, 2, 99]`
- D: `[99, 2, 1]`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `[3, 2, 1]`

*Explanation:* `list[::-1]` creates a new reversed copy of the list, so modifying `list1` does not affect `list2`.

</p>
</details>

---

### **Ready for the next level? 🚀**

If you got most of these right, you're well on your way to mastering Python lists! Keep practicing, and challenge yourself with even more advanced Python concepts! 🔥🐍
