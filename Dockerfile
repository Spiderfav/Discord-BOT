FROM python:3.8

WORKDIR /usr/src/app

ADD Discord.py ./

ADD contestants.txt ./

ADD enf.txt ./

RUN pip3 install discord

CMD [ "python", "./Discord.py" ]
