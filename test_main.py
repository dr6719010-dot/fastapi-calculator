"""Unit tests for FastAPI endpoints."""

import pytest
from fastapi.testclient import TestClient
from main import app, calculation_history


client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_history():
    """Clear history before each test."""
    calculation_history.clear()
    yield
    calculation_history.clear()


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_home_endpoint(self):
        """Test home endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        assert "Calculator API is live" in response.json()["message"]


class TestCalculateEndpoint:
    """Tests for calculate endpoint."""
    
    def test_calculate_sum(self):
        """Test sum calculation."""
        response = client.post("/calculate", json={
            "operation": "sum",
            "numbers": [1, 2, 3]
        })
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "sum"
        assert data["result"] == 6
        assert "timestamp" in data
    
    def test_calculate_product(self):
        """Test product calculation."""
        response = client.post("/calculate", json={
            "operation": "product",
            "numbers": [2, 3, 4]
        })
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "product"
        assert data["result"] == 24
    
    def test_calculate_difference(self):
        """Test difference calculation."""
        response = client.post("/calculate", json={
            "operation": "difference",
            "numbers": [10, 3, 2]
        })
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "difference"
        assert data["result"] == 5
    
    def test_calculate_division(self):
        """Test division calculation."""
        response = client.post("/calculate", json={
            "operation": "division",
            "numbers": [10, 2]
        })
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "division"
        assert data["result"] == 5
    
    def test_calculate_logarithm(self):
        """Test logarithm calculation."""
        response = client.post("/calculate", json={
            "operation": "log",
            "numbers": [1, 2.718281828]
        })
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "log"
        assert isinstance(data["result"], list)
        assert len(data["result"]) == 2
    
    def test_calculate_logarithm_with_base(self):
        """Test logarithm calculation with base."""
        response = client.post("/calculate", json={
            "operation": "log",
            "numbers": [1, 10, 100],
            "base": 10
        })
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "log"
    
    def test_invalid_operation(self):
        """Test invalid operation."""
        response = client.post("/calculate", json={
            "operation": "invalid",
            "numbers": [1, 2, 3]
        })
        assert response.status_code == 422  # Pydantic validation error

    
    def test_empty_list(self):
        """Test empty numbers list."""
        response = client.post("/calculate", json={
            "operation": "sum",
            "numbers": []
        })
        assert response.status_code == 400
        assert "cannot be empty" in response.json()["detail"]
    
    def test_division_by_zero(self):
        """Test division by zero error."""
        response = client.post("/calculate", json={
            "operation": "division",
            "numbers": [10, 0]
        })
        assert response.status_code == 400
        assert "division by zero is not allowed" in response.json()["detail"]


class TestHistoryEndpoint:
    """Tests for history endpoint."""
    
    def test_history_empty(self):
        """Test history with no calculations."""
        response = client.get("/history")
        assert response.status_code == 200
        data = response.json()
        assert data["history"] == []
        assert data["total_calculations"] == 0
    
    def test_history_after_calculation(self):
        """Test history after calculation."""
        client.post("/calculate", json={
            "operation": "sum",
            "numbers": [1, 2, 3]
        })
        
        response = client.get("/history")
        assert response.status_code == 200
        data = response.json()
        assert len(data["history"]) == 1
        assert data["total_calculations"] == 1
        assert data["history"][0]["operation"] == "sum"
        assert data["history"][0]["result"] == 6
    
    def test_history_multiple_calculations(self):
        """Test history with multiple calculations."""
        for i in range(3):
            client.post("/calculate", json={
                "operation": "sum",
                "numbers": [i, i+1]
            })
        
        response = client.get("/history")
        assert response.status_code == 200
        data = response.json()
        assert len(data["history"]) == 3
        assert data["total_calculations"] == 3
