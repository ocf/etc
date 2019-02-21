import pytest


@pytest.fixture(autouse=True)
def etc(fs):
    """Use pyfakefs in every test case"""
    fs.add_real_directory('configs', target_path='/etc/ocf')
