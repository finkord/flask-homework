# Use the official Alpine image as the base image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Create a virtual environment and activate it
RUN python3 -m venv venv
RUn source venv/bin/activate

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Generate initial database data and
# Run the application
CMD flask --app dashboard init-db && flask run