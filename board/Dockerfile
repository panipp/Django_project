FROM python:3.6
WORKDIR /board
ADD ./requirements.txt /board/requirements.txt

# RUN apk update && \
#     apk add --no-cache graphviz postgresql-libs unixodbc postgresql postgresql-contrib && \
#     apk add --no-cache jpeg-dev zlib-dev linux-headers && \
#     apk add --no-cache --virtual .build-deps gcc git musl-dev postgresql-dev unixodbc-dev && \
#     apk --update add gcc make g++ zlib-dev && \
#     python3 -m pip install -r /board/requirements.txt --no-cache-dir && \
#     apk --purge del .build-deps
RUN pip3 install -r /board/requirements.txt
COPY . /board/
