"""Five Seconds to Explain the Glass — entry for make.fun.

Writes one sentence to /output/entry.txt.
"""
import os

# The defence: the cat denies nothing by admitting nothing — the glass was already falling; the cat was only testing gravity, and gravity failed.
TEXT = "The glass was already falling when I walked in — I was simply conducting a gravity inspection and it failed."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
