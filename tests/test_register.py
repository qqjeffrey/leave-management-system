from fastapi.testclient import TestClient
from app.main import app
from app.domain.models.user import User
from unittest.mock import MagicMock
from app.use_cases import register_user

def test_register_user_with_mock(monkeypatch):
    # 建立一個 mock 的 RegisterUserUseCase 實例
    mock_use_case = MagicMock()
    mock_user = User(
        email="test@example.com",
        name="Test User",
        hashed_password="mockedhash"
    )
    mock_use_case.execute.return_value = mock_user

    # patch 掉原本的 DI function
    def mock_get_use_case():
        return mock_use_case

    # 將 mock DI 注入到 route 中
    from app.interfaces.routes import auth_router
    auth_router.get_register_user_use_case = mock_get_use_case

    client = TestClient(app)
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "name": "Test User",
        "password": "securepassword"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["name"] == "Test User"
    assert data["message"] == "Registration successful"

    # 驗證 mock 有被正確呼叫
    mock_use_case.execute.assert_called_once_with(
        email="test@example.com",
        name="Test User",
        password="securepassword"
    )
