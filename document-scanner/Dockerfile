# FROM python:3
# WORKDIR /app
# COPY requirements.txt .
# RUN pip3 install --no-cache-dir -r requirements.txt
# COPY . .
# CMD [ "python3", "documentScanner.py" ]

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 libgl1-mesa-glx && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "documentScanner.py"]


# docker run -d --name sampleScanner --device /dev/video0 -v documentScanner.py:/app/documentScanner.py sample1

