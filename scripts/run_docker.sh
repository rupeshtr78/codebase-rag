#!/bin/bash
docker build -t codebase-rag:v01 .

docker run -v /gits/gits-rupesh/codebase-rag/src:/app/codebase -d -p 8501:8501 -e OPENAI_API_KEY=xxxx --name codebase-rag codebase-rag:v01

