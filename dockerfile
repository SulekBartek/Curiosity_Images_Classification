FROM jupyter/minimal-notebook:latest

RUN mkdir mars_classification
RUN cd mars_classification
WORKDIR /mars_classification

ADD . mars_classification/

RUN pip install -r mars_classification/requirements.txt

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]