#  String Range Expander

This is a Python utility that takes a string input representing numbers and numeric ranges (like `"1-3,5,7-9"`) and expands it into a full list of integers.

The project is structured in progressive stages as outlined in the assignment. All 7 stages have been implemented with a focus on clean design, configurability, and robust handling of edge cases.

---

##  Features by Stage

### 🔹 Stage 1: Basic Range Expansion
Parses numbers and simple numeric ranges:
- `"1-3"` → `[1, 2, 3]`
- `"5"` → `[5]`

### 🔹 Stage 2: Whitespace and Empty Entry Handling
Cleans the input:
- `" , 1-3 , ,5 "` → `[1, 2, 3, 5]`

### 🔹 Stage 3: Custom Range Delimiters
Supports alternate delimiters like `..`, `~`, and `to`:
- `"1..3"` → `[1, 2, 3]`
- `"4~6"` → `[4, 5, 6]`
- `"10 to 12"` → `[10, 11, 12]`

### 🔹 Stage 4: Reversed and Invalid Ranges
Handles:
- Reversed ranges: `"5-3"` → `[5, 4, 3]`
- Single-point ranges: `"3-3"` → `[3]`
- Invalid input: `"3-a"` → raises an error

### 🔹 Stage 5: Step Values
Adds support for step syntax:
- `"1-10:2"` → `[1, 3, 5, 7, 9]`
- `"10-1:3"` → `[10, 7, 4, 1]`

### 🔹 Stage 6: Duplicate and Overlapping Handling
Merges and deduplicates:
- `"1-3,2-5"` → `[1, 2, 3, 4, 5]`

### 🔹 Stage 7: Output Format Control
Supports output as:
- Python `list` → `[1, 2, 3]`
- CSV string → `"1,2,3"`
- Python `set` → `{1, 2, 3}`

---

##  How to Run

### 1. Clone or download the repository

```bash
git clone url
cd string-range-expander

python test_range_expander.py
