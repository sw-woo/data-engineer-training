#!/bin/bash
rm spark/notebooks/*.html
docker exec -it notebook jupyter nbconvert --to html work/pyspark\*.ipynb
mv spark/notebooks/*.html spark/notebooks/html
