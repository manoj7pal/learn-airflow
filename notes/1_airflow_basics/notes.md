# Airflow Architecture

## Core Components

Airflow has seven main components that work together to orchestrate data pipelines:

- **API Server** - Serves the Airflow UI and provides endpoints for Workers to communicate with the Airflow DB
- **Metadata Database** - Stores all metadata related to your Airflow instance, including users and tasks
- **Scheduler** - Monitors and schedules your pipelines
- **Executor** - Defines how and on which system tasks are executed
- **DAG File Processor** - Retrieves and parses DAG files from the DAGs directory
- **Queue** - Holds tasks that are ready to be executed
- **Worker(s)** - Executes the instructions defined in each task

## DAG Execution Flow

Airflow runs DAGs through six sequential steps:

1. **DAG Detection** - The DAG File Processor constantly scans the DAGs directory for new files (default: every 5 minutes)
2. **DAG Processing** - After detection, the DAG is processed and serialized into the metadata database
3. **Schedule Check** - The scheduler checks for DAGs that are ready to run in the metadata database (default: every 5 seconds)
4. **Task Queuing** - Once a DAG is ready to run, its tasks are placed into the executor's queue
5. **Task Retrieval** - When a worker becomes available, it retrieves a task to execute from the queue
6. **Task Execution** - The worker executes the assigned task

## DAG Structure

A DAG consists of four core parts:

- **Import Statements** - Define the specific operators or classes needed for the DAG
- **DAG Definition** - Calls the DAG object and defines properties such as name and schedule
- **DAG Body** - Defines tasks with their specific operators
- **Dependencies** - Defines the execution order of tasks using bitshift operators (`>>` for downstream, `<<` for upstream)

### Task Dependencies

Tasks within a DAG can be positioned as either upstream or downstream relative to other tasks, establishing the workflow execution order.