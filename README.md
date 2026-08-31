# pytest-lab

Simple pytest setup for `OrderProcessing` in `python_testing/main.py`.

## Setup

```bash
pip3 install pytest
```

## How the tests are written

File: `python_testing/tests/test_main.py`

1. Import pytest.
2. Import `patch` from `unittest.mock`.
3. Import the class under test: `OrderProcessing`.
4. Put tests in a class (`TestOrderProcessing`).
5. Use `@pytest.mark.parametrize` with an `expected_exception` column.
6. If an exception is expected, assert it with `pytest.raises`. Otherwise run the call and check the result.

Example:

```python
import pytest
from unittest.mock import patch
from main import OrderProcessing

@pytest.mark.parametrize("order_id, amount, expected_exception", [
    (102, 100, None),
    (102, -50, ValueError),
    (102, 0, ValueError),
])
def test_create_order_scenarios(self, order_system, order_id, amount, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            order_system.create_order(order_id, amount)
    else:
        order = order_system.create_order(order_id, amount)
        assert order["amount"] == amount
```

Payment success is forced in one test by mocking `random.choice`.

## Run tests

```bash
pytest python_testing/tests/test_main.py
```
