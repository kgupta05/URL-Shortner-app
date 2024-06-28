FROM python:3.8-slim-buster
MAINTAINER abdulraheem.akv@gmail.com
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV NAME World
CMD ["python", "app.py"]
