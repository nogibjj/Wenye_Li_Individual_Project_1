"""
Test goes here
"""

import os
from main import general_describe, general_visualize, save_to_markdown


def test_general_describe():
    """Test that the general_describe function works and outputs a description."""
    describe_test = general_describe()
    assert describe_test is not None

    assert os.path.exists("summary.md")
    with open("summary.md", "r") as file:
        content = file.read()
        assert "# Dataset Statistics" in content


def test_general_visualize():
    """Test that visualizations are created and saved as PNG files."""
    general_visualize()

    # Check if the PNG files are created
    assert os.path.exists("alcohol_use_histogram.png")
    assert os.path.exists("marijuana_use_line_chart.png")
    assert os.path.exists("cocaine_use_bar_chart.png")


def test_save_to_markdown():
    """Test that visualizations and content are appended to the Markdown file."""
    save_to_markdown()

    # Verify that images are referenced in the 'test.md' file
    assert os.path.exists("summary.md")
    with open("summary.md", "r") as file:
        content = file.read()
        assert "![Alcohol Use](alcohol_use_histogram.png)" in content
        assert "![Marijuana Use](marijuana_use_line_chart.png)" in content
        assert "![Cocaine Use](cocaine_use_bar_chart.png)" in content
