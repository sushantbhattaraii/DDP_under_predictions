import pandas as pd
import os
import re

def save_error_stretch_to_excel(fractions, max_errors, min_errors, stretches, file_name, reps, error_cutoff):
    """
    Save both raw and summary statistics of error and stretch data to an Excel file.
    """
    n_groups = len(fractions)
    # Group raw data by fraction
    groups_max_error = [max_errors[i::n_groups] for i in range(n_groups)]
    groups_min_error = [min_errors[i::n_groups] for i in range(n_groups)]
    groups_stretch = [stretches[i::n_groups] for i in range(n_groups)]

    # Prepare raw records
    total_nodes = int(re.findall(r'\d+\.?\d*', file_name)[0])
    raw_records = []
    for frac, max_err_list, min_err_list, str_list in zip(fractions, groups_max_error, groups_min_error, groups_stretch):
        num_nodes = int(frac * total_nodes)
        for max_err, min_err, strc in zip(max_err_list, min_err_list, str_list):
            raw_records.append({
                'fraction': frac,
                'num_nodes': num_nodes,
                'max_error': max_err,
                'min_error': min_err,
                'stretch': strc,
                'reps': reps,
                'error_cutoff': error_cutoff,
                'file_name': file_name
            })
    raw_df = pd.DataFrame(raw_records)

    # Compute summary statistics
    summary_records = []
    for frac, max_err_list, min_err_list, str_list in zip(fractions, groups_max_error, groups_max_error, groups_stretch):
        num_nodes = int(frac * total_nodes)
        summary_records.append({
            'fraction': frac,
            'num_nodes': num_nodes,
            'mean_of_max_error': sum(max_err_list) / len(max_err_list),
            'min_of_max_error': min(max_err_list),
            'max_of_max_error': max(max_err_list),
            'mean_of_min_error': sum(min_err_list) / len(min_err_list),
            'min_of_min_error': min(min_err_list),
            'max_of_min_error': max(min_err_list),
            'mean_stretch': sum(str_list) / len(str_list),
            'min_stretch': min(str_list),
            'max_stretch': max(str_list),
            'reps': reps,
            'error_cutoff': error_cutoff,
            'file_name': file_name
        })
    summary_df = pd.DataFrame(summary_records)

    # Ensure output directory exists
    folder = "results/yes_constraints"
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
