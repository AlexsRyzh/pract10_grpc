import os
from beanie import init_beanie
from app.model.User import User
from motor.motor_asyncio import AsyncIOMotorClient


async def init():
    client = AsyncIOMotorClient(
        os.getenv("MONGODB_URL")
    )

    await init_beanie(
        database=client.auth,
        document_models=[User]
    )
