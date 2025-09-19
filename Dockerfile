# 1. Base image
FROM continuumio/miniconda3

# 2. Working directory
WORKDIR /app

# 3. Copy and create Conda environment
COPY environment.yml .
RUN conda env create -f environment.yml

# 4. Use Conda env in all subsequent commands
SHELL ["conda", "run", "-n", "airbnb-app", "/bin/bash", "-c"]

# 5. Copy project files
COPY . .

# 6. Expose Streamlit port
EXPOSE 8501

# 7. Run Streamlit app
CMD ["conda", "run", "-n", "airbnb-app", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
