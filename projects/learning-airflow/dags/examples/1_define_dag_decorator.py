# Importing dag decorator
from airflow.sdk import dag
from pendulum import datetime

# Define DAG Object
@dag(
        dag_id = 'my_dag_1',
        schedule = '@daily',
        start_date = datetime(2026, 1, 18),
        description = 'My first DAG using the new SDK',
        tags = ['example', 'de3velopment'],
        max_consecutive_failed_dag_runs = 3
)
def my_dag():
    pass

my_dag()