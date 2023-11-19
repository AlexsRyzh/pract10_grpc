import os

from gen.python.service_pb2 import *
from gen.python.service_pb2_grpc import *
from app.model.User import *
import grpc
import jwt


class Server(AuthServiceServicer):
    async def Login(self, request, context):

        if (
            request.login == '' or
            request.password == ''
        ):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Argument can't be an empty")
            return Response()

        user = await User.find(
            User.login == request.login,
            User.password == request.password
        ).first_or_none()

        if user is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return Response()

        token = jwt.encode({"id": str(user.id)}, os.getenv('SECRETE_KEY'), algorithm="HS256")

        return Response(
            token=token
        )

    async def Registration(self, request, context):

        if (
            request.login == '' or
            request.password == '' or
            request.username == ''
        ):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Argument can't be an empty")
            return Response()

        user = await User.find(
            User.login == request.login,
            User.password == request.password
        ).first_or_none()

        print(user)
        if user is not None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User already exist")
            return Response()

        user = User(
            username=request.username,
            login=request.login,
            password=request.password
        )

        await user.create()

        token = jwt.encode({"id": str(user.id)}, os.getenv('SECRETE_KEY'), algorithm="HS256")

        return Response(
            token=token
        )
