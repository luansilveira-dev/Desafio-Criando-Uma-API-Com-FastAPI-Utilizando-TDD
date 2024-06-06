from typing import List
import pymongo
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from bson.binary import Binary, UuidRepresentation
from store.core.exception import BaseException, NotFoundException


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        product_model.id = Binary(product_model.id.bytes, UuidRepresentation.STANDARD)
        await self.collection.insert_one(product_model.model_dump())
        
        return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        _id = Binary(id.bytes, UuidRepresentation.STANDARD)
        result = await self.collection.find_one({"id": _id})

        if not result:
            raise NotFoundException(message=f"Produto não encontrado com filtro: {id}")

        return ProductOut(**result)

    async def query(self) -> List[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        _id = Binary(id.bytes, UuidRepresentation.STANDARD)

        result = await self.collection.find_one_and_update(
            filter={"id": _id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        _id = Binary(id.bytes, UuidRepresentation.STANDARD)
        product = await self.collection.find_one({"id": _id})

        if not product:
            raise NotFoundException(message=f"Produto não encontrado com filtro: {id}")

        result = await self.collection.delete_one({"id": _id})

        return True if result.deleted_count > 0 else False


product_usecase = ProductUsecase()
