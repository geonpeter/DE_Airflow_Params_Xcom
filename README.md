# Parameters, XCom and Context using a simple DAG (Directed Acyclic Graph
This project demonstrates basic Airflow concepts including Parameters, XCom, and Context using a simple DAG (Directed Acyclic Graph).

## Overview
This Airflow DAG demonstrates how to:
  1. Pass input parameters to a DAG
  2. Use XCom to share data between tasks
  3. Utilize the Airflow context in tasks

## Concepts Demonstrated

  1. Parameters (Params)
  - Used to pass input values to your DAG when triggered
  - Set in the Airflow web UI or API when manually triggering the DAG
  - Accessed in tasks via the context['params'] dictionary
  2. XCom (Cross-communication)
  - Used to pass small amounts of data between tasks within a DAG
  - Data is pushed to XCom in one task and pulled in another
  - Utilized via xcom_push() and xcom_pull() methods of the TaskInstance

  3. Context
  - Provides task-specific information and utilities
  - Passed to task functions when provide_context=True
  - Contains params, ti (TaskInstance), and other Airflow objects

  ## DAG Structure
  1. task_1: Receives input from params and pushes it to XCom
  2. task_2: Pulls data from XCom (pushed by task_1) and prints it

