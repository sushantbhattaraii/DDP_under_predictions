import pandas as pd
import os
import re

def save_error_stretch_to_excel(fractions, errors, stretches, file_name, reps, error_cutoff):
    """
    Save both raw and summary statistics of error and stretch data to an Excel file.
    """
    n_groups = len(fractions)
    # Group raw data by fraction
    groups_error = [errors[i::n_groups] for i in range(n_groups)]
    groups_stretch = [stretches[i::n_groups] for i in range(n_groups)]

    # Prepare raw records
    total_nodes = int(re.findall(r'\d+\.?\d*', file_name)[0])
    raw_records = []
    for frac, err_list, str_list in zip(fractions, groups_error, groups_stretch):
        num_nodes = int(frac * total_nodes)
        for err, strc in zip(err_list, str_list):
            raw_records.append({
                'fraction': frac,
                'num_nodes': num_nodes,
                'error': err,
                'stretch': strc,
                'reps': reps,
                'error_cutoff': error_cutoff,
                'file_name': file_name
            })
    raw_df = pd.DataFrame(raw_records)

    # Compute summary statistics
    summary_records = []
    for frac, err_list, str_list in zip(fractions, groups_error, groups_stretch):
        num_nodes = int(frac * total_nodes)
        summary_records.append({
            'fraction': frac,
            'num_nodes': num_nodes,
            'mean_error': sum(err_list) / len(err_list),
            'min_error': min(err_list),
            'max_error': max(err_list),
            'mean_stretch': sum(str_list) / len(str_list),
            'min_stretch': min(str_list),
            'max_stretch': max(str_list),
            'reps': reps,
            'error_cutoff': error_cutoff,
            'file_name': file_name
        })
    summary_df = pd.DataFrame(summary_records)

    # Ensure output directory exists
    folder = "results/error_and_stretch_data_with_cutoff_AND_overlap"
    os.makedirs(folder, exist_ok=True)
    excel_path = os.path.join(folder, f"{os.path.splitext(file_name)[0]}.xlsx")

    # Write both raw and summary to Excel
    with pd.ExcelWriter(excel_path) as writer:
        raw_df.to_excel(writer, sheet_name='raw', index=False)
        summary_df.to_excel(writer, sheet_name='summary', index=False)

    return excel_path

# Example usage within your plotting function:
# excel_file = save_error_stretch_to_excel(fractions, errors, stretches, file_name, reps, error_cutoff)
# print(f"Data saved to {excel_file}")
