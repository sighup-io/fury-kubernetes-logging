FROM elasticsearch:6.4.1

RUN elasticsearch-plugin install repository-s3 -b

RUN echo -Des.allow_insecure_settings=true >> /usr/share/elasticsearch/config/jvm.options
