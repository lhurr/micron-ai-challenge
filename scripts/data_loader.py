import glob
import os
import pandas as pd

def load_data(directory=".") -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:

    run_pattern = os.path.join(directory, "run_data_*.parquet")
    incoming_pattern = os.path.join(directory, "incoming_run_data_*.parquet")
    metrology_pattern = os.path.join(directory, "metrology_data*.parquet")

    run_files = sorted(glob.glob(run_pattern))
    incoming_files = sorted(glob.glob(incoming_pattern))
    metrology_files = sorted(glob.glob(metrology_pattern))


    run_df = pd.concat([pd.read_parquet(f) for f in run_files], ignore_index=True)
    incoming_df = pd.concat([pd.read_parquet(f) for f in incoming_files], ignore_index=True) if incoming_files else pd.DataFrame()
    metrology_df = pd.concat([pd.read_parquet(f) for f in metrology_files], ignore_index=True)

    return run_df, incoming_df, metrology_df

