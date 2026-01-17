# Import library
from airflow.sdk import DAG, task
from pendulum import datetime

# Define DAG Context Manager
with DAG(
    dag_id = 'my_dag_2',
    schedule = '@daily',
    start_date = datetime(2026, 1, 1),
    description = 'My second DAG example',
    tags = ['example', 'second_dag'],
    max_consecutive_failed_dag_runs = 3
):
    # Python task definition
    @task
    def task_a():
        print("This is Task A")

    task_a()