from airflow.sdk import DAG, task
from airflow.sensors.base import PokeReturnValue

from datetime import datetime


with DAG(
    dag_id = 'sensor_example_dag',
    description = 'DAG demonstrating sensor functionality',

    schedule ='@daily',
    start_date = datetime(2026, 1, 1),
    tags = ['sensor', 'example'],

    catchup = False,
    max_consecutive_failed_dag_runs = 3
):
    @task
    def get_value():
        val = -10
        return val
    
    @task
    def print_value(val):
        print(f'Retrieved Value: {val}')

    @task.sensor(
        poke_interval=5, 
        timeout = 15,
        mode = 'poke', # 'reschedule'
        soft_fail = True
    )
    def wait_for_positive_value(value) -> PokeReturnValue:
        if value > 0:
            condition_met = True
        else:
            condition_met = False

        return PokeReturnValue(is_done = condition_met, xcom_value = value)


    value = wait_for_positive_value(get_value())
    print_value(value)