import pandas as pd
import numpy as np

# RULES
# bulky: >= 1.000.000 or >= 150
# heavy: >= 20

# DISPATCH
# standard: not bulky and not heavy
# special: (bulky or heavy) BUT not both
# rejected: bulky and heavy

def sort(width, height, length, mass):

    is_heavy = (mass >= 20)
    is_bucky = (width * height * length >= 1000000 or
                width >= 150 or
                height >= 150 or
                length >= 150)

    if is_bucky and is_heavy:
        return "REJECTED"
    elif is_bucky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# read data from csv
# handle inconsistences, errors and missing values
# for inconsistences exclude the line
# calculate statistics:
#   total number of packages
#   number and % of packages in each stack
#   average, mim and max for Mass and Volume
# generate a summary report
#   statistics
#   easy to read

def data_ingestion():
    # Read CSV, use first line as header
    artifacts = pd.read_csv('packages.csv', on_bad_lines='skip', header=0)
    # Strip whitespace from column names
    artifacts.columns = artifacts.columns.str.strip()
    # Remove rows with missing values
    artifacts = artifacts.dropna()
    # Remove duplicates
    artifacts = artifacts.drop_duplicates()
    # Convert all columns to integer (assuming all columns are numeric)
    for col in artifacts.columns:
        artifacts[col] = pd.to_numeric(artifacts[col], errors='coerce')
    # Drop rows where conversion failed (non-integer values)
    artifacts = artifacts.dropna().astype(int)
    artifacts = artifacts[
        (artifacts['Width'] > 0) &
        (artifacts['Height'] > 0) &
        (artifacts['Length'] > 0) &
        (artifacts['Mass'] > 0)
    ]
    return artifacts

def statistics(packages):
    total_packages = len(packages)

    packages['category'] = packages.apply(
        lambda row: sort(row['Width'], row['Height'], row['Length'], row['Mass']),
        axis=1
    )

    category_counts = packages['category'].value_counts()
    category_percentages = packages['category'].value_counts(normalize=True) * 100

    packages['Volume'] = packages['Width'] * packages['Height'] * packages['Length']

    mass_stats = {
        'average': packages['Mass'].mean(),
        'min': packages['Mass'].min(),
        'max': packages['Mass'].max()
    }

    volume_stats = {
        'average': packages['Volume'].mean(),
        'min': packages['Volume'].min(),
        'max': packages['Volume'].max()
    }

    report = {
        'total_packages': total_packages,
        'category_counts': category_counts.to_dict(),
        'category_percentages': category_percentages.to_dict(),
        'mass_stats': mass_stats,
        'volume_stats': volume_stats
    }

    return report

def generate_report(stats):
    print("Package Sorting Report")
    print("======================")
    print(f"Total Packages: {stats['total_packages']}\n")

    print("Category Distribution:")
    for category, count in stats['category_counts'].items():
        percentage = stats['category_percentages'][category]
        print(f"  {category}: {count} ({percentage:.2f}%)")
    print()

    print("Mass Statistics:")
    for category, count in stats['mass_stats'].items():
        print(f"  {category}: {count} ({percentage:.2f}%)")
    print()

    print("Volume Statistics:")
    for category, count in stats['volume_stats'].items():
        print(f"  {category}: {count} ({percentage:.2f}%)")
    print()
    
packages = data_ingestion()
stats = statistics(packages)
generate_report(stats)