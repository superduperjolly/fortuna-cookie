# Base from Python 3.6.1
FROM python:3.6.1-slim

# Install necessary packages
RUN pip install pipenv==2018.11.26
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system

# Maintain workdir as 
WORKDIR /fortuna-cookie 

# Copy the program files
COPY . /fortuna-cookie

# Expose a port to the host
EXPOSE 5000

# Make the image run Python whatever happens
ENTRYPOINT ["python"]

# The default command to run 
CMD ["app.py"]
