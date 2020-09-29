FROM python:3.8

RUN pip install fastapi uvicorn 'pydantic[email]'

EXPOSE 8500

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8500", "--reload"]