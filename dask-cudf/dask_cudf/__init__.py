from .core import (
    DataFrame,
    Series,
    from_cudf,
    from_dask_dataframe,
    concat,
    from_delayed,
)
from .io import read_csv, read_orc, read_json, read_parquet
from . import backends

import cudf
from cudf._version import get_versions

__version__ = get_versions()["version"]
del get_versions

__all__ = [
    "DataFrame",
    "Series",
    "from_cudf",
    "from_dask_dataframe",
    "concat",
    "from_delayed",
]

if not hasattr(cudf.DataFrame, "mean"):
    cudf.DataFrame.mean = None
del cudf
