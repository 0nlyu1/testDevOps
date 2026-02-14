import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home_redirects_to_dashboard(client):
    # follow_redirects=False면 "리다이렉트(302)" 자체를 검사할 수 있음
    response = client.get('/', follow_redirects=False)

    # / 는 정상적으로 dashboard로 보내는 게 목표라 302가 맞음
    assert response.status_code in (301, 302)

    # 어디로 보내는지(Location 헤더) 확인
    location = response.headers.get("Location", "")
    assert location.endswith("/dashboard")
