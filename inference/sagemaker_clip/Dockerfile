FROM python:3.10

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*


RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py && python get-pip.py
      
        
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY src /opt/program
WORKDIR /opt/program

COPY requirements.txt .

RUN pip3 install -r requirements.txt