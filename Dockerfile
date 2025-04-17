FROM python:3.13.1
WORKDIR /nasa_info_ui
COPY . /nasa_info_ui
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "./src/Space_Information.py", "--server.port=8501", "--server.address=0.0.0.0"]
