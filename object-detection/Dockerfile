FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 libgl1-mesa-glx && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "objectDetection.py"]


# docker run -d --name your-container-name --device /dev/video0 -v objectDetection.py:/app/objectDetection.py your-image-name

