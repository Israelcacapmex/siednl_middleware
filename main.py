

from json import JSONEncoder
from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

ALLOWED_EXTENSIONS = set(['xlsx'])
ALLOWED_NAME_MIR =set(['mir'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def allowed_name_file(filename):
    resp = filename.upper()
    resp = resp.find('MIR')
    if(resp >= 0):
        return True
    else:
        return False
   
@app.route('/upload', methods=['GET', 'POST'])  # type: ignore
def upload():
    if request.method == 'POST':
        if not 'file' in request.files:
            return("No se ha seleccionado ningun Archivo.",400)
        else:
            file = request.files['file']
            if file not in request.files and allowed_file(file.filename):
                if file not in request.files and allowed_name_file(file.filename):
                        df = pd.read_excel(file)
                        df[['Unnamed: 0']] = df[['Unnamed: 0']].fillna(method='ffill', axis=0)
                        df[['Unnamed: 1']] = df[['Unnamed: 1']].fillna(value=' ', axis=0)
                        df[['Unnamed: 2']] = df[['Unnamed: 2']].fillna(value=' ', axis=0)
                        df[['Unnamed: 3']] = df[['Unnamed: 3']].fillna(value=' ', axis=0)
                        df[['Unnamed: 4']] = df[['Unnamed: 4']].fillna(value=' ', axis=0)
                        df[['Unnamed: 5']] = df[['Unnamed: 5']].fillna(value=' ', axis=0)
                        df[['Unnamed: 6']] = df[['Unnamed: 6']].fillna(value=' ', axis=0)



                        # df2 = df.copy()
                        # df2 = df2.fillna(method='ffill', axis=0)
                        # df2= df2.fillna(0)
                        # df['Unnamed: 1'] = df['Unnamed: 1'].fillna(0).astype(str)
                        # df['Unnamed: 0'] = df['Unnamed: 0'].fillna(0).astype(str)
                        # df2 = df.copy()
                        # df2['Unnamed: 0'] = df2['Unnamed: 0'].fillna(0).astype(str)
                        # df2['Unnamed: 1'] = df2['Unnamed: 1'].fillna(0).astype(str)
                        # textoactividades= df2.loc[df2['Unnamed: 0'].str.contains('ACTIVIDADES PROCESOS|ACTIVIDADES|PROCESOS|ACTI', case=False, regex=True, na =False) ].index.tolist()
                        # contenido = []

                        # for i in range(df2['Unnamed: 1'].size):
                        #     for j in textoactividades:
                        #         if i == j:
                        #             contenido1 = df2['Unnamed: 1'][i]
                        #             contenido.append(contenido1)
                        # for i in range(df2['Unnamed: 0'].size):
                        #     for j in contenido:
                        #         if  j in df2['Unnamed: 0'][i]:
                        #             df2['Unnamed: 0'][i] = 'C'+str(j)

                        # for i in range(df2['Unnamed: 0'].size):
                           
                        #     aux = []
                        #     if 'C1' in df2['Unnamed: 0'][i]:
                        #         w = 1
                        #         for j in textoactividades:
                        #             if i+w in textoactividades:
                        #                 aux.append(j)
                        #                 w = w + 1
                        #         contadorp = 0
                           
                                
                            
                        # for i in range(df2['Unnamed: 1'].size):
                        #     contadorp = 0
                        #     for j in textoactividades:
                        #         contadorp = contadorp+1 
                        #         if i == j:
                        #             df['Unnamed: 1'][i] =df2['Unnamed: 0'][i] + str(contadorp)+ ' ' + df['Unnamed: 1'][i]

                        # for i in range(df2['Unnamed: 1'].size):
                        #     contadorw = 1
                        #     for j in textoactividades: 
                        #         if i == j:
                        #             if df['Unnamed: 1'][i] in df2['Unnamed: 0'][i]:
                        #                 df['Unnamed: 1'][i] = df['Unnamed: 1'][i]+str(contadorw )

                        def Encabezado(df):
                            
                            institucion = df.loc[df['Unnamed: 0'].str.contains('INST|INSTITUCIÓN|INSTITUCION', case=False, regex=True, na =False)]
                            nombre_del_programa= df.loc[df['Unnamed: 0'].str.contains('NOMBRE DEL PROGRAMA|NOMBRE|NOM|PROG', case=False, regex=True, na =False)]
                            eje = df.loc[df['Unnamed: 0'].str.contains('EJE DEL PED|EJE', case=False, regex=True, na =False)]
                            tema = df.loc[df['Unnamed: 0'].str.contains('TEMA DEL PED|TEMA', case=False, regex=True, na =False)]
                            objetivo = df.loc[df['Unnamed: 0'].str.contains('OBJETIVO|OBJ|JETI|IVO', case=False, regex=True, na =False)]
                            estrategia = df.loc[df['Unnamed: 0'].str.contains('ESTRATEGIA|ESTRA|TEGIA', case=False, regex=True, na =False)]
                            lineas_de_accion = df.loc[df['Unnamed: 0'].str.contains('LÍNEAS DE ACCIÓN PED|LINEAS|LÍNEAS|ACCIÓN|ACCION', case=False, regex=True, na =False)]
                            beneficiario = df.loc[df['Unnamed: 0'].str.contains('BENEFICIARIO|BENE|FICI|ARIO', case=False, regex=True, na =False)]
                            clasificacion_programatica= df.loc[df['Unnamed: 5'].str.contains('CLASIFICACIÓN PROGRAMÁTICA|CLASIFICACIÓN|PROGRAMÁTICA|CLAS|PROGRA', case=False, regex=True, na =False)]
                            cp_conac_modalidad= df.loc[df['Unnamed: 5'].str.contains('CP CONAC |CP|CONAC|"Modalidad"|CP CONAC', case=False, regex=True, na =False)]
                            encabezado_array=[]
                            encabezado = {
                                'institucion': institucion.iloc[0,1],
                                'nombre_del_programa': nombre_del_programa.iloc[0,1],
                                'eje':eje.iloc[0,1], 
                                'tema':tema.iloc[0,1],
                                'objetivo':objetivo.iloc[0,1],
                                'estrategia':estrategia.iloc[0,1],
                                'lineas_de_accion':lineas_de_accion.iloc[0,1], 
                                'beneficiario':beneficiario.iloc[0,1],
                                'clasificacion_programatica':clasificacion_programatica.iloc[0,6],
                                'cp_conac_modalidad':cp_conac_modalidad.iloc[0,6]
                            }
                            encabezado_array.append(encabezado)
                            
                            return encabezado_array

                        def Fin(df):
                            resumen = df.iloc[18, 1] 
                            indicador= df.iloc[18,2]  
                            formula = df.iloc[18,3]
                            frecuencia = df.iloc[18,4]
                            medios_verificacion = df.iloc[18,5]
                            supuestos= df.iloc[18,6]
                            fin_array =[]
                            fin={
                                'resumen':resumen,
                                'indicador':indicador,
                                'formula':formula,
                                'frecuencia':frecuencia,
                                'medios':medios_verificacion,
                                'supuestos':supuestos
                            }
                            fin_array.append(fin)
                            return fin_array

                        def Propositos(df):
                            df.iloc[19,0]
                            resumen =df.iloc[19,1]
                            indicador= df.iloc[19,2]
                            formula = df.iloc[19,3]
                            frecuencia = df.iloc[19,4]
                            medios_verificacion = df.iloc[19,5]
                            supuestos = df.iloc[19,6]
                            propositos_array=[]
                            propositos = {
                                'resumen':resumen,
                                'indicador':indicador,
                                'formula':formula,
                                'frecuencia':frecuencia,
                                'medios_verificacion':medios_verificacion,
                                'supuestos':supuestos
                            }
                            propositos_array.append(propositos)
                            return propositos_array
                        
                        def Componentes(df):
                            array_indices_componentes =df.loc[df['Unnamed: 0'].str.contains('COMPONENTE|COMPO|NENTES', case=False, regex=True, na =False)].index.tolist()
                            componentes_array=[]
                            x = 1
                           # print(df.loc[df['Unnamed: 0'].str.contains('COMPONENTE|COMPO|NENTES', case=False, regex=True, na =False)])

                            for i in range(len(array_indices_componentes)):
                                                                   
                                    componente = df.iloc[array_indices_componentes[i], 1]
                                    indicador = df.iloc[array_indices_componentes[i], 2]
                                    formula = df.iloc[array_indices_componentes[i], 3]
                                    frecuencia = df.iloc[array_indices_componentes[i], 4]
                                    medios = df.iloc[array_indices_componentes[i], 5]
                                    supuestos = df.iloc[array_indices_componentes[i], 6]

                                    
                                    if "." in componente:
                                         componente = df.iloc[array_indices_componentes[i], 1].split('. ')[1]
                                    else: 
                                        componente = df.iloc[array_indices_componentes[i], 1]
                                 
                                    componentes = {
                                        'componentes': "C" + str(i +1),
                                        'resumen': "C" + str(i +1) + '. ' + componente,
                                        'indicador': indicador,
                                        'formula': formula,
                                        'frecuencia': frecuencia,
                                        'medios': medios,
                                        'supuestos': supuestos
                                    }
                                    componentes_array.append(componentes)

                                    x = x+1
                            return componentes_array

                        

                        
                        def Actividades(df):
                            array_indices_actividades= df.loc[df['Unnamed: 0'].str.contains('ACTIVIDADES PROCESOS|ACTIVIDADES|PROCESOS|ACTI', case=False, regex=True, na=False) ].index.tolist()
                            actividades_array=[]
                            componentes = Componentes(df)
                            primerActividad = array_indices_actividades[0]
                            act =  0
                            componente = 0

                            for i in range(len(array_indices_actividades)):

                                if primerActividad == array_indices_actividades[i]:
                                    act = act + 1
                                    primerActividad = primerActividad + 1
                                    actividad = "A" + str(act) + componentes[componente]['componentes']
                                else:
                                    act = 1
                                    componente = componente + 1
                                    primerActividad = array_indices_actividades[i] + 1
                                    actividad = "A" + str(act) + componentes[componente]['componentes']

                                if "." in df.iloc[array_indices_actividades[i], 1]:
                                    res = df.iloc[array_indices_actividades[i], 1].split('.')[1]
                                else:
                                    res = " "+df.iloc[array_indices_actividades[i], 1]
                                
                               
                                resumen= actividad +"." + res
                                indicador=df.iloc[array_indices_actividades[i],2]
                                formula=df.iloc[array_indices_actividades[i],3]
                                frecuencia=df.iloc[array_indices_actividades[i],4]
                                medios=df.iloc[array_indices_actividades[i],5]
                                supuestos=df.iloc[array_indices_actividades[i],6]

                                actividades ={
                                    'actividad': actividad,
                                    'resumen': resumen,
                                    'indicador':indicador,
                                    'formula':formula,
                                    'frecuencia':frecuencia,
                                    'medios':medios,
                                    'supuestos':supuestos
                                }
                                actividades_array.append(actividades)
                            return actividades_array


                        

                        def CaluloActComp(df):
                            componentes = Componentes(df)
                            actividades = Actividades(df)
                            comp = []
                            act = []
                            act_count = []
                            x = 1

                            for i in componentes:
                                act_counter = 0
                                act_count = []
                                c = i['componentes']
                                
                                for i in range(int(len(c))):
                                    if 'C' not in  c:
                                        c = 'C'+str(i+1) 
                                        comp.append(c)
                                    
                                if c == 'C'+str(x):
                                    c = 'C'+str(x)
                                else:
                                    c = 'C'+str(x)     
                                x = x + 1

                                for j in actividades:
                                    if( c in j['actividad']):
                                        act_counter = act_counter + 1
                                        act_count.append(act_counter)
                                    elif( c in j['actividad']):
                                        act_counter = act_counter + 1
                                        act_count.append(act_counter)
                                act.append({'componente': c, 'actividades': act_count})
                            return act
                        matriz = {
                            'encabezado':Encabezado(df),
                            'fin':Fin(df),
                           'propositos':Propositos(df),
                            'actividades': Actividades(df),
                            'componentes': Componentes(df),
                          'componenteActividad': CaluloActComp(df),
                        }

                        return  jsonify(matriz)
                else:
                    return("Se esperaba una Matriz de Indicadores Prespuestarios.",400)
            else:
                return("El archivo seleccionado no coincide con el formato esperado.",400)

            

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug= True)
        