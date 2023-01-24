FROM ubuntu:latest
ENV VERSION=1.2.0
RUN apt-get update && apt-get install -y python-is-python3 vim zip unzip
COPY zip_job.py /tmp/
CMD ["/bin/bash", "-c", "echo $(uname -o) $(uname -m) && ls /tmp/zip_job.py"]
