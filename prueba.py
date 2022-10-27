

from cmath import nan
from flask import Flask, request, jsonify, render_template
import pandas as pd
import json
from flask_cors import CORS
import openpyxl
from pyparsing import null_debug_action
app = Flask(__name__)
CORS(app)

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
            print("No se ha seleccionado ningun Archivo.")
            return("No se ha seleccionado ningun Archivo.",400)
        else:
            file = request.files['file']
            
            if file not in request.files and allowed_file(file.filename):
                if file not in request.files and allowed_name_file(file.filename):
                        # print(allowed_name_file(file.filename))
                        df = pd.read_excel(file )
                        df = df.fillna(method='ffill', axis=0)
                        df2 = df.copy()
                        df2 = df2.fillna(method='ffill', axis=0)
                        df2= df2.fillna(0)
                        df_index = df.iloc[:,0].tolist()
                        df_index2 = df.iloc[:,1].tolist()
                        
                        df['Unnamed: 1'] = df['Unnamed: 1'].fillna(0).astype(str)
                        df['Unnamed: 0'] = df['Unnamed: 0'].fillna(0).astype(str)
                        df2 = df.copy()
                        df2['Unnamed: 0'] = df2['Unnamed: 0'].fillna(0).astype(str)
                        df2['Unnamed: 1'] = df2['Unnamed: 1'].fillna(0).astype(str)
                        textocomponente =df2.loc[df2['Unnamed: 0'].str.contains('COMPONENTE|COMPO|NENTES', case=False, regex=True, na =False)].index.tolist()
                        textoactividades= df2.loc[df2['Unnamed: 0'].str.contains('ACTIVIDADES PROCESOS|ACTIVIDADES|PROCESOS|ACTI', case=False, regex=True, na =False) ].index.tolist()
                        #print(textocomponente)
                        #print(textoactividades)
                        contenido = []

                        #indices= df.loc[df['Unnamed: 0'].str.contains('ACTIVIDADES PROCESOS|ACTIVIDADES|PROCESOS|ACTI', case=False, regex=True, na =False) ].index.tolist()
                        #for i in textocomponente:
                            #x = i
                            #print(x)
                        #print(x)
                            #if textocomponente[i] == df2['Unnamed: 1'][i]:
                             #   componentedf[i] = df2['Unnamed: 1'][i]
                              #  print(df2['Unnamed: 1'][i])
                            #print(componentedf)
            
                        #for i in range(df2['Unnamed: 0'].size):
                         #   if 'ACTIVIDADES' in df2['Unnamed: 0'][i]:
                          #      print(df2['Unnamed: 0'][i],i)
                            #print('hola',i)
                        #print(df2['Unnamed: 0'])
                        #print(df2['Unnamed: 1'])

                        for i in range(df2['Unnamed: 1'].size):
                            for j in textocomponente:
                            #print(i)
                                #print('indice',i,'Valor que ocupo tomar del indice',j)
                                if i == j :
                                    contenido1 = df2['Unnamed: 1'][i]
                                    contenido.append(contenido1)
                        
                        for i in range(df2['Unnamed: 1'].size):
                         #   if  str(contenido) in df2['Unnamed: 1'][i] :
                                print('indice',i,df2['Unnamed: 1'][i])


                        #print(contenido)


                        def Encabezado(df):
                            
                            #institucion = df.loc[df['Unnamed: 0'] == 'INSTITUCIÓN:']
                            institucion = df.loc[df['Unnamed: 0'].str.contains('INST|INSTITUCIÓN|INSTITUCION', case=False, regex=True, na =False)]
                            #nombre_del_programa= df.loc[df['Unnamed: 0'] == 'NOMBRE DEL PROGRAMA:']
                            nombre_del_programa= df.loc[df['Unnamed: 0'].str.contains('NOMBRE DEL PROGRAMA|NOMBRE|NOM|PROG', case=False, regex=True, na =False)]
                            #eje = df.loc[df['Unnamed: 0'] == 'EJE DEL PED:']
                            eje = df.loc[df['Unnamed: 0'].str.contains('EJE DEL PED|EJE', case=False, regex=True, na =False)]
                            #tema = df.loc[df['Unnamed: 0'] == 'TEMA DEL PED:']
                            tema = df.loc[df['Unnamed: 0'].str.contains('TEMA DEL PED|TEMA', case=False, regex=True, na =False)]
                            #objetivo = df.loc[df['Unnamed: 0'] == 'OBJETIVO:']
                            objetivo = df.loc[df['Unnamed: 0'].str.contains('OBJETIVO|OBJ|JETI|IVO', case=False, regex=True, na =False)]
                            #estrategia = df.loc[df['Unnamed: 0'] == 'ESTRATEGIA:']
                            estrategia = df.loc[df['Unnamed: 0'].str.contains('ESTRATEGIA|ESTRA|TEGIA', case=False, regex=True, na =False)]
                            #lineas_de_accion = df.loc[df['Unnamed: 0'] == 'LÍNEAS DE ACCIÓN PED:']
                            lineas_de_accion = df.loc[df['Unnamed: 0'].str.contains('LÍNEAS DE ACCIÓN PED|LINEAS|LÍNEAS|ACCIÓN|ACCION', case=False, regex=True, na =False)]
                            #beneficiario = df.loc[df['Unnamed: 0'] == 'BENEFICIARIO (PO/AE):']
                            beneficiario = df.loc[df['Unnamed: 0'].str.contains('BENEFICIARIO|BENE|FICI|ARIO', case=False, regex=True, na =False)]
                            #clasificacion_programatica= df.loc[df['Unnamed: 5'] == 'CLASIFICACIÓN PROGRAMÁTICA:']
                            clasificacion_programatica= df.loc[df['Unnamed: 5'].str.contains('CLASIFICACIÓN PROGRAMÁTICA|CLASIFICACIÓN|PROGRAMÁTICA|CLAS|PROGRA', case=False, regex=True, na =False)]
                            #cp_conac_modalidad= df.loc[df['Unnamed: 5'] == 'CP CONAC "Modalidad":']
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
                            #array_indices_componentes =df.loc[df['Unnamed: 0'] == 'COMPONENTES'].index.tolist()
                            array_indices_componentes =df.loc[df['Unnamed: 0'].str.contains('COMPONENTE|COMPO|NENTES', case=False, regex=True, na =False)].index.tolist()
                            componentes_array=[]
                            x = 1
                            for i in range(len(array_indices_componentes)):
                               
                                    codigo = df.iloc[array_indices_componentes[i],1].split('. ')[0]
                                    
                                    componente = df.iloc[array_indices_componentes[i], 1]
                                    indicador = df.iloc[array_indices_componentes[i], 2]
                                    formula = df.iloc[array_indices_componentes[i], 3]
                                    frecuencia = df.iloc[array_indices_componentes[i], 4]
                                    medios = df.iloc[array_indices_componentes[i], 5]
                                    supuestos = df.iloc[array_indices_componentes[i], 6]
                                    
                                    if   "C" in componente:
                                         componente = "C"+str(x)
                                    else:
                                         componente = "C"+str(x)

                                    componentes = {
                                        'componentes': "C" + str(i +1)+ ' ' + codigo,
                                        'resumen': "C" + str(i +1) + ' ' + componente,
                                        'indicador': indicador,
                                        'formula': formula,
                                        'frecuencia': frecuencia,
                                        'medios': medios,
                                        'supuestos': supuestos
                                    }
                                    componentes_array.append(componentes)
                                    #print('componente',componente)
                                    #print('codigo',codigo)
                                    
                                    x = x+1
                                    #print(x)  
                            #print(array_indices_componentes)
                            return componentes_array

                        

                        
                        def Actividades(df):
                            #array_indices_actividades= df.loc[df['Unnamed: 0'] == 'ACTIVIDADES (PROCESOS)'].index.tolist()
                            array_indices_actividades= df.loc[df['Unnamed: 0'].str.contains('ACTIVIDADES PROCESOS|ACTIVIDADES|PROCESOS|ACTI', case=False, regex=True, na =False) ].index.tolist()
                            actividades_array=[]
                            for i in range(len(array_indices_actividades)):
                                        codigo = df.iloc[array_indices_actividades[i],1].split('. ')[0]
                                        actividad=df.iloc[array_indices_actividades[i],1]
                                        indicador=df.iloc[array_indices_actividades[i],2]
                                        formula=df.iloc[array_indices_actividades[i],3]
                                        frecuencia=df.iloc[array_indices_actividades[i],4]
                                        medios=df.iloc[array_indices_actividades[i],5]
                                        supuestos=df.iloc[array_indices_actividades[i],6]
                                        #print('resumen',actividad)
                                        #print('actividad',codigo)

                                        #if 'C' in  actividad:
                                          #   codigo = actividad + str(i)
                                             #print('resumen',actividad)
                                             #print('actividad',codigo)
                                        #if 
                                        #else:
                                         #   codigo = 'AC' + str(i)
                                            #actividad ='AC' + str(i)
                                            #print('resumen',actividad)
                                            #print('actividad',codigo)

                                        actividades ={
                                            'actividad': "A" + str(i +1),
                                            'resumen': actividad,
                                            'indicador':indicador,
                                            'formula':formula,
                                            'frecuencia':frecuencia,
                                            'medios':medios,
                                            'supuestos':supuestos
                                        }
                                        print()
                                        actividades_array.append(actividades)
                                        #print(codigo)
                            #print(array_indices_actividades)
                            print()
                            return actividades_array


                        

                        def CaluloActComp(df):
                            componentes = Componentes(df)
                            actividades = Actividades(df)
                            comp = []
                            act = []
                            act_count = []
                            x = 1
                            #for q in actividades:
                             #   a = q['codigo']
                              #  print(a)

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
                                x = x+1
                               
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
                           #'componenteActividad': CaluloActComp(df)
                        }

                        return  matriz





          
                else:
                    print("Se esperaba una Matriz de Indicadores Prespuestarios.")
                    return("Se esperaba una Matriz de Indicadores Prespuestarios.",400)
            else:
                print("El archivo seleccionado no coincide con el formato esperado.")
                return("El archivo seleccionado no coincide con el formato esperado.",400)

            

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug= True)
        