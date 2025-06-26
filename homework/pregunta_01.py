"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realiza la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    Aplica transformación y depuración de datos según lo requerido,
    y guarda el archivo limpio en "files/output/solicitudes_de_credito.csv".
    """
    import pandas as pd
    import os

    # Cargar el archivo CSV
    datos = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";").dropna()

    # Estandarización de las columnas sexo y tipo de emprendimiento
    datos["sexo"] = datos["sexo"].str.lower()
    datos["tipo_de_emprendimiento"] = datos["tipo_de_emprendimiento"].str.lower()

    # Reemplazo de guines bajos y medios en la columa idea de negocio
    datos["idea_negocio"] = (
        datos["idea_negocio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.strip()
    )

    # Sustitución de guines medio y bajos en la columna barrio
    datos["barrio"] = (
        datos["barrio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    # Estandarización de la fecha
    def formatear_fecha(fecha):
        return f"{fecha[8:10]}/{fecha[5:7]}/{fecha[0:4]}" if fecha[0:4].isdigit() else fecha

    # Aplicar formato de fecha estandarizada
    datos["fecha_de_beneficio"] = datos["fecha_de_beneficio"].apply(formatear_fecha)

    # Normalizar y convertir los datos del monto de crédito en flotante
    datos["monto_del_credito"] = (
        datos["monto_del_credito"]
        .str.replace(" ", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # Limpieza de los datos en línea de crédito sustituyendo guines medio y bajos por espacios
    datos["línea_credito"] = (
        datos["línea_credito"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    # Eliminar valores duplicados
    datos_limpios = datos.drop_duplicates(subset=[
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "comuna_ciudadano",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ])

    # Crear carpeta output que contiene la información 
    os.makedirs(os.path.dirname("files/output/solicitudes_de_credito.csv"), exist_ok=True)
    datos_limpios.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

    if __name__ == "__main__":
        pregunta_01()