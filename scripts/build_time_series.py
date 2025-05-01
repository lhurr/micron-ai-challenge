import pandas as pd
import numpy as np

def build_series_per_run(df):
    """
    Build a nested DataFrame of shape [n_runs, n_sensors] where each cell is a pandas Series of sensor values.
    """
    runs = df['Run ID'].unique()
    sensors = df['Sensor Name'].unique()

    X = pd.DataFrame(index=runs, columns=sensors)
    for run in runs:
        df_run = df[df['Run ID'] == run]
        for sensor in sensors:
            df_sensor = df_run[df_run['Sensor Name'] == sensor]
            if not df_sensor.empty:

                series = pd.Series(df_sensor.sort_values('Time Stamp')['Sensor Value'].values)
                X.at[run, sensor] = series
            else:
                # If a sensor has no data for this run, fill with an empty Series or NaNs
                X.at[run, sensor] = pd.Series(dtype=float)
    return X

def merge_current_incoming(run_df, inc_df):
    """
    combined nested DataFrame including current and incoming sensors.
    Incoming sensor names are prefixed to distinguish them.
    """
    X_curr = build_series_per_run(run_df)
    X_inc = build_series_per_run(inc_df)

    X_inc = X_inc.rename(columns=lambda x: f"incoming_{x}")
    X_all = pd.concat([X_curr, X_inc], axis=1).fillna(pd.Series(dtype=object))
    X_all.sort_index(inplace=True)
    return X_all

def build_target_vector(met_df):
    """
    For each run_id, collect the 49 measurements into a numpy array (sorted by X,Y or any fixed order).
    Returns a DataFrame y indexed by run_id with 49-dimensional targets.
    """
    met_df_sorted = met_df.sort_values(by=['Run ID', 'X', 'Y'])

    y_series = met_df_sorted.groupby('Run ID')['measurement'].apply(lambda vals: np.array(vals.values))
    y_df = pd.DataFrame({'y': y_series})
    return y_df
