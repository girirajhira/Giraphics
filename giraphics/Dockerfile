
FROM registry.gitlab.com/islandoftex/images/texlive:latest

#RUN apt-get install -y texlive-latex-extra

RUN apt-get install -y librsvg2-bin

RUN apt-get install -y texlive-fonts-recommended texlive-latex-base texlive-latex-extra texlive-latex-recommended \
    dvisvgm

RUN apk add  --no-cache ffmpeg

WORKDIR /Giraphics

RUN pip3 install


