from locust import User, task, between, events
import grpc
import time
import random

import glossary_pb2
import glossary_pb2_grpc

from config import GRPC_HOST, TERM_IDS


class GrpcUser(User):
    wait_time = between(0.1, 0.5)

    def on_start(self):
        self.channel = grpc.insecure_channel(GRPC_HOST)
        self.stub = glossary_pb2_grpc.GlossaryServiceStub(self.channel)

    @task(7)
    def get_term(self):
        term_id = random.choice(TERM_IDS)
        req = glossary_pb2.GetTermRequest(id=term_id)

        start = time.time()
        success = True
        error_msg = ""

        try:
            self.stub.GetTerm(req)
        except Exception as e:
            success = False
            error_msg = str(e)

        total_time_ms = (time.time() - start) * 1000

        events.request.fire(
            request_type="gRPC",
            name="gRPC: GetTerm",
            response_time=total_time_ms,
            response_length=0,
            exception=None if success else error_msg
        )

    @task(3)
    def search_terms(self):
        req = glossary_pb2.SearchTermsRequest(
            query=random.choice(["a", "e", "tech", "data"]),
            page=random.randint(1, 5),
            page_size=20
        )

        start = time.time()
        success = True
        error_msg = ""

        try:
            self.stub.SearchTerms(req)
        except Exception as e:
            success = False
            error_msg = str(e)

        total_time_ms = (time.time() - start) * 1000

        events.request.fire(
            request_type="gRPC",
            name="gRPC: SearchTerms",
            response_time=total_time_ms,
            response_length=0,
            exception=None if success else error_msg
        )
