
import itertools
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

# Function to convert HEX to LAB
def hex_to_lab(hex_code):
    rgb = sRGBColor.new_from_rgb_hex(hex_code)
    lab = convert_color(rgb, LabColor)
    return lab

# Read input file
input_file = "summer_negative_count_hexa.txt"
output_file = "summer_negative_output.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

# Parse input data
hex_data = {}
for line in lines:
    hex_code, count = line.strip().split()
    hex_data[hex_code] = int(count)

# Convert all HEX values to LAB
lab_data = {hex_code: hex_to_lab(hex_code) for hex_code in hex_data.keys()}

# Merging logic
merged_data = hex_data.copy()

while True:
    used = set()
    new_merged_data = merged_data.copy()
    merged = False

    for (hex1, lab1), (hex2, lab2) in itertools.combinations(lab_data.items(), 2):
        if hex1 in used or hex2 in used or hex1 not in merged_data or hex2 not in merged_data:
            continue

        delta_e = delta_e_cie2000(lab1, lab2)
        if delta_e <= 2:
            # Merge counts
            new_count = merged_data[hex1] + merged_data[hex2]
            new_merged_data[hex1] = new_count
            del new_merged_data[hex2]
            lab_data[hex1] = hex_to_lab(hex1)  # Update LAB for merged key
            del lab_data[hex2]
            used.add(hex1)
            used.add(hex2)
            merged = True

    merged_data = new_merged_data
    if not merged:  # Exit if no merging occurred in this iteration
        break

# Save results to output file
with open(output_file, "w") as file:
    for hex_code, count in merged_data.items():
        file.write(f"{hex_code} {count}\n")

print(f"Results saved to {output_file}")
