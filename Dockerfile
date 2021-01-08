FROM mengdong/test-rapids:latest

RUN . /opt/conda/etc/profile.d/conda.sh \
    && conda activate rapids \
    && pip install -U gcsfs

ADD rapids_opt2.py /rapids
ADD entrypoint.sh /rapids

WORKDIR /rapids

ENTRYPOINT ["bash", "entrypoint.sh"]