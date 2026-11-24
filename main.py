"""Write the sick-day excuse entry to $ENTRY_OUT.

The harness may hand us a file path or a directory; both are handled.
Stdlib only.
"""

import os
import sys

SICK_DAY_LINE = (
    "I got stung by a bee while brushing my teeth and now my lip "
    "looks like it lost an argument with a balloon animal."
)


def build_entry_text():
    """Return the single-line excuse, validated as one line under 200 chars."""
    line = SICK_DAY_LINE.strip()
    if "\n" in line or not 1 <= len(line) <= 200:
        raise ValueError("entry must be a single line of 1-200 characters")
    return line


def entry_path_for(raw_target):
    """Resolve $ENTRY_OUT to a concrete file path (file or directory)."""
    if os.path.isdir(raw_target):
        return os.path.join(raw_target, "entry.txt")
    return raw_target


def emit_entry():
    destination = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    target_file = entry_path_for(destination)
    parent_dir = os.path.dirname(target_file)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    with open(target_file, "w", encoding="utf-8") as handle:
        handle.write(build_entry_text())
    return 0


if __name__ == "__main__":
    sys.exit(emit_entry())
