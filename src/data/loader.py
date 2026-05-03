"""
Data loading utilities for SecureScan AI.
Handles loading and combining multiple vulnerability datasets.
"""

import os
import re
import pandas as pd
from typing import Optional


def load_bigvul(path: str = "data/MSR_data_cleaned.csv") -> pd.DataFrame:
    """Load and prepare BigVul dataset.
    
    Args:
        path: Path to BigVul CSV file.
    
    Returns:
        DataFrame with code and label columns.
    """
    df = pd.read_csv(path, low_memory=False)
    df = df[['func_before', 'vul']].dropna()
    df.columns = ['code', 'label']
    return df


def load_diversevul(path: str = "data/DiverseVul-Cleaned.csv") -> pd.DataFrame:
    """Load and prepare DiverseVul dataset.
    
    Args:
        path: Path to DiverseVul CSV file.
    
    Returns:
        DataFrame with code and label columns.
    """
    df = pd.read_csv(path, low_memory=False)
    df = df[['func', 'target']].dropna()
    df.columns = ['code', 'label']
    df['label'] = df['label'].apply(
        lambda x: int(float(str(x).strip()))
        if str(x).strip() in ['0', '1', '0.0', '1.0'] else None)
    df = df.dropna(subset=['label'])
    df['label'] = df['label'].astype(int)
    return df


def load_formai(path: str = "data/FormAI_dataset.csv") -> pd.DataFrame:
    """Load and prepare FormAI dataset.
    
    Args:
        path: Path to FormAI CSV file.
    
    Returns:
        DataFrame with code and label columns.
    """
    df = pd.read_csv(path)
    df = df[['Source code', 'Vulnerability type']].dropna()
    df.columns = ['code', 'label']
    df['label'] = df['label'].apply(
        lambda x: 0 if 'NOT VULNERABLE' in str(x) else 1)
    return df


def load_all_datasets(data_dir: str = "data") -> pd.DataFrame:
    """Load and combine all three datasets.
    
    Args:
        data_dir: Directory containing all dataset files.
    
    Returns:
        Combined DataFrame with code and label columns.
    """
    dfs = []

    bigvul_path = os.path.join(data_dir, "MSR_data_cleaned.csv")
    if os.path.exists(bigvul_path):
        df1 = load_bigvul(bigvul_path)
        dfs.append(df1)
        print(f"BigVul loaded: {len(df1)} samples")

    diversevul_path = os.path.join(data_dir, "DiverseVul-Cleaned.csv")
    if os.path.exists(diversevul_path):
        df2 = load_diversevul(diversevul_path)
        dfs.append(df2)
        print(f"DiverseVul loaded: {len(df2)} samples")

    formai_path = os.path.join(data_dir, "FormAI_dataset.csv")
    if os.path.exists(formai_path):
        df3 = load_formai(formai_path)
        dfs.append(df3)
        print(f"FormAI loaded: {len(df3)} samples")

    df_all = pd.concat(dfs, ignore_index=True)
    df_all = df_all.dropna(subset=['code', 'label'])
    df_all = df_all[df_all['code'].str.len() > 50]
    df_all['label'] = df_all['label'].astype(int)
    print(f"Total combined: {len(df_all)} samples")
    return df_all
