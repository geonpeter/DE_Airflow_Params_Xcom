from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
dag = DAG(
    'dag_params_xcom',
    schedule_interval=None,  # Fixed the typo
    default_args=default_args,
    tags=['dev'],
    params={'input': 'Default Message'},
)

# Task 1: Push a message to XCom
def task_1(**kwargs):
    received_msg = kwargs['params']['input']
    kwargs['ti'].xcom_push(key='msg', value=received_msg)
    
# Task 2: Pull the message from XCom and print it
def task_2(**kwargs):
    received_msg = kwargs['ti'].xcom_pull(task_ids='task_1', key='msg')
    print(f"Received message from task_1 is: {received_msg}")

# Task 1: PythonOperator to run task_1 function
task1 = PythonOperator(
    task_id='task_1',
    python_callable=task_1,
    dag=dag,
)

# Task 2: PythonOperator to run task_2 function
task2 = PythonOperator(
    task_id='task_2',
    python_callable=task_2,
    dag=dag,
)

# Set task dependencies
task1 >> task2
