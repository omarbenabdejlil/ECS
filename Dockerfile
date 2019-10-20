FROM python:3-alpine
MAINTAINER BENSAAD Anouar bensaad.tig@gmail.com
LABEL name ecs
LABEL src "https://github.com/omarbenabdejlil/ECS"
LABEL creator omarbenabdejlil
RUN apk add --no-cache git && \
    git clone https://github.com/omarbenabdejlil/ECS.git
WORKDIR ECS
RUN pip install --user --upgrade pip && \
pip install --user -r ./requirements.txt

VOLUME [ "/ecs" ]
ENTRYPOINT [ "python", "ecs.py" ]
CMD ["--help"]