"""
Main cli or app entry point
"""

from mylib.lib import *

def general_describe():
    # Save dataset statistics to Markdown
    with open('test.md', 'w') as file:
        description = describe_dataset()
        file.write("# Dataset Statistics\n")
        file.write(description.to_markdown())  # Convert DataFrame to Markdown format
    return description

def general_visualize():
    # Save visualizations to PNG files
    create_histogram("alcohol_use_histogram.png")
    create_line_chart("marijuana_use_line_chart.png")
    create_bar_chart("cocaine_use_bar_chart.png")

def save_to_markdown():
    with open('test.md', 'a') as file:
        file.write("## Test section\n")
        file.write("This is a test entry in the markdown file.")

if __name__ == '__main__':
    print(general_describe())
    general_visualize()
    save_to_markdown()
