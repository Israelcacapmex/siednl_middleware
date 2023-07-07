FROM python:3.8.10-slim-buster
WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install python-dotenv
RUN pip install Flask
RUN pip install -U flask-cors
RUN pip install PyJWT
RUN pip install pandas
RUN pip install openpyxl
RUN pip install pandas
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
