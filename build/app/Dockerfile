FROM python:3.7.5
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code


ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


ADD entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]
