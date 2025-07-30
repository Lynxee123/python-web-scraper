# Use a lightweight base Python image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy project files into the container
COPY requirements.txt .
COPY scraper.py .
COPY output ./output

# Install Python dependencies
RUN pip install -r requirements.txt

# Run the scraper
# CMD ["python", "scraper.py"]
CMD ["bash"]