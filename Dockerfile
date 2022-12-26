FROM python:3.9-alpine3.17
EXPOSE 8080
COPY . .
RUN apk update
RUN apk add gcc musl-dev mariadb-connector-c-dev 
RUN pip3 install -r requirements.txt --no-cache-dir
RUN apk del gcc musl-dev
RUN pip install pymysql
WORKDIR ./mysite/
ADD cmd.sh /
RUN chmod +x /cmd.sh
CMD ["/cmd.sh"]
