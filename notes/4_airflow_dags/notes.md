# DAG & Task Definition Best Practices

## DAG Configuration

When defining a DAG in Airflow, several key properties must be configured to ensure proper identification and scheduling:

- **Unique Identifier:** Every DAG must have a `dag_id` that is unique across the entire Airflow instance.
- **Start Date:** While optional (defaulting to `None`), setting a `start_date` is crucial for the scheduler to know when to begin processing.
- **Schedule Interval:** This optional parameter defines the frequency at which the DAG is triggered (e.g., cron expression or `@daily`).
- **Metadata:** It is strongly recommended to define a **description** and **tags** for every DAG. This improves discoverability and allows users to filter pipelines effectively in the UI.

## Task Creation

Tasks are the building blocks of your workflow. Follow these guidelines for defining them:

- **Operator Selection:** Before writing custom code, always check the [Astronomer Registry](https://registry.astronomer.io/) for existing providers and operators that fit your use case.
- **Unique Identifier:** Each task must have a `task_id` that is unique within its specific DAG.
- **Default Arguments:** You can apply common configurations (like `retries`, `owner`, or `start_date`) to all tasks in a DAG by passing a dictionary to the `default_args` parameter.

## Defining Dependencies

Properly defining the execution order is essential for a functional pipeline:

- **Bitshift Operators:** Use `>>` (downstream) and `<<` (upstream) to define relationships between tasks. These operators also support lists for fan-in/fan-out patterns.
- **Chain Helper:** Use the `chain()` function specifically when defining dependencies between two lists of tasks (e.g., pairwise dependencies) or for long linear sequences where bitshift syntax becomes repetitive.