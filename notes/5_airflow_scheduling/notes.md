# Airflow Scheduling & Backfilling

## DAG Lifecycle & States
- **Initial State:** A DAG Run begins in the **Queued** state.
- **Running State:** It transitions to **Running** as soon as the first task begins execution.
- **Final State:** The run concludes as either **Success** or **Failure**, determined by the final state of its leaf tasks.

## Core Scheduling Parameters
Two primary parameters control when DAGs execute:
1. **Start Date (`start_date`):** Defines the timestamp from which the scheduler begins creating DAG Runs. It marks the beginning of the DAG's timeline.
2. **Schedule Interval (`schedule_interval`):** Determines the frequency of execution. It defines the `data_interval_start`, `data_interval_end`, and `logical_date` for each run.

## Historical Execution
- **Catchup:** A built-in mechanism that automatically runs all non-triggered DAG Runs between the `start_date` and the current time (or the last trigger time).
- **Backfilling:**
  - Allows users to run historical DAG Runs that were missed or need to be re-processed.
  - Can be triggered via the **Airflow CLI** to target specific data intervals, even those outside the standard schedule.
  - Useful for re-running existing DAG Runs to correct data issues.

## Defining Schedules
- **CRON Expressions:** Used for specific calendar-based times (e.g., "Every day at midnight").
- **Timedelta Objects:** Used for fixed-frequency intervals relative to the start date (e.g., "Every 3 days").
- **Timetables:** Advanced feature for defining complex, precise custom schedules beyond standard CRON capabilities.

## Best Practices
- **Static Start Date:** Always use a static, fixed datetime for the `start_date` (e.g., `datetime(2023, 1, 1)`). Avoid dynamic values like `datetime.now()`, which can confuse the scheduler and break execution logic.

Thank you for tuning in. See you in the next module.