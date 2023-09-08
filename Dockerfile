FROM hitokizzy/geezram:slim-buster

RUN git clone -b main https://github.com/SendiAp/Rose-Pro /home/rose/
WORKDIR /home/rose

RUN wget https://raw.githubusercontent.com/SendiAp/Rose-Pro/main/requirements.txt \
    && pip3 install --no-cache-dir -U -r requirements.txt \
    && rm requirements.txt
    
CMD bash start
