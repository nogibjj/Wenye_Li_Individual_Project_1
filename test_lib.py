"""
Test goes here

"""
from mylib.lib import (
    load_dataset,
    describe_dataset,
    describe_median,
)


def test_load_dataset():
    """Test the load_dataset function."""
    dataset = load_dataset()
    assert dataset is not None
    assert len(dataset) > 0


def test_describe_dataset():
    """Test the describe_dataset function."""
    description = describe_dataset()
    assert description is not None
    assert len(description) > 0


def test_describe_median():
    """Test the describe_median function."""
    median_values = describe_median()
    assert median_values is not None
    assert len(median_values) > 0
