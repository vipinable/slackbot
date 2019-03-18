FROM python:2
COPY slackbot.py .
RUN pip install --no-cache-dir websocket-client==0.47.0 
RUN pip install --no-cache-dir slackclient==1.3.0 
ENV PYTHONPATH /usr/local/lib/python2.7/site-packages
CMD [ "python", "slackbot.py" ]
