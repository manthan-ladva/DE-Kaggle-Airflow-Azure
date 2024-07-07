from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from kaggle_download import run_kaggle_etl


default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date' : datetime(2020, 11, 8),
    'email' : ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


dag = DAG(
    'kaggle_dag',
    default_args=default_args,
    description='Our First DAG with ETL process!',
    schedule_interval=timedelta(days=1)
)



run_etl = PythonOperator(
    task_id = 'complete_kaggle_etl',
    python_callable = run_kaggle_etl,
    dag = dag
)

run_etl
