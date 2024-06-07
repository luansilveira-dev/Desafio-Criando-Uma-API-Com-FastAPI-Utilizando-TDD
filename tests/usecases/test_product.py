from typing import List
from uuid import UUID
from bson.binary import Binary, UuidRepresentation
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase
from store.core.exception import NotFoundException
import pytest


@pytest.mark.asyncio
async def test_usecases_create_should_return_success(product_in):

    # product_in.id = Binary(product_in.id.bytes, UuidRepresentation.STANDARD)
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    # assert result.id == product_in.id
    assert result.name == "Iphone 14 pro Max"


@pytest.mark.asyncio
async def test_usecases_get_should_return_success(product_id, product_inserted):

    #product_id_ = UUID(bytes=product_inserted.id)

    result = await product_usecase.get(id=product_inserted.id)
    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"


@pytest.mark.asyncio
async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))
    assert (
        err.value.message
        == "Produto não encontrado com filtro: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


@pytest.mark.asyncio("products_inserted")
async def test_usecases_query_should_return_success():
    result = await product_usecase.query()
    assert isinstance(result, List)


@pytest.mark.asyncio
async def test_usecases_update_should_return_success(
    product_id, product_up, product_inserted
):
    # product_id_binary = UUID(bytes=product_inserted.id)

    product_up.price = "7.500"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


@pytest.mark.asyncio
async def test_usecases_delete_should_return_success(product_id, product_inserted):
    # product_id_binary = UUID(bytes=product_inserted.id)

    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


@pytest.mark.asyncio
async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))
    assert (
        err.value.message
        == "Produto não encontrado com filtro: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )
