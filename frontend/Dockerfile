FROM python:3.9-slim

# Working directory within the container
WORKDIR /app

# Copy the files to the working directory
COPY . .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Define the command to start the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]
