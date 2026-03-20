from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("UpSetPlot")
except PackageNotFoundError:
    __version__ = "unknown"

from .data import (
    from_contents,
    from_indicators,
    from_memberships,
    generate_counts,
    generate_samples,
)
from .plotting import UpSet, plot
from .reformat import query

__all__ = [
    "UpSet",
    "generate_counts",
    "generate_samples",
    "plot",
    "from_memberships",
    "from_contents",
    "from_indicators",
    "query",
]
