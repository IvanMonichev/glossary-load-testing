#!/bin/bash

grpcurl -plaintext \
  -d '{ "id": "691b65bca36cd161609d8248" }' \
  localhost:50051 \
  glossary.GlossaryService.GetTerm

grpcurl -plaintext \
  -d '{ "query": "data", "page": 1, "page_size": 20 }' \
  localhost:50051 \
  glossary.GlossaryService.SearchTerms