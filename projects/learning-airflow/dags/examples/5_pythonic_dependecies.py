from airflow.sdk import DAG, task
from pendulum import datetime

# Define the default arguments
default_args = {
    'retries': 3,
}

# Define DAG Context Manager
with DAG(
    dag_id = 'my_dag_5',
    description = 'My Fifth DAG example',
    schedule = '@daily',
    start_date = datetime(2026, 1, 1),
    tags = ['example', 'development'],
    catchup = False,
    max_consecutive_failed_dag_runs = 5,
    default_args = default_args
):
    # Python task definitions
    @task
    def print_a():    
        val = 10
        return val # context['ti'].xcom_push(key = 'return_value', value = val)


    @task
    def print_b(val: int):
        print(f'Value pulled from Task A: {val}')
        return val**2

    @task
    def print_c(val: int):
        print(f'Value pulled from Task A in Task C: {val}')
        return val**3
    
    @task
    def print_d(val1: int, val2: int):
        print(f'Value pulled from Task B in Task C: {val1}')
        print(f'Value pulled from Task C in Task C: {val2}')

        print(f'Sum of values from Task B and Task C: {val1 + val2}')
        
    
    # Pythonic way of defining dependencies
    val = print_a()
    sq_val = print_b(val)
    cube_val = print_c(val)
    print_d(sq_val, cube_val)

    