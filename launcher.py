import re
import subprocess
from plot_graph import *

repetitions = 50
errors = []
for rep in range(repetitions):
    # The four fraction values
    fractions = [1/32, 1/16, 1/8, 1/4, 1/2]
    nodes_count = []


    pattern = re.compile(
        r"Overall error \(max_i\(distance_in_G / diameter_G\)\) =\s*([0-9.+\-eE]+)"
    )

    pattern2 = re.compile(
        r"Total \# of vertices \(n\):\s*([0-9.+\-eE]+)"
    )

    for frac in fractions:
        print(f"\n=== Running run.py with --fraction {frac:.6f}  and Iteration {rep} ===")
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
            m2 = pattern2.search(line)
            if m:
                error_value = float(m.group(1))
            if m2:
                num_nodes = int(m2.group(1))
        
        proc.wait()
        if proc.returncode != 0:
            raise subprocess.CalledProcessError(proc.returncode, proc.args)

        errors.append(error_value)
        nodes_count.append(num_nodes)


print("Plotting the error graph...")

filename = str(nodes_count[0])+"nodes_error_graph-repetitions-"+str(repetitions)+ ".png"

plot_error_graph_with_boxplot(fractions, errors, filename, repetitions)