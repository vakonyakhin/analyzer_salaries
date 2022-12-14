FROM "python:slim-buster"

ENV SJ_KEY =v3.r.134950175.096fd8e380b90ba4c12093d1988f82e0db91be66.bc679cd162966a5239f7221003248fc452f3b102

WORKDIR   /home/app/python/analyze_salary 
    
COPY . .

RUN  pip install -U pip \
     pip install -r requirements.txt

CMD ["python", "main.py"]

