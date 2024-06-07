import pytest
from tests.fectories import product_data
from fastapi import status

@pytest.mark.asyncio
async def test_controller_create_should_return_success(client, product_url):
    response = await client.post(product_url, json=product_data())
    content = response.json()
    breakpoint()
    assert response.status_code == status.HTTP_201_CREATED
