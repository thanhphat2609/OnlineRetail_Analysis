FROM quay.io/astronomer/astro-runtime:12.1.0
RUN pip install --no-cache-dir great-expectations && pip install --no-cache-dir pyodbc && \
    python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-sqlserver && deactivate
    