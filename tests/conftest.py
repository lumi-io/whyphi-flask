import pytest
from api import create_app, mongo

@pytest.fixture(scope="session")
def test_client():
    app = create_app(test_config=True)
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
    mongo.db.postings.delete_many({})
