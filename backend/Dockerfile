FROM python:3.9-slim

# Working directory within the container
WORKDIR /app

# Copy the files to the working directory
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to start the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:flask_app"]
