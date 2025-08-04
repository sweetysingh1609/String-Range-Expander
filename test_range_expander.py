from range_expander import RangeExpander

# You can change delimiters or output format as needed
expander = RangeExpander(delimiters=['-', '..', '~', 'to'], output_format='list')

# Test Inputs
test_cases = [
    ("1-3,5,7-9", [1, 2, 3, 5, 7, 8, 9]),
    (" , 1-3 , ,5 ", [1, 2, 3, 5]),
    ("1..3,4~6,10 to 12", [1, 2, 3, 4, 5, 6, 10, 11, 12]),
    ("5-3", [3, 4, 5][::-1]),  # Reversed range
    ("3-3", [3]),
    ("1-10:2", [1, 3, 5, 7, 9]),
    ("10-1:3", [10, 7, 4, 1]),
    ("1-3,2-5", [1, 2, 3, 4, 5]),  # deduplication
]

# Run tests
for i, (input_str, expected) in enumerate(test_cases):
    try:
        result = expander.expand(input_str)
        print(f"Test {i+1}: PASS - {result}")
    except Exception as e:
        print(f"Test {i+1}: FAIL - Exception: {e}")
