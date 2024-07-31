from pathlib import Path

COL_NAMES = (
    "Results reception time",
    "MD5 hash of participant's IP address",
    "Controller name",
    "Order number of item",
    "Inner element number",
    "Label",
    "Latin Square Group",
    "PennElementType",
    "PennElementName",
    "Parameter",
    "Value",
    "EventTime",
    "Item",
    "Condition",
    "Group",
    "Context",
    "Sentence",
    "Target",
    "ComprehensionQuestion",
    "Comments"
)

with open('../data/ClozeData(in).csv') as original_file:
    lines = [line for line in original_file.readlines() if ',exp,' in line]

print(len(lines))

with open('../data/experimental_data.csv','w') as experimental_file:
    experimental_file.write(f"{','.join(COL_NAMES)}\n")
    for line in lines:
        experimental_file.write(line)

