"""Basic package initialization test."""

import agentprobe


def test_version() -> None:
    """Verify package version is defined."""
    assert agentprobe.__version__ == "0.1.0"
