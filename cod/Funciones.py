
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
    valor_1 = comparacion(pkmn1, pkmn2, pkdx)
    valor_2 = comparacion(pkmn2, pkmn1, pkdx)

    total = valor_1 - valor_2
    return total


def starter(starters, gym, pkdx):
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

    total = 0
    
    for lider in range(len(gym)):
        for i in list(gym.values())[lider]:
            total += puntaje_total(pkmn, i, pkdx)
                
    return total

def Top_regional (gym, pkdx, pkdx_nacional):
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