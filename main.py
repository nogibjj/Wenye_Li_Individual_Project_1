"""
Main cli or app entry point
"""

from mylib.lib import *

def general_describe():
    return load_dataset().describe()

def general_visualize():
    create_histogram()
    create_line_chart()
    create_bar_chart()

if __name__ == '__main__':
    print(general_describe())
    general_visualize()
