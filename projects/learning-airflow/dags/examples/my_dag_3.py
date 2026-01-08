from airflow.sdk import DAG, task, chain, chain_linear

from pendulum import datetime

# Define the default arguments
default_args = {
    'retries': 3,
}

# Define DAG Context Manager
with DAG(
    dag_id = 'my_dag_3',
    schedule = '@weekly',
    start_date = datetime(2026, 2, 1),
    description = 'My third DAG example',
    tags = ['example', 'third_dag'],
    max_consecutive_failed_dag_runs = 5,
    default_args = default_args
):
    # Python task definitions
    @task()
    def print_a():
        print("This is Task A in the example DAG pipeline.")

    @task
    def print_b():
        print("This is Task B in the example DAG pipeline.")
        
    @task
    def print_c():
        print("This is Task C in the example DAG pipeline.")

    @task
    def print_d():
        print("This is Task D in the example DAG pipeline.")

    @task
    def print_e():
        print("This is Task E in the example DAG pipeline.")

    @task
    def print_f():
        print("This is Task F in the example DAG pipeline.")
    
    @task
    def print_g():
        print("This is Task G in the example DAG pipeline.")

    # Define task dependencies using chain
    # chain_linear(
    #     print_a(), 
    #     [print_b(), print_c(), print_d()], 
    #     [print_e(), print_f()]
    # )

    # More Flexible way of defining dependencies
    a = print_a()
    d = print_d()
    group_1 = [print_b(), print_c(), d]

    a >> group_1
    group_1 >> print_e()
    group_1 >> print_f()
    d >> print_g()