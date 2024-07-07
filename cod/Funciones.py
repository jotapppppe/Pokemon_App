
import pandas as pd

# DATOS
pokedex_completa = pd.read_csv("data\Pokemon.csv")
tabla_de_tipos = pd.read_csv("data/tabla_tipos.csv")

tipo = pd.DataFrame({
    'Numero': range(18),
    'Tipo': tabla_de_tipos.loc[:, 'Attacking']
})
tipo = tipo.pivot_table(index=None, columns='Tipo', values='Numero', aggfunc='first')

############################################################################################################################

# FUNCIONES
def comparacion(pkmn1, pkmn2, pkdx):
    '''
    Esta función calcula la puntuación entre dos Pokémon en función de sus tipos.

    Parameters:
    pkmn1 (int): El índice del primer Pokémon en el Pokédex DataFrame.
    pkmn2 (int): El índice del segundo Pokémon en el Pokédex DataFrame.
    pkdx (DataFrame): el DataFrame de Pokédex que contiene información sobre Pokémon.

    Returns:
    int: La puntuación calculada entre los dos Pokémon.

    Note:
    La función utiliza el DataFrame 'tabla_de_tipos' para determinar la efectividad de cada tipo frente a otro.
    '''

    tipo_pkmn1_1 = pkdx.loc[pkmn1, 'Type1']
    tipo11 = tipo.loc['Numero', tipo_pkmn1_1]
    
    tipo12 = None
    if pkdx.loc[pkmn1, 'Type2'] != ' ':
        tipo_pkmn1_2 = pkdx.loc[pkmn1, 'Type2']
        tipo12 = tipo.loc['Numero', tipo_pkmn1_2]
    
    tipo_pkmn2_1 = pkdx.loc[pkmn2, 'Type1']
    tipo21 = tipo.loc['Numero', tipo_pkmn2_1]
    
    tipo22 = None
    if pkdx.iloc[pkmn2]['Type2'] != ' ':
        tipo_pkmn2_2 = pkdx.loc[pkmn2, 'Type2']
        tipo22 = tipo.loc['Numero', tipo_pkmn2_2]
    
    # Inicializar el puntaje en 0
    puntaje = 0
    
    # Sumar los valores correspondientes solo si existen
    if tipo12 is None and tipo22 is None:
        puntaje = tabla_de_tipos.iloc[tipo11, tipo21 + 1]
    
    if  tipo12 is not None:
        puntaje = tabla_de_tipos.iloc[tipo11, tipo21 + 1] + tabla_de_tipos.iloc[tipo12, tipo21 + 1]
    
    if tipo22 is not None:
        puntaje = tabla_de_tipos.iloc[tipo11, tipo21 + 1] * tabla_de_tipos.iloc[tipo11, tipo22 + 1]
    
    if tipo12 is not None and tipo22 is not None:
        puntaje = tabla_de_tipos.iloc[tipo11, tipo21 + 1] * tabla_de_tipos.iloc[tipo11, tipo22 + 1] + tabla_de_tipos.iloc[tipo12, tipo21 + 1] * tabla_de_tipos.iloc[tipo12, tipo22 + 1]
    
    return puntaje


def puntaje_total(pkmn1, pkmn2, pkdx):
    '''
    Calcula la puntuación total entre dos Pokémon en función de sus tipos.

    Parameters:
    pkmn1 (int): El índice del primer Pokémon en el Pokédex DataFrame.
    pkmn2 (int): El índice del segundo Pokémon en el Pokédex DataFrame.
    pkdx (DataFrame): El DataFrame de Pokédex que contiene información sobre Pokémon.

    Returns:
    int: La puntuación total calculada entre los dos Pokémon.

    Note:
    La puntuación se calcula restando la puntuación del segundo Pokémon de la puntuación del primer Pokémon.
    '''
    valor_1 = comparacion(pkmn1, pkmn2, pkdx)
    valor_2 = comparacion(pkmn2, pkmn1, pkdx)

    total = valor_1 - valor_2
    return total


