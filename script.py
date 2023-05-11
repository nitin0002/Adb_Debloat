import subprocess
import pandas as pd

def adbScript():
    # Run ADB command to get package list
    result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], stdout=subprocess.PIPE)

    # Process the result and store in a DataFrame
    packages = [line.replace('package:', '').strip() for line in result.stdout.decode().split('\n') if line]
    df = pd.DataFrame(packages, columns=['package_name'])

    # Write DataFrame to CSV file
    df.to_csv('packages.csv', index=False)