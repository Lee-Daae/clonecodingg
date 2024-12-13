FROM python:3.13.0
#rsa 키 넣을 경로 생성
RUN mkdir /root/.ssh/
# 이미지를 가지는 사람은 private key또한 입수 가능
# 호스트의 파일 복사
ADD ./.ssh/id_rsa /root/.ssh/id_rsa

RUN chmod 600 /root/.ssh/id_rsa # 권한 추가

RUN touch /root/.ssh/known_hosts

RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR /home/

RUN echo "test"

RUN git clone git@github.com:Lee-Daae/pinterest.git

WORKDIR /home/pinterest/
# 필요한 기본 도구 설치
RUN apt-get update && apt-get install -y curl
# PDM 직접 설치
RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 -
# 경로 설정
ENV PATH="/root/.local/bin:$PATH"

RUN pdm import requirements.txt 

RUN pdm add gunicorn

RUN pdm add mysqlclient

#RUN echo "SECRET_KEY=django-insecure-ywc40v0ndy%srwmwoj0=3w^l1#%(v-@ferl89@33*_as@dd*h!" > .env

#RUN pdm run python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "pdm run python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy &&pdm run python manage.py migrate --settings=pragmatic.settings.deploy &&pdm run gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]