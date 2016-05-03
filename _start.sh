docker run -it --rm --name grattis \
  -e app_id='<YOURS>' \
  -e app_secret='<YOURS>' \
  -e user='<YOURS>' \
  -v $HOME/projects/facebook/grattis.py:/usr/src/app/grattis.py \
  facebook bash
