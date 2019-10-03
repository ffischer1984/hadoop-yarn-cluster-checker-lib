FROM python:3.7.3

LABEL "repository"="https://github.com/ffischer1984/hadoop-yarn-cluster-checker-lib"


COPY hadoop_yarn_cluster_checker_model /app
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
RUN cd /app
RUN pip install -r requirements.txt
RUN python -m pytest test --junitxml=./test-reports/coverage.xml

ENTRYPOINT ["/entrypoint.sh"]

