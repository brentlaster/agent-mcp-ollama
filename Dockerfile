
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    curl git python3 python3-pip build-essential

RUN curl -fsSL https://ollama.com/install.sh | sh
ENV PATH="/root/.ollama/bin:${PATH}"

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app

CMD ["bash"]
