FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2021.03.4
RUN pip install git+https://github.com/bp-kelley/descriptastorus.git@d552f934757378a61dd1799cdb589a864032cd1b
RUN pip install tqdm==4.62.2
RUN pip install torch==1.9.0
RUN pip install scipy==1.7.1
RUN pip install scikit-learn==0.24.2

WORKDIR /repo
COPY ./repo
