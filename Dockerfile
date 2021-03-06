FROM python:3.7
MAINTAINER SeungWon "recordable0711@gmail.com"
ENV TZ=Asia/Seoul

COPY . /LabS
WORKDIR /LabS
RUN pip install -r requirements.txt
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
EXPOSE 8000

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:8000", "--preload", "run:api_app"]
