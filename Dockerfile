from python
WORKDIR /website
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]

