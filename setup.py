from setuptools import setup, find_packages

setup(
    name='langchain-rag-pkg',  # Replace with your package name
    version='0.1.0',  # Replace with your package version
    packages=find_packages(),
    install_requires=[
        'langchain_community',
        'langchain_text_splitters',
        'langchain_chroma',
        'langchain_openai',
        'langchain_core',
        'langchain',
        'click',
        'streamlit',
        'numpy<2,>=1',
        'esprima',
        'pandas',
        'tree-sitter',
        'tree-sitter-languages',
        'pytest',
    ],
    author='Rupesh',  # Replace with your name
    author_email='rupeshtr78@gmail.com',  # Replace with your email
    description='Lanchain Rags',  # Replace with your package description
    url='https://github.com/rupeshtr78/ai-lab',  # Replace with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)

# python setup.py install
# pip install .
# pip install -e .  # Install in editable mode
