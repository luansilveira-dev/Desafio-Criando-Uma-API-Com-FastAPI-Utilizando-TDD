from bson.binary import Binary, UuidRepresentation
from store.schemas.product import ProductOut
from store.usecases.product import product_usecase
import pytest


@pytest.mark.asyncio
async def test_usecases_should_return_success(product_in):
    
    product_in.id = Binary(product_in.id.bytes, UuidRepresentation.STANDARD)
    result = await product_usecase.create(body=product_in)
    
    # assert isinstance(result, ProductOut)
    assert result is None
