# Dockerfile
FROM python:3.11

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . . 

# Run FastAPI with uvicorn
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
