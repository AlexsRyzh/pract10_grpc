import logging
import os
import asyncio
from concurrent import futures
from app.server import *
from dotenv import load_dotenv
from gen.python.service_pb2_grpc import *
import grpc
from app.db.init_db import init

async def start():
    server = grpc.aio.server()
    add_AuthServiceServicer_to_server(
        Server(), server
    )
    server.add_insecure_port(f"[::]:{os.getenv('PORT')}")
    await init()
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(start())
