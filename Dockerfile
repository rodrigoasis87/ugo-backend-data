FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV APP=undefined
ENV PORT=8081

RUN chmod +x runner.sh

EXPOSE $PORT

CMD ["./runner.sh"]
