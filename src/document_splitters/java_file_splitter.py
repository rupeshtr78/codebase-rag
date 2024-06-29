from langchain.text_splitter import Language
from langchain_community.document_loaders.parsers.language.java import JavaSegmenter
from langchain.text_splitter import TokenTextSplitter, RecursiveCharacterTextSplitter
import re

java_source_code = ""

CHUNK_QUERY = """
    [
        (class_declaration) @class
        (interface_declaration) @interface
        (enum_declaration) @enum
        
    ]
""".strip()

# Create an instance of JavaSegmenter
java_segmenter = JavaSegmenter(java_source_code)

# Extract functions and classes
chunks = java_segmenter.extract_functions_classes()
print(chunks)

# Correct import for JavaParser if needed (assuming it's from a similar package)
# from langchain_community.document_loaders.parsers.language.java import JavaParser

# java_parser = JavaParser()
# splits = java_parser.split_text(java_source_code)

def split_java_file(content):
    # Split on class definitions, method definitions, and blank lines
    splits = re.split(r'(public|private|protected)?\s*(class|interface|enum)|(\w+\s+\w+\s*([^)]*)\s*{)|\n\s*\n', content)
    return [split.strip() for split in splits if split and split.strip()]

splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = splitter.split_text(java_source_code)

java_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.JAVA, chunk_size=1000, chunk_overlap=200)
splits = java_splitter.split_text(java_source_code)
