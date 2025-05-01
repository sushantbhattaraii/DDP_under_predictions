import pandas as pd
import glob
import matplotlib.pyplot as plt
import re
import numpy as np
from matplotlib.ticker import MultipleLocator
from fractions import Fraction


# Gather and sort all 64-node Excel files
files = sorted(glob.glob('./results/error_and_stretch_data_with_cut-off_AND_overlap/256/overlap25/256nodes_diameter*.xlsx'))

m = re.search(r'(\d+)nodes_', files[0])
node_count = m.group(1) if m else "?"

m2 = re.search(r'(\d+).xlsx', files[0])
overlap_value = m2.group(1) if m else "?"

# Prepare colormap
cmap = plt.get_cmap('tab20')

all_x = []

plt.figure(figsize=(9, 10))
for idx, f in enumerate(files):
    # Read data
    df = pd.read_excel(f)
    # Compute mean error and mean stretch by fraction
    mean_error = df.groupby('fraction')['error'].mean()
    mean_stretch = df.groupby('fraction')['stretch'].mean()
    
    all_x.extend(mean_error.index.tolist())
    all_x.extend(mean_stretch.index.tolist())


    # Extract cutoff value from filename
    cutoff = f.split("_cutoff")[1].split("-")[0]
    actual_cutoff = 1/(float(cutoff))
    # Plot mean error with a unique color
    plt.plot(
        mean_error.index,
        mean_error.values,
        marker='o',
        label=f'{actual_cutoff}:cutoff Error',
        color=cmap(2 * idx)
    )
    # Plot mean stretch with the next unique color
    plt.plot(
        mean_stretch.index,
        mean_stretch.values,
        marker='o',
        label=f'{actual_cutoff}: cutoff Stretch',
        color=cmap(2 * idx + 1)
    )


unique_x = sorted(set(all_x))

# Labeling
plt.xlabel(f'Fraction of predicted nodes among {node_count} nodes (# of operations)')
plt.ylabel('Error / Stretch')
plt.title(f'Error/Stretch vs Fraction of nodes (# of operations) in {node_count} Node Graph | Prediction Overlap: {overlap_value}%')
plt.grid(True)

plt.vlines(x=mean_error.index, ymin=0, ymax=mean_error.values, color='gray', linestyle='--', linewidth=0.8)

ax = plt.gca()
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.set_xticks(unique_x)

plt.legend(loc='best')
plt.tight_layout()
plt.show()
