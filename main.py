import os

LINE = "A dustpan catches every speck except the last grey line, which it leaves like a signature."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as entry:
    # Preserve the exact review without a trailing newline.
    entry.write(LINE)
