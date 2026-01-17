from airflow.sdk import DAG, task
from airflow.sdk.exceptions import AirflowException

from datetime import datetime

with DAG(
    dag_id = 'example_task_test',
    description='An example DAG to demonstrate task testing',
    tags=['example', 'testing'],

    schedule='@daily',
    start_date = datetime(2026, 1, 1),

    catchup = False,
    max_consecutive_failed_dag_runs = 3
):
    @task
    def my_task(val):
        # raise AirflowException("This is a test exception")
        print(val)
        return 42
    
    my_task(80)
