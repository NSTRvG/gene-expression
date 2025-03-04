import pandas as pd
import numpy as np

def cargar_datos(file_path):
    """Carga los datos de expresión génica desde un archivo Excel"""
    df_24h = pd.read_excel(file_path, sheet_name="24h_RPKM_cqn_padj05")
    df_14h = pd.read_excel(file_path, sheet_name="14h_cqnRPKM_padj05")
    df_8h = pd.read_excel(file_path, sheet_name="8h_cqn and RPKM")
    return df_8h, df_14h, df_24h

def preparar_datos(df_8h, df_14h, df_24h):
    """Prepara los datos numéricos y calcula promedios de MW y Oven"""
    df_8h_numeric = df_8h.select_dtypes(include=[np.number])
    df_14h_numeric = df_14h.select_dtypes(include=[np.number])
    df_24h_numeric = df_24h.select_dtypes(include=[np.number])

    df_avg_8h = pd.DataFrame({
        "MW_8h": df_8h_numeric.iloc[:, :3].mean(axis=1),
        "Oven_8h": df_8h_numeric.iloc[:, 3:].mean(axis=1)
    })
    df_avg_14h = pd.DataFrame({
        "MW_14h": df_14h_numeric.iloc[:, :3].mean(axis=1),
        "Oven_14h": df_14h_numeric.iloc[:, 3:].mean(axis=1)
    })
    df_avg_24h = pd.DataFrame({
        "MW_24h": df_24h_numeric.iloc[:, :3].mean(axis=1),
        "Oven_24h": df_24h_numeric.iloc[:, 3:].mean(axis=1)
    })

    return df_avg_8h, df_avg_14h, df_avg_24h
