from typing import TYPE_CHECKING, List
from langchain_community.document_loaders.generic import GenericLoader, Document
from langchain_community.document_loaders.parsers import LanguageParser
from logging import getLogger

logger = getLogger(__name__)

if TYPE_CHECKING:
    from langchain_openai import OpenAIEmbeddings


class CodeBaseLoader:
    def __init__(self, path: str, language: str):
        self.path = path
        self.language = language

    def doc_loader(self) -> List[Document]:
        loader = GenericLoader.from_filesystem(
            self.path,
            glob="**/*",
            suffixes=[".js", ".ts", ".go", ".py", ".java", ".c", ".cpp", ".h", ".hpp", ".rs", ".rb", ".php", ".html", ],
            exclude=["Dockerfile", "vendor", "docker-compose.yml", "Makefile", "README.md", "build", "dist",
                     "node_modules", "target", "out", ".git", ".idea", ".vscode", ".venv", ".pytest_cache", ".tox",
                     ".mypy_cache", ".cache", ".eggs", ".ipynb_checkpoints", ".gitignore", ".dockerignore",
                     ".gitattributes", ".editorconfig", ".pre-commit-config.yaml", ".flake8", ".pylintrc",
                     ".gitlab-ci.yml", ".travis.yml", ".github", ".gitignore", ".gitattributes", ".editorconfig",
                     ".pre-commit-config.yaml", ".flake8", ".pylintrc", ".gitlab-ci.yml", ".travis.yml", ".github"],
            parser=LanguageParser(language=self.language, parser_threshold=500),
        )
        documents = loader.load()
        logger.info(f"Loaded {len(documents)} documents.")
        return documents
