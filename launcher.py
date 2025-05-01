import re
import subprocess
from plot_graph import *
import argparse
import os
import re
from fractions import Fraction
from save_data_to_excel import *

def main(network_file_name, repetitions, error_cutoff, overlap):
    max_errors = []
    min_errors = []
    stretches = []
    for rep in range(repetitions):
        # The four fraction values
        fractions = [1/32, 1/16, 1/8, 1/4, 1/2]
        nodes_count = []


        pattern = re.compile(
            r"Overall max error \(max_i\(distance_in_G / diameter_G\)\) =\s*([0-9.+\-eE]+)"
        )

        pattern4 = re.compile(
            r"Overall min error \(min_i\(distance_in_G / diameter_G\)\) =\s*([0-9.+\-eE]+)"
        )

        pattern2 = re.compile(
            r"Total \# of vertices \(n\):\s*([0-9.+\-eE]+)"
        )

        pattern3 = re.compile(
            r"Stretch \(sum_of_distance_in_T / sum_of_distance_in_G\) =\s*([0-9.+\-eE]+)"
        )

        for frac in fractions:
            print(f"\n=== Running run.py with --fraction {frac:.6f}  and Iteration {rep} ===")
            proc = subprocess.Popen(
                ["python", "run.py", "--fraction", str(frac), "--network", str(network_file_name), "--cutoff", str(error_cutoff), "--overlap", str(overlap)],
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
                m3 = pattern3.search(line)
                m4 = pattern4.search(line)
                if m:
                    max_error_value = float(m.group(1))
                if m2:
                    num_nodes = int(m2.group(1))
                if m3:
                    stretch_value = float(m3.group(1))
                if m4:
                    min_error_value = float(m4.group(1))
            
            proc.wait()
            if proc.returncode != 0:
                raise subprocess.CalledProcessError(proc.returncode, proc.args)

            max_errors.append(max_error_value)
            min_errors.append(min_error_value)
            stretches.append(stretch_value)
            nodes_count.append(num_nodes)


    # Searching for the diameter of the graph from its filename
    md = re.search(r"diameter(\d+)", str(network_file_name))
    if md:
        diameter_value = md.group(1)   # this is the string "48"

    

    print("Plotting the error graph...")

    # filename = str(nodes_count[0])+"nodes_diameter"+str(diameter_value)+"_cutoff"+str(error_cutoff)+"-repetitions"+str(repetitions)+".png"
    filename = str(nodes_count[0])+"nodes_diameter"+str(diameter_value)+"_cutoff"+str(error_cutoff)+"-repetitions"+str(repetitions)+ "-overlap"+str(overlap)+".png"

    # plot_error_and_stretch_graph_with_boxplot(fractions, errors, filename, repetitions, stretches, error_cutoff, overlap)
    save_error_stretch_to_excel(fractions, max_errors, min_errors, stretches, filename, repetitions, error_cutoff)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Running the experiment with different fractions of predicted nodes and with different graphs... ")
    p.add_argument(
        "-n",
        "--network",
        required=True,
        type=str,
        help="The network file name to run an algorithm on (e.g. '256random_diameter71test.edgelist')"
    )
    p.add_argument(
        "-r",
        "--repetitions",
        default=1,
        type=int,
        help="Number of repetitions for the experiment (default: 1)"
    )
    p.add_argument(
        "-c",
        "--cutoff",
        default=1.0,
        type=float,
        help="Cutoff parameter for the error value (implies the error value cannot go beyond this cutoff)"
    )
    p.add_argument(
        "-o",
        "--overlap",
        default=100,
        type=int,
        help="Overlap of the actual nodes requesting for the object (in percentage)"
    )
    args = p.parse_args()
    main(args.network, args.repetitions, args.cutoff, args.overlap)
