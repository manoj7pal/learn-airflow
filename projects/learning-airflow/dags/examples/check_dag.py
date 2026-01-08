from airflow.sdk import DAG, task

from pendulum import datetime, duration

default_args = {
    'retries': 3
}

with DAG(
    dag_id = 'check_dag',
    description = 'DAG to check data',
    schedule = '@daily', # everyday at midnight # duration(month=2, days=1, hours=13, minutes=30, seconds=30 ) 
    start_date = datetime(2025, 1, 1),
    tags = ['data_engineering'],
    max_consecutive_failed_dag_runs = 3,
    default_args = default_args,
    catchup = False
):
    
    @task.bash
    def create_file():
        return 'echo "Hi there!" >/tmp/dummy'

    @task.bash
    def check_file_exists():
        return 'test -f /tmp/dummy'

    @task()
    def read_file():
        print(open('/tmp/dummy', 'rb').read())

    create_file() >> check_file_exists() >> read_file()

    
