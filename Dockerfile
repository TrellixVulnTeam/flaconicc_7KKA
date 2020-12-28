FROM python:3
ADD api.py /
ADD webapi.py /
RUN pip install pystrich
COPY requirements.txt /
RUN pip3 install --trusted-host pypi.python.org -r /requirements.txt
CMD [ "python", "./api.py" ]
CMD [ "python", "./webapi.py" ]