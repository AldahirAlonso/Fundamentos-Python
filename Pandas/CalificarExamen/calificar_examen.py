import pandas as pd

#1
df_estudiantes = pd.read_csv("respuestas_estudiantes.csv")
df_correctas = pd.read_excel("./respuestas_correctas.xlsx")
#2
preguntas = df_correctas['Pregunta'].values
#3
clave_respuestas = {}
for i in range(df_correctas.shape[0]):
	pregunta = df_correctas['Pregunta'].iloc[i]
	respuesta = df_correctas['Respuesta'].iloc[i]
	clave_respuestas[pregunta] = respuesta
#4
df_estudiantes['Puntuacion'] = 0
for p in preguntas:
	respuesta_correcta = clave_respuestas[p]
	df_estudiantes['Puntuacion'] = df_estudiantes['Puntuacion'].add((df_estudiantes[p] == respuesta_correcta).astype(int))
#5
df_detalle = df_estudiantes.copy()
for p in preguntas:
	df_detalle[p] = df_detalle[p].where(
		df_detalle[p] == clave_respuestas[p],
		df_detalle[p] + 'X'
	)
df_detalle = df_detalle.sort_values('Puntuacion', ascending=False)
print("Leyenda: Respuesta X = Incorrecta")
print(df_detalle.to_string(index=False))
#6
print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")
print(df_estudiantes[['Nombre', 'Puntuacion']].sort_values('Puntuacion', ascending=False).to_string(index=False))
#7
df_estudiantes.to_csv("resultados_examen.csv", index=False)
print("\nResultados guardados en 'resultados_examen.csv'")