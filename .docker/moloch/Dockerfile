# ----------------------------------------------------------------------------------------
# This container just executes some python code to parse the URL of the Moloch/arkime
# release, which is then copied to the actual container.
#
#

FROM python:3 AS urlparser

WORKDIR /app
COPY parse.py .
RUN curl -OL https://s3.amazonaws.com/files.molo.ch
RUN /usr/bin/python3 parse.py files.molo.ch > /result.txt

# ----------------------------------------------------------------------------------------

FROM almalinux

ENV ES_HOST elasticsearch
ENV ES_PORT 9200
ENV MOLOCH_LOCALELASTICSEARCH no
ENV MOLOCH_ELASTICSEARCH "http://"$ES_HOST":"$ES_PORT
ENV MOLOCH_INTERFACE eth0
ENV MOLOCH_PASSWORD blabla
ENV MOLOCHDIR "/data/moloch"
ENV CAPTURE off
ENV VIEWER on
ENV INITALIZEDB false
ENV WIPEDB false
ENV PATH "/data:/data/moloch/bin:${PATH}"

COPY --from=urlparser /result.txt .

RUN \
        dnf -y update && \
        dnf -y install epel-release dnf-plugins-core && \
        dnf config-manager --set-enabled powertools

RUN dnf -y update && \
dnf -y install \
  ethtool \
  file \
  libyaml-devel \
  perl-JSON \
  perl-libwww-perl \
  perl-LWP-Protocol-https

RUN mkdir -p /data
RUN curl -o arkime.rpm https://s3.amazonaws.com/files.molo.ch/$(cat /result.txt)
RUN rpm -i arkime.rpm

COPY /scripts /data
COPY /etc /data/moloch/etc
RUN chmod 755 /data/*.sh

EXPOSE 8005
WORKDIR /data/moloch

# I need to fix this: this container shouldn't run as root
# USER 1000
ENTRYPOINT ["/data/startmoloch.sh"]
