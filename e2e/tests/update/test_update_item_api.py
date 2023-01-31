from faker import Faker

from api.update import UpdateApi

fake = Faker()


def test_update_items():
    id = 3
    name = fake.name()
    job = fake.job()
    response = UpdateApi().update_put_item(id, name, job)
    assert response['name'] == name, 'actual name is not match expected name'
    assert response['job'] == job, 'actual job is not match expected job'


def test_update_item():
    id = 3
    name = fake.name()
    job = fake.job()
    response = UpdateApi().update_put_item(id, name, job)
    assert response['name'] == name, 'actual name is not match expected name'
    assert response['job'] == job, 'actual job is not match expected job'
