FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x run_analysis.sh
RUN mkdir -p resultados

CMD ["./run_analysis.sh"]
