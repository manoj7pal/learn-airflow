# Airflow UI

## Module Summary
Thank you for joining this module on the Airflow UI. We explored the core interface components that allow users to monitor and manage data pipelines effectively.

### Key Views & Features
- **DAGs View**: The landing page upon logging in, providing a comprehensive list of all data pipelines (DAGs) in the Airflow instance.
- **Grid View**: Displays a history of tasks and DAG Run states for a specific DAG.
- **Graph View**: Visually represents task dependencies and workflow structure.
- **Code View**: Shows the serialized code of the pipeline stored in the database, allowing users to verify if recent modifications have been picked up by the scheduler.

### Debugging & Management
- **Task Failure**: In the event of a failure, users can navigate to the Grid or Graph view, access logs for the failed task, identify the error, and rerun the specific task.
- **Global Lists**: Users can view all historical executions across the instance by navigating to:
  - **DAGs View > Runs** (for a list of all DAG Runs)
  - **DAGs View > Task Instances** (for a list of all individual task executions)

Thank you for tuning in. See you in the next module