# Airflow CLI

## Module Summary
Thank you for joining this module on the Airflow CLI.  
We explored multiple ways to run the Airflow CLI and why it’s an important companion to the Airflow UI.

## Running the Airflow CLI
- Different approaches exist for running the CLI depending on how Airflow is installed (local install, containerized environments, managed platforms, etc.).
- Having CLI access is especially helpful when troubleshooting issues that are harder to diagnose from the UI alone.

## Essential “Getting Started” Commands
- We covered the core commands that are useful when first setting up and working with an Airflow environment.
- These commands help validate that Airflow services are working and that DAGs/tasks are being discovered correctly.

## Understanding Your Environment
- We learned how CLI commands can reveal details about the Airflow environment (configuration, metadata, and runtime context).
- Knowing these details helps with debugging tasks and diagnosing unexpected scheduling/execution behavior.

## Exporting and Importing Settings
- We explored how to export and import settings between Airflow environments.
- This helps with repeatable setups and migration workflows (for example, moving configurations from one environment to another).

## Backfill & Testing
- We covered the `backfill` command and why it can be tricky to run if CLI access is restricted.
- Alongside identifying DAG issues, we also learned how to test tasks to surface errors earlier in development.

## Why the CLI Matters
Airflow CLI is a very useful tool and provides options that are not available in the UI, especially for deep debugging and environment inspection.  
For additional context on how Airflow components work together (which helps interpret CLI output), see the Airflow fundamentals documentation. [airflow.apache](https://airflow.apache.org/docs/apache-airflow/2.10.5/tutorial/fundamentals.html)

# Additional Resources

For further reading and deeper dives into the topics discussed, explore the following resources:

## Environment & Configuration
*   **[Local Development Environment](https://academy.astronomer.io/local-development-environment):** A guide to setting up a local Airflow environment for testing and development.
*   **[Environment Variables](https://academy.astronomer.io/astro-module-environment-variables):** Learn how to configure your Airflow environment using variables.
*   **[Airflow Configuration](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html):** The official reference for all `airflow.cfg` parameters and settings.

## CLI Tools

*   **[CLI Commands](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html):** Comprehensive documentation for the native Airflow Command Line Interface.
*   **[Astro CLI](https://docs.astronomer.io/astro/cli/reference):** Reference guide for the Astro CLI, used for managing Astronomer deployments.

## Data & Connections
*   **[Airflow Variables](https://academy.astronomer.io/astro-runtime-variables-101):** Best practices for using Airflow Variables to store runtime configuration.
*   **[Airflow Connections](https://academy.astronomer.io/connections-101):** Learn how to securely manage connections to external systems and databases.

## Troubleshooting
*   **[Debugging DAGs](https://academy.astronomer.io/debug-dags):** Techniques and strategies for identifying and fixing issues in your data pipelines.