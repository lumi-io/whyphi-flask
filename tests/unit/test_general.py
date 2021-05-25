def test_homepage_with_fixture(test_client):
    """Testing to see if server is running."""
    response = test_client.get('/')
    assert response.status_code == 200