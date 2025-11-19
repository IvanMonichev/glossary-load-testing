from app.load_ids import load_term_ids

REST_HOST = "http://exp-fastapi-service:4010"
GRPC_HOST = "exp-grpc-service:50051"

TERM_IDS = load_term_ids()
