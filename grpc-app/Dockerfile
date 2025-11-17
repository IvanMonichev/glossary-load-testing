FROM python:3.11-slim AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only proto first
COPY app/proto ./proto

# Generate pb files
RUN python -m grpc_tools.protoc \
    -I=proto \
    --python_out=. \
    --grpc_python_out=. \
    proto/glossary.proto

# Copy the rest of the app (NOW WITHOUT nesting)
COPY app/*.py ./

# Expose
EXPOSE 50051

CMD ["python", "server.py"]
