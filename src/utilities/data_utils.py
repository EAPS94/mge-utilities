"""
data_utils.py: Funciones para carga y preprocesamiento de datos.

Autor: Eduardo P
"""

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica limpieza de datos al DataFrame.

    Se eliminan columnas irrelevantes, se manejan valores nulos y se codifican
    variables categóricas para su uso en modelos de machine learning.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame original con datos sin procesar.

    Returns
    -------
    pd.DataFrame
        DataFrame limpio y listo para análisis.
    """
    df.drop(['GarageArea', 'GarageYrBlt', 'TotRmsAbvGrd', '1stFlrSF', 'Id'],
            axis=1,
            inplace=True)

    df.drop(['Street', 'Utilities', 'Condition2', 'RoofMatl', 'Heating'],
            axis=1,
            inplace=True)

    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]

    df.drop(['PoolQC', 'Alley', 'MiscFeature'], axis=1, inplace=True)

    df['Fence'] = df['Fence'].fillna('None')
    df['FireplaceQu'] = df['FireplaceQu'].fillna('None')
    df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].median())

    df.drop(['GarageType', 'GarageFinish', 'GarageCond'], axis=1, inplace=True)
    df['GarageQual'] = df['GarageQual'].fillna('None')

    df.drop(['BsmtFinType2', 'BsmtExposure', 'BsmtCond', 'BsmtFinType1'],
            axis=1,
            inplace=True)
    df['BsmtQual'] = df['BsmtQual'].fillna('None')
    df['MasVnrType'] = df['MasVnrType'].fillna('None')
    df['MasVnrArea'] = df['MasVnrArea'].fillna(0)

    df['Electrical'] = df['Electrical'].fillna(df['Electrical'].mode()[0])

    return df


def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convierte variables categóricas en valores numéricos.

    Utiliza mappings y `LabelEncoder` para transformar variables categóricas en 
    valores numéricos.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con columnas categóricas.

    Returns
    -------
    pd.DataFrame
        DataFrame con variables categóricas codificadas.
    """
    quality_mapping = {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'Po': 0, 'None': -1}
    df['ExterQual'] = df['ExterQual'].map(quality_mapping)
    df['BsmtQual'] = df['BsmtQual'].map(quality_mapping)
    df['KitchenQual'] = df['KitchenQual'].map(quality_mapping)

    categorical_features = df.select_dtypes(include=['object']).columns.to_list()
    le = LabelEncoder()
    for col in categorical_features:
        df[col] = df[col].astype(str)
        df[col] = le.fit_transform(df[col])

    return df


def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Selecciona las mejores características del conjunto de datos.

    Utiliza `SelectKBest` con `f_regression` para seleccionar las 10 mejores 
    características del conjunto de datos.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame limpio con características.

    Returns
    -------
    pd.DataFrame
        DataFrame con solo las mejores características y la variable objetivo.
    """
    features = df.drop(columns=['SalePrice'])
    target = df['SalePrice']

    selector = SelectKBest(score_func=f_regression, k=10)
    selected_features_array = selector.fit_transform(features, target)

    selected_feature_names = features.columns[selector.get_support()]
    df_selected = pd.DataFrame(selected_features_array, columns=selected_feature_names)

    df_selected['SalePrice'] = target.values

    return df_selected
