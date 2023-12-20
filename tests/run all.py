import pytest

# Run the tests in the desired order
pytest.main(
    ['test_sign_up.py', 'test_sign_in.py', 'test_contact_us.py', 'test_browse_deals.py', 'test_shopping_cart.py',
     'test_edit_email.py'])
