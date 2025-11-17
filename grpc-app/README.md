# GRPC App


```bash
python -m grpc_tools.protoc \
    -I=app/proto \
    --python_out=app \
    --grpc_python_out=app \
    app/proto/glossary.proto
```