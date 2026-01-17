from airflow.sdk import DAG, task, Context
from pendulum import datetime

# Define the default arguments
default_args = {
    'retries': 3,
}

# Define DAG Context Manager
with DAG(
    dag_id = 'my_dag_4',
    description = 'My Fourth DAG example',
    schedule = '@daily',
    start_date = datetime(2026, 1, 1),
    tags = ['example', 'development'],
    catchup = False,
    max_consecutive_failed_dag_runs = 5,
    default_args = default_args
):
    # Python task definitions
    @task()
    def print_a(**context: Context):
        val = 10
        context['ti'].xcom_push(key = 'xc_print_a_val', value = val)

        print("This is Task A in the example DAG pipeline.")

    @task
    def print_b(**context: Context):
        val = context['ti'].xcom_pull(task_ids='print_a', key='xc_print_a_val')
        print(f'Value pulled from Task A: {val}')
        
        print("This is Task B in the example DAG pipeline.")
        
    
    # More Flexible way of defining dependencies
    a = print_a()
    b = print_b()

    a >> b
    