from faker import Faker

from api.create import CreateApi

fake = Faker()


def test_update_items():
    id = 3
    name = fake.name()
    job = fake.job()
    response = CreateApi().create_item(id, name, job)
    print(response)
