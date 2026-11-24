import os

TEXT = "The ultrasound showed two heartbeats, and the doctor said only one of them was mine."

def main():
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, not whitespace-only.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
