# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y wget build-essential && \
    wget https://www.sqlite.org/2023/sqlite-autoconf-3430000.tar.gz && \
    tar xvfz sqlite-autoconf-3430000.tar.gz && \
    cd sqlite-autoconf-3430000 && \
    ./configure --prefix=/usr/local && \
    make && \
    make install && \
    cd / && \
    rm -rf /sqlite-autoconf-3430000 && \
    rm /sqlite-autoconf-3430000.tar.gz

# Update library path
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
ENV OPENAI_API_KEY=""

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run main.py when the container launches
CMD streamlit run main.py
