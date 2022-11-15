# Base image.
FROM python:3.7

# Working directory.
WORKDIR /code

# Copy dependencies file to working directory.
COPY requirements.txt requirements.txt

# Install dependencies.
RUN pip install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm

# Copy file to working directory.
COPY garden.py garden.py

CMD ["python3", "garden.py"]
