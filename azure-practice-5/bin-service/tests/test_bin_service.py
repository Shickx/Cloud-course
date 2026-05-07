from bin_service.services.chef_service import get_chefs

def test_get_chefs_returns_list():
    result = get_chefs()

    assert result is not None
    assert isinstance(result, list)