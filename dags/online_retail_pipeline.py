"""
## Astronaut ETL example DAG

This DAG queries the list of astronauts currently in space from the
Open Notify API and prints each astronaut's name and flying craft.

There are two tasks, one to get the data from the API and save the results,
and another to print the results. Both tasks are written in Python using
Airflow's TaskFlow API, which allows you to easily turn Python functions into
Airflow tasks, and automatically infer dependencies and pass data.

The second task uses dynamic task mapping to create a copy of the task for
each Astronaut in the list retrieved from the API. This list will change
depending on how many Astronauts are in space, and the DAG will adjust
accordingly each time it runs.

For more explanation and getting started instructions, see our Write your
first DAG tutorial: https://www.astronomer.io/docs/learn/get-started-with-airflow

![Picture of the ISS](https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2010/02/space_station_over_earth/10293696-3-eng-GB/Space_Station_over_Earth_card_full.jpg)
"""

from airflow import DAG
# with operator need to set dag = dag for relationships
from airflow.operators.bash import BashOperator

def create_data_pipeline_dag(dagid):

    # Create a DAG
    dag = DAG(
        f'{dagid}',
        description = 'A Pipeline for Online Retail',
        schedule_interval=None,  # Set to None for manual trigger
        catchup=False,
    )

    # Define the task
    source_quality_check = BashOperator(
        task_id='Source_Quality_Check',
        bash_command='python /usr/local/airflow/include/great_expectation/data_source_quality.py',
        dag = dag
    )


    create_staging_table = BashOperator(
        task_id='Create_Staging_Table',
        bash_command='python /usr/local/airflow/include/great_expectation/create_staging_table.py',
        dag = dag
    )

    create_dwh_table = BashOperator(
        task_id='Create_DWH_Table',
        bash_command='dbt run --project-dir /usr/local/airflow/include/dbt',
        dag = dag
    )

    source_quality_check >> create_staging_table >> create_dwh_table

    # Return the created DAG
    return dag

# Create the DAG when the file is imported
data_pipeline_dag = create_data_pipeline_dag('PL_Main_Online_Retail')