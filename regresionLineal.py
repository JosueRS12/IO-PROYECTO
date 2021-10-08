import pandas as pd # permite leer los datos de un dataset
import statsmodels.formula.api as smf #Libreria que permite calcular los datos
#estadisticos del programa

#Se lee el archivo y/o dataset en formato csv
df = pd.read_csv('./Estadisticas_portal_Anterior.csv')

#Se establece el modelo de regresion lineal a partir del OLS (modelos cuadrados
#por minimos cuadrados)
reg = smf.ols('Numero_de_Visitas ~ Votos_Positivos + Votos_Negativos', data=df)
# se ajusta la respuesta
res = reg.fit()
# se muetra la respuesta
print(res.summary())
print(res.rsquared)
# print(res.rsquared)

