FROM python:3.7

# Create app directory
WORKDIR /app

# Install app dependencies
COPY code/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY code /app

EXPOSE 50000
CMD [ "python", "simpleapp.py" ]