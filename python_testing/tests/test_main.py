import pytest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import OrderProcessing


@pytest.fixture
def order_system():
    return OrderProcessing()


class TestOrderProcessing:

    def test_create_order(self, order_system):
        order = order_system.create_order(101, 50)
        assert order["amount"] == 50
        assert order["status"] == "pending"

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

    def test_get_order_status(self, order_system):
        order_system.create_order(103, 75)
        assert order_system.get_order_status(103) == "pending"
        assert order_system.get_order_status(999) == "not found"

    @pytest.mark.skip(reason="Payment processing is slow, skipping for now")
    def test_process_payment(self, order_system):
        order_system.create_order(104, 200)
        assert order_system.process_payment(104) in [True, False]

    @pytest.mark.slow
    def test_slow_payment_processing(self, order_system):
        order_system.create_order(105, 150)
        result = order_system.process_payment(105)
        assert result in [True, False]
        assert order_system.get_order_status(105) in ["paid", "failed"]

    def test_mocked_payment_processing(self, order_system):
        order_system.create_order(106, 300)

        with patch("main.random.choice", return_value=True):
            assert order_system.process_payment(106) is True
            assert order_system.get_order_status(106) == "paid"
