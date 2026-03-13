#Base image
FROM python:3.9-slim

#set the working directory inside the container
WORKDIR /app

#copy requirements file 
COPY requirements.txt .

#install all dependencies from requirements.txt
RUN pip install -r requirements.txt

#Copy the code 
COPY main.py .

#Port expose
EXPOSE 5000

#env
ENV PYTHONUNBUFFERED=1

#serve this application
CMD ["python", "main.py"]