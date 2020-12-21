# 데이터 엔지니어링 기본 실습
> 본 레포지토리를 데이터 엔지니어링 실습을 위한 노트북 위에서 스파크 3.0 실습을 할 수 있는 도커 이미지 입니다


## 히스토리
* v1.0 (2020/12/09) 스파크 3.0 환경에서 노트북 기동이 가능한 이미지 생성
* v1.0 (2020/12/09) MySQL, MongoDB 및 인코딩 등 기본 로컬라이제이션 적용
* v1.1 (2020/12/10) Delta Lake 라이브러리 설치 및 예제 노트북 추가


## 도커 컴포즈를 통한 실행
> 아래의 docker-compose logs 명령을 통해 획득한 URL(http://127.0.0.1:8888/?token=19742e3a83a3f2eb1ce9db319b24dd64ed2722a8cdbc97d9)으로 접속합니다
```bash
$ git clone https://github.com/psyoblade/data-engineer-training.git && cd data-engineer-training
$ docker-compose up -d
$ docker-compose logs notebook
```

## 스파크 예제 실습
* [스파크 스트리밍 예제](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-stream-1.html)
