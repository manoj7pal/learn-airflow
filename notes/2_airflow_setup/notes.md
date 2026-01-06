# Install & Setup Airflow

## Installation Methods

There are two primary ways to install Airflow on a local machine:

### 1. Python Package Index (PyPI)
- **Best for:** Users comfortable with Python and managing local Python environments.
- **Pros:** Native execution without container overhead.
- **Cons:** Requires significant manual configuration to get Airflow working correctly on a local machine.

### 2. Containerization Solutions (Docker, Podman)
- **Best for:** Users familiar with containerization workflows.
- **Pros:** Easier dependency management and isolation.
- **Cons:** May require customization of the container if specific fine-tuning is needed.

***

## The Astro CLI
The [Astro CLI](https://github.com/astronomer/astro-cli) is an open-source command line interface designed to simplify setting up, running, and managing Airflow. It includes built-in features to accelerate development.

- **Alternatives:** 
  - Native **Airflow CLI** (built-in).
  - [AirflowCTL](https://github.com/kaxil/airflowctl) (open-source project).
- **Installation:** Instructions for Mac, Windows, and Linux are available in the [official documentation](https://docs.astronomer.io/astro/cli/install-cli).

***

## Project Structure & Management

### Commands
Use the following Astro CLI commands to manage the project lifecycle:
- **Initialize:** `astro dev init` (Generates a new project structure)
- **Start:** `astro dev start`
- **Restart:** `astro dev restart`
- **Stop:** `astro dev stop`

### Directory Breakdown
When initializing a project, the Astro CLI generates a standard directory structure:

- **`dags/`**: Contains Python files for data pipelines (e.g., `example_dag_advanced`, `example_dag_basic`).
- **`include/`**: Stores supporting files like SQL queries, bash scripts, or Python functions to keep pipelines clean.
- **`plugins/`**: Used for customizing the instance by adding new operators or modifying the UI.
- **`tests/`**: Contains tests for data pipelines (utilizing tools like `pytest`).
- **`.dockerignore`**: Specifies files/folders to exclude from the Docker image build.
- **`.env`**: Configures the Airflow instance via environment variables.
- **`.gitignore`**: Specifies files to ignore in version control (crucial for excluding sensitive credentials).
- **`airflow_settings.yaml`**: Stores configurations (connections and variables) to ensure persistence when recreating the local environment.
- **`Dockerfile`**: Defines the Docker image build, specifying the Astro runtime image and Airflow version.
- **`packages.txt`**: Lists additional Operating System packages to install.
- **`README.md`**: Project instructions and information.
- **`requirements.txt`**: Specifies additional Python packages and versions to install.

***

## VSCode Integration
To enable features like correct syntax highlighting and autocompletion in VSCode, the instance must be run inside the Docker container. This requires the [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) extension.