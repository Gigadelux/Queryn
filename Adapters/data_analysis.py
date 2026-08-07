# %%
import polars as pl

# %%
df = pl.read_parquet("data/embeddings/embeddings.parquet")
df.head()
# %%


def nan_report(df: pl.DataFrame) -> pl.DataFrame:
    """Per-column NaN/null counts. Polars has no labeled Series (no index),
    so this returns the practical equivalent of pandas' df.isna().sum():
    a two-column (column, nan_count) frame, sorted worst-first.

    Handles both plain float columns and fixed_size_list/Array embedding
    columns, where plain is_nan() can't reach elements inside the list.
    """
    exprs = []
    for name, dtype in df.schema.items():
        if dtype in (pl.Float32, pl.Float64):
            expr = (pl.col(name).is_null() | pl.col(name).is_nan()).sum()
        elif isinstance(dtype, pl.Array) and dtype.inner in (pl.Float32, pl.Float64):
            expr = (
                pl.col(name).is_null().sum()
                + pl.col(name).arr.eval(pl.element().is_nan()).arr.sum().sum()
            )
        else:
            expr = pl.col(name).is_null().sum()
        exprs.append(expr.alias(name))

    counts = df.select(exprs)
    return (
        counts.transpose(include_header=True, header_name="column", column_names=["nan_count"])
        .sort("nan_count", descending=True)
    )


# %%
nan_report(df)
# %%
