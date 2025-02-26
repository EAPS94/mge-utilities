"""
model_utils.py: Funciones para evaluar modelos de machine learning.

Autor: Eduardo P
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
from sklearn.base import BaseEstimator

def evaluate_model(model: BaseEstimator, x_test: pd.DataFrame, y_test: pd.Series, model_name: str) -> None:
    """
    Evalúa un modelo de machine learning y muestra métricas de rendimiento.

    Calcula el error absoluto medio (MAE) y la raíz del error cuadrático medio (RMSE).

    Parameters
    ----------
    model : BaseEstimator
        Modelo entrenado compatible con `scikit-learn`.
    x_test : pd.DataFrame
        Conjunto de prueba de características (features).
    y_test : pd.Series
        Conjunto de prueba de la variable objetivo.
    model_name : str
        Nombre del modelo evaluado.

    Returns
    -------
    None
    """
    y_pred = model.predict(x_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"\nEvaluación del modelo {model_name}:")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
