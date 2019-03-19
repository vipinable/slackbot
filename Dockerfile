FROM scratch
ADD alpine-minirootfs-3.9.2-x86_64.tar.gz /
ADD slackbot.py .
RUN apk add --no-cache python2
RUN apk add --no-cache py-pip
RUN pip install --no-cache-dir websocket-client==0.47.0
RUN pip install --no-cache-dir slackclient==1.3.0 
CMD [ "python", "slackbot.py" ]
