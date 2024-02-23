FROM python:3.11-slim

WORKDIR /python-docker

COPY . .
RUN pip install -r requirements.txt && pip cache purge

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]