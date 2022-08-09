# serasa-challenge
selection process serasa experian

# Docker
```
docker build -t santander-chalange:latest .

docker run -it santander-chalange /bin/sh
or
docker run -it --env-file .env santander-chalange /bin/sh


python src/main_train.py -d data/train_data/train.csv
```