from queries import q10

from . import IO_FUNCS
from . import customer
from . import lineitem
from . import nation
from . import orders

tool = "pandas[pyarrow]"
fn = IO_FUNCS[tool]
print(q10.query(fn(customer), fn(nation), fn(lineitem), fn(orders)))

tool = "polars[lazy]"
fn = IO_FUNCS[tool]
print(q10.query(fn(customer), fn(nation), fn(lineitem), fn(orders)).collect())

tool = "pyarrow"
fn = IO_FUNCS[tool]
print(q10.query(fn(customer), fn(nation), fn(lineitem), fn(orders)))

tool = "dask"
fn = IO_FUNCS[tool]
print(q10.query(fn(customer), fn(nation), fn(lineitem), fn(orders)).compute())
