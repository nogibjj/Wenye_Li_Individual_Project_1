"""
Main cli or app entry point
"""

from mylib.lib import (
    describe_dataset,
    describe_median,
    create_histogram,
    create_line_chart,
    create_bar_chart,
)


def general_describe():
    """Save dataset statistics to Markdown and return the description."""
    with open("summary.md", "w") as file:
        description = describe_dataset()
        median_values = describe_median()
        file.write("# Dataset Statistics\n")
        file.write(description.to_markdown())
        file.write("\n## Median Values\n")
        file.write(median_values.to_markdown())
    return description


def general_visualize():
    """Generate and save visualizations as PNG files."""
    create_histogram("alcohol_use_histogram.png")
    create_line_chart("marijuana_use_line_chart.png")
    create_bar_chart("cocaine_use_bar_chart.png")


def save_to_markdown():
    """Append visualizations and other information to Markdown."""
    with open("summary.md", "a") as file:
        # Append images to the Markdown
        file.write("\n## Visualizations\n")
        file.write("### Alcohol Use Histogram\n")
        file.write("![Alcohol Use](alcohol_use_histogram.png)\n")

        file.write("### Marijuana Use Line Chart\n")
        file.write("![Marijuana Use](marijuana_use_line_chart.png)\n")

        file.write("### Cocaine Use Bar Chart\n")
        file.write("![Cocaine Use](cocaine_use_bar_chart.png)\n")


if __name__ == "__main__":
    general_describe()
    general_visualize()
    save_to_markdown()
