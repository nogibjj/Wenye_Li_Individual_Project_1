"""
    library file
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/drug-use-by-age/drug-use-by-age.csv"

def load_dataset():
    return pd.read_csv(dataset)

def describe_dataset():
    return pd.read_csv(dataset).describe()

def create_histogram():
    dataset = load_dataset()
    plt.figure(figsize=(8, 6))
    
    # Plotting the histogram
    plt.hist(dataset['alcohol_use'], bins=10, edgecolor='black')
    plt.xlabel('Alcohol Use (%)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Alcohol Use')
    
    # Show plot
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def create_line_chart():
    dataset = load_dataset()
    data_selected = dataset[['age', 'marijuana_use']]

    plt.figure(figsize=(10, 6))
    plt.plot(data_selected['age'], data_selected['marijuana_use'], label='Marijuana Use (%)', marker='o', color='g')

    plt.xlabel('Age')
    plt.ylabel('Marijuana Use (%)')
    plt.title('Trend of Marijuana Use by Age')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def create_bar_chart():
    dataset = load_dataset()
    data_selected = dataset[['age', 'cocaine_use']]

    plt.figure(figsize=(10, 6))
    plt.bar(data_selected['age'], data_selected['cocaine_use'], color='orange')

    plt.xlabel('Age')
    plt.ylabel('Cocaine Use (%)')
    plt.title('Cocaine Use by Age')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

