import re
import subprocess
from run import plot_error_graph

# The four fraction values
fractions = [1/32, 1/16, 1/8, 1/4]
errors = []

pattern = re.compile(
    r"Overall error \(max_i\(distance_in_G / diameter_G\)\) =\s*([0-9.+\-eE]+)"
)

for frac in fractions:
    print(f"\n=== Running run.py with --fraction {frac:.6f} ===")
    proc = subprocess.run(
        ["python", "run.py", "--fraction", str(frac)],
        capture_output=True,
        text=True,
        check=True
    )
    output = proc.stdout.strip()

    # Search for the line containing the line
    m = pattern.search(output)
    error_value = float(m.group(1))
    errors.append(error_value)

print("Plotting the error graph...")

plot_error_graph(fractions, errors)