# Stage 1–7: Complete String Range Expander

import re
from typing import List, Union, Set

class RangeExpander:
    def __init__(self,
                 delimiters: List[str] = ['-'],
                 step_delimiter: str = ':',
                 output_format: str = 'list'):
        self.delimiters = delimiters
        self.step_delimiter = step_delimiter
        self.output_format = output_format

    def expand(self, input_str: str) -> Union[List[int], Set[int], str]:
        tokens = [t.strip() for t in input_str.split(',') if t.strip()]
        result = []

        for token in tokens:
            step = 1

            if self.step_delimiter in token:
                token, step_str = token.split(self.step_delimiter)
                if not step_str.strip().isdigit():
                    raise ValueError(f"Invalid step value: {step_str}")
                step = int(step_str.strip())

            delimiter_used = None
            for delim in self.delimiters:
                if delim in token:
                    delimiter_used = delim
                    break

            if delimiter_used:
                parts = [p.strip() for p in token.split(delimiter_used)]
                if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                    raise ValueError(f"Invalid range: {token}")
                start, end = int(parts[0]), int(parts[1])
                if start <= end:
                    result.extend(range(start, end + 1, step))
                else:
                    result.extend(range(start, end - 1, -step))
            else:
                if not token.strip().isdigit():
                    raise ValueError(f"Invalid number: {token}")
                result.append(int(token.strip()))

        # Stage 6: Deduplication and merging handled by converting to sorted set
        result = sorted(set(result))

        # Stage 7: Output format control
        if self.output_format == 'list':
            return result
        elif self.output_format == 'csv':
            return ','.join(map(str, result))
        elif self.output_format == 'set':
            return set(result)
        else:
            raise ValueError(f"Unsupported output format: {self.output_format}")

# Example usage:
# expander = RangeExpander(delimiters=['-', '..', '~', 'to'], output_format='list')
# print(expander.expand("1-3, 2~5, 10 to 12, 5-3, 1-10:2, 10-1:3"))
