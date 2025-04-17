import re
import subprocess
from run import plot_error_graph

# The four fraction values
fractions = [1/32, 1/16, 1/8, 1/4, 1/2]
errors = []

pattern = re.compile(
    r"Overall error \(max_i\(distance_in_G / diameter_G\)\) =\s*([0-9.+\-eE]+)"
)

for frac in fractions:
    print(f"\n=== Running run.py with --fraction {frac:.6f} ===")
    proc = subprocess.Popen(
        ["python", "run.py", "--fraction", str(frac)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    captured = ""

    # read line by line
    for line in proc.stdout:
        print(line, end="")       # echo to your terminal
        captured += line
        m = pattern.search(line)
        if m:
            error_value = float(m.group(1))
    
    proc.wait()
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, proc.args)

    errors.append(error_value)

print("Plotting the error graph...")

plot_error_graph(fractions, errors)