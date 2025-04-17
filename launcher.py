import subprocess

# The four fraction values
fractions = [1/32, 1/16, 1/8, 1/4]

for frac in fractions:
    print(f"\n=== Running a.py with --fraction {frac:.6f} ===")
    subprocess.run(
        ["python", "run.py", "--fraction", str(frac)],
        check=True
    )