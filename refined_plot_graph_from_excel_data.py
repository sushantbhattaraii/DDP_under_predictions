import pandas as pd
import glob
import matplotlib.pyplot as plt
import re
import numpy as np
from matplotlib.ticker import MultipleLocator
from fractions import Fraction
import os

# Gather and sort all Excel files
files = sorted(glob.glob('./results/error_and_stretch_data_with_cut-off_AND_overlap/64/overlap50/64nodes_diameter*.xlsx'))

# Extract node count and overlap from filename
m = re.search(r'(\d+)nodes_', files[0])
node_count = m.group(1) if m else "?"

m2 = re.search(r'overlap(\d+)', files[0])
overlap_value = m2.group(1) if m2 else "?"

# Prepare colormap
cmap = plt.get_cmap('tab20')
all_x = []

# Create two subplots: one for error, one for stretch
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 11), sharex=True)

for idx, f in enumerate(files):
    df = pd.read_excel(f)
    mean_error = df.groupby('fraction')['error'].mean()
    mean_stretch = df.groupby('fraction')['stretch'].mean()
    
    mean_error.index = mean_error.index * int(node_count)
    mean_stretch.index = mean_stretch.index * int(node_count)
    
    all_x.extend(mean_error.index.tolist())
    
    # Extract cutoff value from filename
    cutoff = f.split("_cutoff")[1].split("-")[0]
    actual_cutoff = 1 / float(cutoff)

    # Plot error
    ax1.plot(
        mean_error.index,
        mean_error.values,
        marker='o',
        label=f'{actual_cutoff}-cutoff Error',
        color=cmap(2 * idx)
    )

    # Plot stretch
    ax2.plot(
        mean_stretch.index,
        mean_stretch.values,
        marker='o',
        label=f'{actual_cutoff}-cutoff Stretch',
        color=cmap(2 * idx + 1)
    )

unique_x = sorted(set(all_x))

# Format error subplot
ax1.set_ylabel('Error')
ax2.set_xlabel(f'Number of predicted nodes among {node_count} nodes (# of operations)')
ax1.set_title(f'Error vs Fraction of Predicted Nodes (Overlap: {overlap_value}%)')
ax1.legend(loc='best')
# ax1.grid(True)

# Format stretch subplot
ax2.set_ylabel('Stretch')
ax2.set_xlabel(f'Number of predicted nodes among {node_count} nodes (# of operations)')
ax2.set_title(f'Stretch vs Fraction of Predicted Nodes (Overlap: {overlap_value}%)')
ax2.legend(loc='best')
# ax2.grid(True)

# Set shared x-ticks
ax2.set_xticks(unique_x)

# Save or display
plt.tight_layout()
folder = "6_cutoffs_merged"
filename = f'{node_count}_nodes_overlap{overlap_value}.png'
path_to_save = os.path.join('results', folder, filename)

# plt.savefig(path_to_save)
plt.show()
