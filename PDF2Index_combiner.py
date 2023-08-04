import sys

# Parse CLI flags
args = sys.argv[1:]
if len(args) == 0:
    print("Usage: 'python index_combiner.py index1.txt index2.txt index3.txt' etc.")
    sys.exit()

# Get file data
index = {}
for count, filename in enumerate(args):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.read().split("\n"):
            if ": " not in line:
                continue
            index_key, pages = line.split(": ", 1)  # Modified this line
            if index_key not in index:
                index[index_key] = ""
            index[index_key] += f"{count + 1}({pages}) | "

# Trim trailing " | "s
for key in index.keys():
    index[key] = index[key].rstrip(" | ")

# Turn index -> lines
lines = []
for key in index.keys():
    lines.append(f"{key}: {index[key]}")
lines.sort()
output_file = "out.txt"  # Change this line to set the desired output filename
with open(output_file, "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

print(f"Written combined index to {output_file}")
