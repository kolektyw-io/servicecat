FROM python:latest
COPY api/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY api /servicecat
WORKDIR /servicecat
RUN chmod +x run.sh
EXPOSE 8000