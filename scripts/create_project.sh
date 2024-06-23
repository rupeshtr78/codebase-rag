#!/bin/bash

# Base Directory
ROOT_DIR="langchain"
mkdir $ROOT_DIR

# Subdirectories
mkdir -p $ROOT_DIR/document_loaders
mkdir -p $ROOT_DIR/document_splitters
mkdir -p $ROOT_DIR/chroma
mkdir -p $ROOT_DIR/chains
mkdir -p $ROOT_DIR/prompts
mkdir -p $ROOT_DIR/interfaces

# __init__.py files
touch $ROOT_DIR/__init__.py
touch $ROOT_DIR/document_loaders/__init__.py
touch $ROOT_DIR/document_splitters/__init__.py
touch $ROOT_DIR/chroma/__init__.py
touch $ROOT_DIR/chains/__init__.py
touch $ROOT_DIR/prompts/__init__.py
touch $ROOT_DIR/interfaces/__init__.py

# Others
touch $ROOT_DIR/document_loaders/generic_loader.py
touch $ROOT_DIR/document_splitters/recursive_character_text_splitter.py
touch $ROOT_DIR/chroma/vector_store_retriever.py
touch $ROOT_DIR/chains/create_chains.py
touch $ROOT_DIR/chains/combine_documents.py
touch $ROOT_DIR/prompts/chat_prompt_template.py
touch $ROOT_DIR/interfaces/cli.py
touch $ROOT_DIR/interfaces/ui.py

# Main file
touch main.py


echo "Directories and files have been created."
