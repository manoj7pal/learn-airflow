# XComs (Cross-Communications)

## Overview
XComs are a native Airflow feature designed to enable data sharing between tasks. They function by storing messages in the Airflow metadata database, allowing downstream tasks to retrieve results from upstream tasks.

## Key Concepts
- **Structure:** An XCom record consists of a **key**, **value**, **timestamp**, **task_id**, **dag_id**, and **run_id**.
- **Serialization:** Any data stored in XComs must be **JSON serializable**.
- **Creation:** By default, returning a value from a Python function (in a PythonOperator/TaskFlow API) automatically creates an XCom with the key `return_value`.
- **Methods:**
  - `xcom_push`: Explicitly pushes data with a custom key.
  - `xcom_pull`: Retrieves data from specific task IDs or multiple tasks simultaneously.

## Usage & Limitations
- **Use Case:** Best suited for sharing **small amounts of metadata** (e.g., file paths, status flags, dates, or API references).
- **Visualization:** XCom values and properties can be viewed directly in the Airflow UI under the **Admin > XComs** tab.
- **Storage Limits:** The maximum size of an XCom is dictated by the underlying database:
  - **SQLite:** ~2GB
  - **PostgreSQL:** ~1GB
  - **MySQL:** ~64KB (default configuration often limits to 64KB, though technically larger blobs are possible, the text implies strict limits).

## Best Practices
- **Avoid Large Data:** XComs are **unsuitable** for passing large datasets (e.g., DataFrames).
- **Alternative:** For heavy data processing, use XCom to pass a reference (like a path to S3 or GCS) and trigger an external processing job (e.g., Spark) to handle the actual data.

Thank you for tuning in. See you in the next module.

# JSON Serialization

**JSON serialization** is the process of converting a data object (like a dictionary, list, or class instance) into a JSON (JavaScript Object Notation) string format. This allows the data to be stored, transmitted over a network (e.g., via APIs), or saved to a file, and then reconstructed (deserialized) later.

In the context of **Airflow XComs**, data must be JSON serializable because XComs are stored in the Airflow metadata database, which typically handles simple text or JSON blobs.

### JSON Serializable vs. Non-Serializable

| Category | Definition | Python Examples |
| :--- | :--- | :--- |
| **JSON Serializable** | Data types that have a direct mapping to JSON standards and can be automatically converted by standard libraries (like Python's `json` module). | -  **Primitives:** `str`, `int`, `float`, `bool` (`True`/`False`), `None`<br>-  **Collections:** `dict` (with string keys), `list`, `tuple` (converts to array)<br>-  **Nested Structures:** Lists of dicts, dicts of lists, etc. |
| **JSON Non-Serializable** | Complex objects or types that do not have a standard string representation in JSON. These will raise a `TypeError` if you try to serialize them directly. | -  **Custom Objects:** Class instances (e.g., `MyClass()`)<br>-  **Dates:** `datetime`, `date` objects (unless converted to strings)<br>-  **Files:** File handlers, sockets, database connections<br>-  **Dataframes:** Pandas `DataFrame` (unless using `.to_json()`)<br>-  **Sets:** `set` (must be converted to list) |

### Examples

**1. Serializable (Works)**
```python
import json

data = {
    "task_id": "process_data",
    "retries": 3,
    "success": True,
    "tags": ["etl", "daily"]
}

json_string = json.dumps(data) 
# Result: '{"task_id": "process_data", "retries": 3, "success": true, "tags": ["etl", "daily"]}'
```

**2. Non-Serializable (Fails)**
```python
import json
from datetime import datetime

data = {
    "start_time": datetime.now()  # datetime objects are NOT natively JSON serializable
}

# Raises TypeError: Object of type datetime is not JSON serializable
json.dumps(data)
```

**How to fix Non-Serializable data for Airflow XComs:**
To store non-serializable objects (like dates) in XComs, you must convert them to a serializable format first (e.g., convert `datetime` to an ISO string).

```python
# Fix: Convert to string first
data = {
    "start_time": datetime.now().isoformat() 
}
json.dumps(data) # Works!
```