FROM python:3.10 
EXPOSE 5000
WORKDIR /app
COPY Pipfile Pipfile.lock /app/ 
RUN pip install pipenv
RUN pipenv install --system --deploy
COPY . .
ENV FLASK_APP=src/app.py
CMD ["flask", "run", "--host=0.0.0.0"]