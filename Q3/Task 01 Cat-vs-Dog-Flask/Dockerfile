FROM python:alpine
MAINTAINER Waleed Butt "waleed3072@gmail.com"
COPY . ~/src
WORKDIR ~/src
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["./__init__.py"]