# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
