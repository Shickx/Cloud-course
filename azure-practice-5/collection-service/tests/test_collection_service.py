from collection_service.services.class_service import get_classes

def test_get_classes_returns_list():
    result = get_classes()

    assert isinstance(result, list)