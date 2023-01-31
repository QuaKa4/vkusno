from api.delete import DeleteApi


def test_update_items():
    response = DeleteApi().delete_item()
    print(response)
