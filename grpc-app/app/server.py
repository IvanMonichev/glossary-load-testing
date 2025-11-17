import grpc
from bson import ObjectId
from grpc_reflection.v1alpha import reflection

import glossary_pb2
import glossary_pb2_grpc

from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["glossary"]
terms = db.get_collection("terms")


class GlossaryService(glossary_pb2_grpc.GlossaryServiceServicer):

    async def GetTerm(self, request, context):
        term = await terms.find_one({"_id": ObjectId(request.id)})

        if not term:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Term not found")
            return glossary_pb2.GetTermResponse()

        return glossary_pb2.GetTermResponse(
            term=glossary_pb2.Term(
                id=str(term["_id"]),
                title=term["title"],
                description=term["description"],
                tags=term["tags"],
            )
        )

    async def SearchTerms(self, request, context):
        skip = (request.page - 1) * request.page_size

        cursor = terms.find(
            {"title": {"$regex": request.query, "$options": "i"}}
        ).skip(skip).limit(request.page_size)

        items = []
        async for term in cursor:
            items.append(
                glossary_pb2.Term(
                    id=str(term["_id"]),
                    title=term["title"],
                    description=term["description"],
                    tags=term["tags"],
                )
            )

        return glossary_pb2.SearchTermsResponse(terms=items)


async def serve():
    server = grpc.aio.server()
    glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(
        GlossaryService(), server
    )

    SERVICE_NAMES = (
        glossary_pb2.DESCRIPTOR.services_by_name['GlossaryService'].full_name,
        reflection.SERVICE_NAME,
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:50051")
    print("Listening on port 50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
