# Airflow Sensors Best Practices

## Introduction
In Apache Airflow, a sensor is a specialized task that waits for an external event or condition to be met before allowing downstream tasks to proceed. This makes them essential for orchestrating workflows dependent on external systems like file arrivals, API responses, or database updates [[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)][[Airflow Docs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html)].

## Core Configuration Best Practices
When using sensors, proper configuration is essential to prevent resource exhaustion and ensure efficient DAG execution:

- **Timeout:** Always define a meaningful `timeout` parameter. The default is 7 days, which is excessively long. Analyze your specific use case to determine a realistic maximum wait time (e.g., 30 minutes or 2 hours) to fail fast if data doesn't arrive [[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)][[Orchestra](https://www.getorchestra.io/guides/airflow-concepts-airflow-sensors-explained)].
- **Poke Interval:** Tune the `poke_interval` (frequency of checks) based on your latency requirements. Do not use the default 60 seconds if a 5-minute delay is acceptable. A longer interval reduces the load on your Airflow scheduler and database [[Orchestra](https://www.getorchestra.io/guides/airflow-concepts-airflow-sensors-explained)][[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)].

## Choosing the Right Mode
The `mode` parameter determines how the sensor utilizes worker resources:

- **`mode='poke'`:** 
  - **Use when:** The expected wait time is short (e.g., < 5 minutes) or the check frequency must be very high (e.g., every second).
  - **Behavior:** The sensor occupies a worker slot continuously for its entire duration.
  - **Risk:** Can lead to deadlocks if too many sensors occupy all available worker slots [[Airflow Docs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html)][[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)].

- **`mode='reschedule'`:**
  - **Use when:** The expected wait time is long or uncertain.
  - **Behavior:** The sensor releases the worker slot between checks, freeing it up for other tasks. While waiting, its status changes to `up_for_reschedule`.
  - **Benefit:** Prevents "sensor deadlock" where running sensors block other tasks from executing [[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)][[Airflow Docs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html)].

## Advanced Optimization: Deferrable Operators
For modern Airflow environments (2.2+), **Deferrable Operators** (Async Operators) are the gold standard for sensors:
- **How they work:** They offload the waiting process to a lightweight "Triggerer" service, releasing the worker entirely (consuming *zero* worker slots while waiting).
- **Recommendation:** Whenever possible, use deferrable versions of sensors (often enabled via `deferrable=True` or by using specific async classes) instead of standard `reschedule` mode for maximum resource efficiency [[Reddit](https://www.reddit.com/r/dataengineering/comments/1ii6z6y/apache_airflow_best_practices_ama/)][[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)].

## Failure Handling
- **Soft Fail:** Use `soft_fail=True` if the sensor's failure (timeout) should not fail the entire DAG run but rather skip downstream tasks. This is useful for optional data dependencies [[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)].

## `exponential_backoff` Option

In Airflow sensors, **`exponential_backoff`** is a boolean parameter (`True` or `False`) that controls how the wait time between checks (pokes) changes over time.

### How it Works
When you set `exponential_backoff=True`:
1.  **Progressive Waiting:** Instead of checking at a fixed interval (e.g., every 60 seconds), the sensor will wait for progressively longer periods after each unsuccessful check.
2.  **Algorithm:** The wait time typically doubles after each attempt (e.g., 60s, 120s, 240s...), though the exact formula includes some randomization (jitter) to prevent "thundering herd" problems where many sensors retry at the exact same moment.
3.  **Base Interval:** The starting point for the calculation is your defined `poke_interval`.

### Why use it?
It is highly recommended for sensors interacting with **external systems** (like APIs, databases, or S3 buckets) to:
*   **Reduce Load:** Prevents hammering a busy or down system with constant requests.
*   **Rate Limiting:** Helps avoid hitting API rate limits during outages or slow periods.
*   **Efficiency:** If a job is taking a long time, there's no need to check it every minute; checking less frequently as time goes on saves resources.

### Example
```python
# With exponential_backoff=True and poke_interval=60
# Check 1: Wait 60s
# Check 2: Wait ~120s
# Check 3: Wait ~240s
# ... up to timeout
```

## Key Takeaways
- **Completion:** Sensors wait for a specific event or condition to be met before completing [[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)].
- **Timeouts:** Sensors time out after 7 days by default; always define a more appropriate `timeout` value [[Airflow Docs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html)].
- **Checking Frequency:** Sensors check the condition at every `poke_interval` (default is 60 seconds) [[Orchestra](https://www.getorchestra.io/guides/airflow-concepts-airflow-sensors-explained)].
- **Resource Usage:** While waiting in `poke` mode, a sensor continuously occupies a worker slot [[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)].
- **Reschedule Mode:** Use `mode='reschedule'` for long-running sensors to free up worker slots; the status will show as `up_for_reschedule` while waiting [[Airflow Docs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html)].
- **TaskFlow API:** You can easily create custom sensors using the `@task.sensor` decorator [[Astronomer](https://www.astronomer.io/docs/learn/what-is-a-sensor)].