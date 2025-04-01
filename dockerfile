# Use Python 3.11 as the base image
FROM python:3.11

# Set the working directory
WORKDIR /testing

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install required dependencies
RUN apt-get update && apt-get install -y wget unzip curl xvfb

# Detect system architecture
RUN arch=$(dpkg --print-architecture) && \
    if [ "$arch" = "amd64" ]; then \
        wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome.gpg && \
        echo 'deb [signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
        apt-get update && apt-get install -y google-chrome-stable; \
    elif [ "$arch" = "arm64" ]; then \
        wget -q -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
        dpkg --add-architecture arm64 && \
        dpkg -i chrome.deb || true && \
        apt-get install -f -y && rm chrome.deb; \
    else \
        echo "Unsupported architecture: $arch" && exit 1; \
    fi

# Install `webdriver-manager` for automatic ChromeDriver handling
RUN pip install --no-cache-dir webdriver-manager

# Set environment variable for display (for headless mode)
ENV DISPLAY=:99

# Run pytest
CMD ["pytest"]
