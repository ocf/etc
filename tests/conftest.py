import pytest


@pytest.fixture(autouse=True)
def etc(fs):
    """Use pyfakefs in every test case"""
    fs.add_real_directory('configs', target_path='/etc/ocf', read_only=True)

    # This is here for vhost configs, but should be removed once they are read
    # from this repo via ocflib instead of read from NFS or the staff web
    # userdir. The statement above this will handle loading from the local
    # files instead of /etc/ocf once that's the case.
    fs.add_real_directory(
        'configs', target_path='/home/s/st/staff/vhost', read_only=True,
    )
