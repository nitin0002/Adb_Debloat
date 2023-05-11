'''
Sort the packages in the CSV file and save the sorted list to a new CSV file
'''
import pandas as pd
def packageSorted():
    # Load CSV file into a DataFrame
    df = pd.read_csv('packages.csv')

    # Sort the packages by name
    df_sorted = df.sort_values('package_name')

    # Write sorted DataFrame to a new CSV file
    df_sorted.to_csv('sorted_packages.csv', index=False)
