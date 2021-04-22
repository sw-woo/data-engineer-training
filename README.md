# 데이터 엔지니어링 기본 실습
> 본 레포지토리를 데이터 엔지니어링 실습을 위한 노트북 위에서 스파크 3.0 실습을 할 수 있는 도커 이미지 입니다


## 히스토리
* v1.0 (2020/12/09) 스파크 3.0 환경에서 노트북 기동이 가능한 이미지 생성
* v1.0 (2020/12/09) MySQL, MongoDB 및 인코딩 등 기본 로컬라이제이션 적용
* v1.1 (2020/12/10) Delta Lake 라이브러리 설치 및 예제 노트북 추가
* v1.2 (2021/04/22) Docker 및 Docker Compose 설치 가이드 추가


## 도커 및 컴포즈 설치
### 1. [스크립트를 통한 도커 설치](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)
* 도커 스크립트를 다운로드 합니다
```bash
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```
* 도커를 sudo 명령어 없이 설치하고자 하는 경우 설정을 변경합니다 
```bash
$ sudo usermod -aG docker <your-user>
```

### 2. [우분투 패키지를 통한 도커 설치](https://docs.docker.com/engine/install/ubuntu/)
> 스크립트를 통해 설치한 경우는 바로 "컴포즈 설치"를 진행하시면 됩니다

* 패키지 업데이트 및 도커 공식 GPG 키를 다운로드 합니다
```bash
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
* 안정화 버전의 레포지토리를 추가 및 설치합니다
```bash
$ echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### 3. 특정 버전의 도커를 설치
* 설치가능한 버전을 확인 후 버전을 명시하여 설치합니다
```bash
$ apt-cache madison docker-ce
$ sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```
* 테스트 도커 이미지를 실행합니다
```bash
$ sudo docker run hello-world
```

### 4. 도커 제거
* 패키지 삭제 및 컨테이너 설치 경로까지 삭제합니다
```bash
$ sudo apt-get purge docker-ce docker-ce-cli containerd.io
$ sudo rm -rf /var/lib/docker
$ sudo rm -rf /var/lib/containerd
```

### 5. [우분투 환경에 최신 도커 컴포즈 설치](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)
* 아래의 명령으로 최신 버전(1.29.1)을 설치합니다
```bash
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
* 실행 바이너리 퍼미션 변경 및 링크를 추가합니다
```bash
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
* 제대로 설치되었는지 버전을 확인합니다
```bash
$ docker-compose --version
docker-compose version 1.29.1, build 1110ad01
```


## 도커 컴포즈를 통한 실행
> 아래의 docker-compose logs 명령을 통해 획득한 URL(http://127.0.0.1:8888/?token=19742e3a83a3f2eb1ce9db319b24dd64ed2722a8cdbc97d9)으로 접속합니다
```bash
$ git clone https://github.com/psyoblade/data-engineer-training.git && cd data-engineer-training
$ docker-compose up -d
$ docker-compose logs notebook
```

## 스파크 예제 실습
* 스파크 기본 명령어 실습
  - [1. 스파크 기본 명령어 이해](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-basic-1.html)
  - [2. 기본 연산 다루기](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-basic-2.html)
  - [3. 데이터 타입 다루기](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-basic-3.html)
  - [4. 조인 연산 다루기](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-basic-4.html)
  - [5. 집계 연산 다루기](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-basic-5.html)
  - [6. 스파크 JDBC to MySQL](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-basic-6.html)
* 스파크 델타 레이크 실습
  - [1. 스파크 델타 레이크 기본](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-delta-1.html)
  - [2. 스파크 델타 레이크 실습](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-delta-2.html)
* 스파크 스트리밍 실습
  - [1. 스파크 스트리밍 예제](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/pyspark-stream-1.html)
* 러닝 스파크 실습
  - [5. UDF 다루기](http://htmlpreview.github.io/?https://github.com/psyoblade/data-engineer-training/blob/master/spark/notebooks/html/learning-spark-ch05.html)