def starter(starters, gym, pkdx):
    '''
    Calcula la puntuación total de cada Pokémon inicial en función de sus interacciones con los Pokémon del gimnasio.

    Parameters:
    starters (lista): una lista de tres números enteros que representan los índices del Pokémon inicial en el marco de datos.
    gym (dict): Un diccionario donde las claves son los nombres de los líderes de los gimnasios y los valores son listas de índices de Pokémon en cada gimnasio.
    pkdx (DataFrame): un DataFrame que contiene datos de Pokémon, incluidos sus tipos y estadísticas.

    Devoluciones:
    DataFrame: Un DataFrame con dos columnas: 'Tipo' (que representa los tipos de Pokémon iniciales) y 'Puntaje' (que representa la puntuación total de cada Pokémon inicial).

    Nota:
    La función calcula la puntuación total de cada Pokémon inicial iterando sobre los Pokémon del gimnasio y llamando a la función puntaje_total.
    La función puntaje_total calcula la puntuación entre dos Pokémon en función de sus tipos.
    La puntuación se calcula restando la puntuación del segundo Pokémon de la puntuación del primer Pokémon.
    '''
    total_1 = 0
    total_2 = 0
    total_3 = 0
    
    for lider in range(len(gym)):
        for i in list(gym.values())[lider]:
            if lider < 2:
                total_1 += puntaje_total(starters[0], i, pkdx)
                total_2 += puntaje_total(starters[1], i, pkdx)
                total_3 += puntaje_total(starters[2], i, pkdx)
            if lider > 1 and lider < 6:
                total_1 += puntaje_total(starters[0] + 1, i, pkdx)
                total_2 += puntaje_total(starters[1] + 1, i, pkdx)
                total_3 += puntaje_total(starters[2] + 1, i, pkdx)
            elif lider > 5:
                total_1 += puntaje_total(starters[0] + 2, i, pkdx)
                total_2 += puntaje_total(starters[1] + 2, i, pkdx)
                total_3 += puntaje_total(starters[2] + 2, i, pkdx)
                    
    resultado = pd.DataFrame({
        'Tipo': ['Planta', 'Fuego', 'Agua'],
        'Puntaje': [total_1, total_2, total_3]
    }) 

    return resultado

def general(pkmn, gym, pkdx):
    '''
    Calcula la puntuación total de un Pokémon específico contra todos los Pokémon del gimnasio.

    Parámetros:
    pkmn (int): El índice del Pokémon específico en el DataFrame de Pokédex.
    gym (dict): Un diccionario donde las claves son los nombres de los líderes de los gimnasios y los valores son listas de índices de Pokémon en cada gimnasio.
    pkdx (DataFrame): un DataFrame que contiene datos de Pokémon, incluidos sus tipos y estadísticas.

    Devoluciones:
    int: La puntuación total calculada para el Pokémon específico contra todos los Pokémon en el gimnasio.

    Nota:
    La función calcula la puntuación iterando sobre los Pokémon en el gimnasio y llamando a la función puntaje_total.
    La función puntaje_total calcula la puntuación entre dos Pokémon en función de sus tipos.
    La puntuación se calcula restando la puntuación del segundo Pokémon de la puntuación del primer Pokémon.
    '''
    total = 0
    
    for lider in range(len(gym)):
        for i in list(gym.values())[lider]:
            total += puntaje_total(pkmn, i, pkdx)
                
    return total

def Top_regional (gym, pkdx, pkdx_nacional):
    '''
    Esta función calcula la puntuación total de cada Pokémon en una Pokédex regional determinada frente a todos los Pokémon en un gimnasio.
    Filtra Pokémon con un total de estadísticas base (Estadísticas) superior a 480.
    La función devuelve un DataFrame ordenado por la puntuación total en orden descendente.

    Parámetros:
    gym (dict): un diccionario donde las claves son los nombres de los líderes de los gimnasios y los valores son listas de índices de Pokémon en cada gimnasio.
    pkdx (DataFrame): un DataFrame que contiene datos de Pokémon, incluidos sus tipos y totales de estadísticas base.
    pkdx_nacional (DataFrame): un DataFrame que contiene datos nacionales de Pokédex, utilizado para calcular puntuaciones.

    Devoluciones:
    DataFrame: Un DataFrame con las columnas 'Número de Pokédex', 'Puntaje', 'Stats', 'Tipo_1', 'Tipo_2'.
    El DataFrame está ordenado por 'Puntaje' en orden descendente y 'Estadísticas' en orden descendente para Pokémon con la misma puntuación.
 """
    '''

    # Lista para almacenar los resultados
    resultados = []
    
    # Calcular el puntaje para cada número de Pokédex y almacenar los resultados
    for numero in list(pkdx.index):
        puntaje = general(numero, gym, pkdx_nacional)  # Suponiendo que pkmn, gym y pkdx están definidos
        resultados.append((pkdx.loc[numero, 'Name'], puntaje, pkdx.loc[numero, 'Total'], pkdx.loc[numero, 'Type1'], pkdx.loc[numero, 'Type2']))
    
    # Construir el DataFrame
    df = pd.DataFrame(resultados, columns=['Número de Pokédex', 'Puntaje', 'Stats', 'Tipo_1', 'Tipo_2'])
    df = df.loc[df['Stats'] >=480]
    # Ordenar el DataFrame por el puntaje en orden descendente
    df = df.sort_values(by=['Puntaje', 'Stats'], ascending=[False, False])
    
    # para borrar los pokemon repetidos
    df = df.drop_duplicates(subset=['Número de Pokédex'], keep='first')

    # Mostrar el DataFrame ordenado
    return df