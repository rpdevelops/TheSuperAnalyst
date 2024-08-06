# Use the Python 3.12.4 base image
FROM python:3.12.4

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose port 8084
EXPOSE 8084

# Specify the command to run your application
# Replace `app.py` with the entry point of your application
CMD ["python", "main.py"]