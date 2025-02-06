# Unit 3 - Social Media Post Validation and Editing

## Overview
This project includes multiple Python functions to validate, edit, and manipulate social media posts using data structures such as **stacks** and **queues**. These functions help ensure proper formatting, content cleansing, and engagement optimization.

---

## Functions & Explanations

### 1. `is_valid_post_format(posts)`
**Purpose:**
- Checks if a post has properly matched **parentheses**, **brackets**, and **curly braces**.
- Uses a **stack** to validate the format.

**Approach:**
1. Iterate through the characters in `posts`.
2. Push opening brackets `{`, `[`, `(` onto the stack.
3. When encountering a closing bracket `}`, `]`, `)`, check if it correctly matches the last opening bracket.
4. If there’s a mismatch or the stack is not empty at the end, return `False`.
5. Otherwise, return `True`.

**Example Usage:**
```python
print(is_valid_post_format("()"))  # Output: True
print(is_valid_post_format("()[]{}"))  # Output: True
print(is_valid_post_format("(]"))  # Output: False
```

---

### 2. `reverse_comments_queue(comments)`
**Purpose:**
- Reverses the order of comments using a **queue**.

**Approach:**
1. Pop elements from the input list and push them into a new list.
2. Return the reversed list.

**Example Usage:**
```python
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# Output: ["Thanks for sharing.", "Love it!", "Great post!"]
```

---

### 3. `is_symmetrical_title(title)`
**Purpose:**
- Checks if a title is **symmetrical** (reads the same forward and backward, ignoring spaces).

**Approach:**
1. Convert the title to lowercase.
2. Use two pointers (`lp` and `rp`) at the start and end of the string.
3. Ignore spaces while checking for symmetry.
4. Return `True` if the title is symmetrical, otherwise `False`.

**Example Usage:**
```python
print(is_symmetrical_title("A Santa at NASA"))  # Output: True
print(is_symmetrical_title("Social Media"))  # Output: False
```

---

### 4. `engagement_boost(engagements)`
**Purpose:**
- Sorts engagement scores in decreasing order based on **squared values**.

**Approach:**
1. Square each engagement value and store the result along with the original index.
2. Sort the squared values in descending order.
3. Return the sorted list.

**Example Usage:**
```python
print(engagement_boost([1, -2, 3, -4]))  # Output: [16, 9, 4, 1]
```

---

### 5. `clean_post(post)`
**Purpose:**
- Removes adjacent pairs of characters where one is uppercase and the other is its lowercase counterpart.

**Approach:**
1. Use a **stack** to store characters.
2. If the current character cancels out the last character in the stack (case-insensitive match), remove both.
3. Otherwise, add it to the stack.
4. Return the cleaned-up post as a string.

**Example Usage:**
```python
print(clean_post("poOost"))  # Output: "post"
print(clean_post("abBAcC"))  # Output: ""
```

---

### 6. `edit_post(post)`
**Purpose:**
- **Reverses each word** in a post while keeping word order.
- Uses a **queue** for reversing words.

**Approach:**
1. Push characters into a queue until a space is encountered.
2. Pop characters from the queue to form a reversed word.
3. Continue for all words in the post.
4. Return the modified post.

**Example Usage:**
```python
print(edit_post("Boost your engagement with these tips"))  
# Output: "tsooB ruoy tnemegagne htiw eseht spit"
```

---

### 7. `post_compare(draft1, draft2)`
**Purpose:**
- Compares two drafts to check if they are **equivalent after processing backspaces (`#`)**.
- Uses a **stack** to simulate the effect of backspaces.

**Approach:**
1. Process both drafts character by character.
2. Push characters onto a stack, but remove the last character when encountering `#`.
3. Compare the final stacks.

**Example Usage:**
```python
print(post_compare("ab#c", "ad#c"))  # Output: True
print(post_compare("ab##", "c#d#"))  # Output: True
print(post_compare("a#c", "b"))  # Output: False
```

---

## **Key Concepts Covered**
✅ **Stacks** - Used for matching brackets, undoing edits (`#` backspaces), and cleaning posts.

✅ **Queues** - Used for reversing comments and reversing words in a post.

✅ **Two-Pointer Technique** - Used for checking symmetrical titles.

✅ **Sorting** - Used for engagement boosting by squaring values and sorting.

---

## **How to Run the Code**
1. Copy the functions into a Python script (e.g., `unit3_social_media.py`).
2. Run the script in a Python environment:
   ```sh
   python unit3_social_media.py
   ```
3. Modify test cases as needed to validate different inputs.

---

## **Conclusion**
This project demonstrates how **stacks, queues, and sorting techniques** can be applied to social media-related tasks. These functions improve content formatting, readability, and engagement management efficiently.

🚀 Happy coding!

