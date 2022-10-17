

from flask import Flask, request, jsonify, render_template
import pandas as pd
import json
from flask_cors import CORS
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
   



@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        if not 'file' in request.files:
            print("No se ha seleccionado ningun Archivo.")
            return("No se ha seleccionado ningun Archivo.",400)
        else:
            file = request.files['file']
            
            if file not in request.files and allowed_file(file.filename):
                if file not in request.files and allowed_name_file(file.filename):
                        print(allowed_name_file(file.filename))
                        df = pd.read_excel(file )
                        df = df.fillna(method='ffill', axis=0)
                    
                        def Encabezado(df):
                            #[FILA, COLUMNA]
                            institucion = df.loc[df['Unnamed: 0'] == 'INSTITUCIÓN:']
                            nombre_del_programa= df.loc[df['Unnamed: 0'] == 'NOMBRE DEL PROGRAMA:']
                            eje = df.loc[df['Unnamed: 0'] == 'EJE:']
                            tema = df.loc[df['Unnamed: 0'] == 'TEMA:']
                            objetivo = df.loc[df['Unnamed: 0'] == 'OBJETIVO:']
                            estrategia = df.loc[df['Unnamed: 0'] == 'ESTRATEGIA:']
                            lineas_de_accion = df.loc[df['Unnamed: 0'] == 'LÍNEAS DE ACCIÓN']
                            beneficiario = df.loc[df['Unnamed: 0'] == 'BENEFICIARIO (PO/AE):']
                            clasificacion_programatica= df.loc[df['Unnamed: 5'] == 'CLASIFICACIÓN PROGRAMÁTICA:']
                            cp_conac_modalidad= df.loc[df['Unnamed: 5'] == 'CP CONAC "Modalidad":']
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
                            array_indices_componentes =df.loc[df['Unnamed: 0'] == 'COMPONENTES'].index.tolist()
                            componentes_array=[]
                            for i in array_indices_componentes:
                                    codigo = df.iloc[i,1].split('. ')[0]
                                    componente = df.iloc[i, 1]
                                    indicador = df.iloc[i, 2]
                                    formula = df.iloc[i, 3]
                                    frecuencia = df.iloc[i, 4]
                                    medios = df.iloc[i, 5]
                                    supuestos = df.iloc[i, 6]
                                    componentes = {
                                        'componentes': codigo,
                                        'resumen': componente,
                                        'indicador': indicador,
                                        'formula': formula,
                                        'frecuencia': frecuencia,
                                        'medios': medios,
                                        'supuestos': supuestos
                                    }
                                    componentes_array.append(componentes)
                            return componentes_array

                        

                        
                        def Actividades(df):
                            array_indices_actividades= df.loc[df['Unnamed: 0'] == 'ACTIVIDADES (Procesos)'].index.tolist()
                            actividades_array=[]
                            for i in array_indices_actividades:
                                        codigo = df.iloc[i,1].split('. ')[0]
                                        actividad=df.iloc[i,1]
                                        indicador=df.iloc[i,2]
                                        formula=df.iloc[i,3]
                                        frecuencia=df.iloc[i,4]
                                        medios=df.iloc[i,5]
                                        supuestos=df.iloc[i,6]
                                        actividades ={
                                            'actividad': codigo,
                                            'resumen': actividad,
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
                            for i in componentes:
                                act_counter = 0
                                c = i['componentes']
                                comp.append(c)
                                for j in actividades:
                                    if( c in j['actividad']):
                                        act_counter = act_counter + 1
                                act.append({'componente': c, 'actividades': act_counter})
                            return act
                        
                        matriz = {
                            'encabezado':Encabezado(df),
                            'fin':Fin(df),
                            'propositos':Propositos(df),
                            'actividades': Actividades(df),
                            'componentes': Componentes(df),
                            'componenteActividad': CaluloActComp(df)
                        }

                        return  matriz
                else:
                    print("Se esperaba una Matriz de Indicadores Prespuestarios.")
                    return("Se esperaba una Matriz de Indicadores Prespuestarios.",400)
            else:
                print("El archivo seleccionado no coincide con el formato esperado.")
                return("El archivo seleccionado no coincide con el formato esperado.",400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
        