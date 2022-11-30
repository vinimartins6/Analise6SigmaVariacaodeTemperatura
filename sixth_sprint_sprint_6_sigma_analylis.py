#**Importar e tratar os dados**
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbrn
import scipy.stats as stats
from scipy.stats import chi2_contingency
from matplotlib import pyplot
import plotly.express as px
from scipy import stats
import numpy as np

from google.colab import files
files.upload()

df = pd.read_excel("analise_vsb_08_APOS_PIRMEIRA_MODIFICACAO.xlsx")
df_fp = df.loc[df['X18 Rota']=='FP']
df_vd = df.loc[df['X18 Rota']=='VD']

print('Junho e Julho de 2022:\nA porcentagem de casos fora da temperatura especificada foi de: '+str(round((df.loc[df['Y Dentro ou fora da objetivada']==1]['Y Dentro ou fora da objetivada'].count()/df['Y Dentro ou fora da objetivada'].count())*100,1))+'%')

"""# **Existe uma diferença significativa entre rotas FP e VD?***"""

pd.crosstab(df['X18 Rota'], df['Y Quente ou frio'])

pd.crosstab(df['X18 Rota'], df['Y Quente ou frio'],normalize='index')

"""Teste de hipótese Qui-Quadrado entre corridas FP e VD"""

ctab = pd.crosstab(df['X18 Rota'], df['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""Teste de hipótese Qui-Quadrado entre corridas FP e VD (Corridas frias)"""

ctab = pd.crosstab(df.loc[(df['Y Quente ou frio']==0)|(df['Y Quente ou frio']==1)]['X18 Rota'] , df.loc[(df['Y Quente ou frio']==0)|(df['Y Quente ou frio']==1)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""Teste de hipótese Qui-Quadrado entre corridas FP e VD (Corridas quentes)

"""

ctab = pd.crosstab(df.loc[(df['Y Quente ou frio']==0)|(df['Y Quente ou frio']==2)]['X18 Rota'] , df.loc[(df['Y Quente ou frio']==0)|(df['Y Quente ou frio']==2)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (df.loc[(df['Y Quente ou frio']==2)]['X18 Rota'],df['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""# **Existe diferença significativa entre corridas com o teor de carbono de aço diferente?***

Até 0,14%C -> BC

0,15 até 0,30 -> MC

Maior 0,31 -> AC

## **Rota FP**
"""

temp = df_fp

pd.crosstab(temp['Teor_carbono'], temp['Y Quente ou frio'])

pd.crosstab(temp['Teor_carbono'], temp['Y Quente ou frio'],normalize='index')

"""Teste de hipótese Qui-Quadrado relacionando as corridas ao teor de carbono


"""

ctab = pd.crosstab(temp['Teor_carbono'], temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""Teste de hipótese Qui-Quadrado relacionando as corridas ao teor de carbono (Corridas frias)"""

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['Teor_carbono'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""Teste de hipótese Qui-Quadrado relacionando as corridas ao teor de carbono (Corridas quentes)"""

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['Teor_carbono'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""## **Rota VD***"""

temp = df_vd

pd.crosstab(temp['Teor_carbono'], temp['Y Quente ou frio'])

pd.crosstab(temp['Teor_carbono'], temp['Y Quente ou frio'],normalize='index')

"""Teste de hipótese Qui-Quadrado relacionando as corridas ao teor de carbono


"""

ctab = pd.crosstab(temp['Teor_carbono'], temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""Teste de hipótese Qui-Quadrado relacionando as corridas ao teor de carbono (Corridas frias)"""

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['Teor_carbono'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""Teste de hipótese Qui-Quadrado relacionando as corridas ao teor de carbono (Corridas quentes)"""

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['Teor_carbono'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""Aços com teor AC e MC possuem comportamento estatísticamente iguais, divergindo do comportamento dos aços BC que tende a perder mais temperatura"""

temp2 = temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]
ctab = pd.crosstab(temp2.loc[(temp2['Teor_carbono']=='Alto Carbono')|(temp2['Teor_carbono']=='Baixo Carbono')]['Teor_carbono'] , temp2.loc[(temp2['Teor_carbono']=='Alto Carbono')|(temp2['Teor_carbono']=='Baixo Carbono')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp2.loc[(temp2['Teor_carbono']=='Baixo Carbono')|(temp2['Teor_carbono']=='Medio Carbono')]['Teor_carbono'] , temp2.loc[(temp2['Teor_carbono']=='Baixo Carbono')|(temp2['Teor_carbono']=='Medio Carbono')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp2.loc[(temp2['Teor_carbono']=='Alto Carbono')|(temp2['Teor_carbono']=='Medio Carbono')]['Teor_carbono'] , temp2.loc[(temp2['Teor_carbono']=='Alto Carbono')|(temp2['Teor_carbono']=='Medio Carbono')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp2['Teor_carbono'],temp2['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a = np.percentile(temp2.loc[(temp2['Teor_carbono']=='Alto Carbono')|(temp2['Teor_carbono']=='Medio Carbono')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
b = np.percentile(temp2.loc[(temp2['Teor_carbono']=='Baixo Carbono')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
print('O 3º quartil da diferença entre as temperaturas objetivadas são:\nAC e MC -> '+str(a)+'\nBC -> '+str(b))

a = np.percentile(temp2.loc[(temp2['Teor_carbono']=='Alto Carbono')|(temp2['Teor_carbono']=='Medio Carbono')]['Diferenca_temperatura'], 25, interpolation = 'midpoint')
b = np.percentile(temp2.loc[(temp2['Teor_carbono']=='Baixo Carbono')]['Diferenca_temperatura'], 25, interpolation = 'midpoint')
print('O 1º quartil da diferença entre as temperaturas objetivadas são:\nAC e MC -> '+str(a)+'\nBC -> '+str(b))

a = np.percentile(temp2.loc[(temp2['Teor_carbono']=='Alto Carbono')|(temp2['Teor_carbono']=='Medio Carbono')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
b = np.percentile(temp2.loc[(temp2['Teor_carbono']=='Baixo Carbono')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
print('A mediana da diferença entre as temperaturas objetivadas são:\nAC e MC -> '+str(a)+'\nBC -> '+str(b))

"""# **FP**

## **Condição da panela***
"""

temp = df_fp.loc[(df_fp['Y Quente ou frio']==0)|(df_fp['Y Quente ou frio']==2)]
pd.crosstab(df_fp['X14 Discreto'], df_fp['Y Quente ou frio'])

pd.crosstab(df_fp['X14 Discreto'], df_fp['Y Quente ou frio'],normalize='index')

temp = df_fp.loc[(df_fp['Y Quente ou frio']==0)|(df_fp['Y Quente ou frio']==2)]
ctab = pd.crosstab(temp['X14 Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 2 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 2 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Até 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Até 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Diferenca_temperatura'],order=['Até 2 horas','Até 3 horas','Mais de 3 horas'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'].mean()
print('As médias da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Perda Térmica (Cº/min)'],order=['Até 2 horas','Até 3 horas','Mais de 3 horas'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Perda Térmica (Cº/min)'].mean()
print('As médias da perda térmica são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

stats.shapiro(temp['Perda Térmica (Cº/min)'])

stats.mannwhitneyu(x=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'] ,y=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'], alternative = 'two-sided')

"""## **Quantidade de ligas e fundentes adicionados**"""

temp = df_fp
pd.crosstab(df_fp['Discreto_Quantidade_ligas_e_fundentes'], df_fp['Y Quente ou frio'])

pd.crosstab(df_fp['Discreto_Quantidade_ligas_e_fundentes'], df_fp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""## **Tempo da última medição de temperatura até a liberação***

"""

temp = df_fp.loc[df_fp['tempo_apos_medicao']<15]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['tempo_apos_medicao'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['tempo_apos_medicao'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['tempo_apos_medicao'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['tempo_apos_medicao'], alternative = 'two-sided')

temp = df_fp.loc[df_fp['tempo_apos_medicao']<15]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['tempo_apos_medicao'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['tempo_apos_medicao'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['tempo_apos_medicao'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['tempo_apos_medicao'], alternative = 'two-sided')

"""## **Posição sequencial***

"""

temp = df_fp.loc[df_fp['X7 Posição Sequencial']!='Solteira']
pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'])

pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X7 Posição Sequencial'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X7 Posição Sequencial'],temp['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""## **Tempo liberação do refino até início de lingotamento**

"""

temp = df_fp
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X16 Tempo de Liberação Refino até Abertura CCM'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['X16 Tempo de Liberação Refino até Abertura CCM'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X16 Tempo de Liberação Refino até Abertura CCM'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['X16 Tempo de Liberação Refino até Abertura CCM'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X16 Tempo de Liberação Refino até Abertura CCM'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X16 Tempo de Liberação Refino até Abertura CCM'], alternative = 'two-sided')

"""## **Tempo da panela no refino***

"""

temp = df_fp.loc[df_fp['X15 Tempo da Panela no Refino']<210]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X15 Tempo da Panela no Refino'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

fig = pyplot.scatter(temp['X15 Tempo da Panela no Refino'],temp['Perda Térmica (Cº/min)'])
plt.xlabel("X15 Tempo da Panela no Refino")
plt.ylabel("Perda Térmica (Cº/min)")
pyplot.show()

a=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'].mean()
b=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'].mean()
c=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'].mean()
print('As médias da diferença entre as temperaturas objetivadas são:\nFrias -> '+str(a)+'\nObjetivada -> '+str(b)+'\nQuentes -> '+str(c))

stats.shapiro(temp['X15 Tempo da Panela no Refino'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

"""# **VD (AC e MC)**

## **Condição da panela**
"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
pd.crosstab(temp['X14 Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X14 Discreto'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X14 Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['X14 Discreto'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['X14 Discreto'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Mais de 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Mais de 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'].mean()
print('As médias da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Perda Térmica (Cº/min)'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Perda Térmica (Cº/min)'].mean()
print('As médias da perda térmica são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

stats.shapiro(temp['Perda Térmica (Cº/min)'])

stats.mannwhitneyu(x=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'] ,y=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'], alternative = 'two-sided')

"""## **Quantidade de ligas e fundentes adicionados**"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'], temp['Y Quente ou frio'])

pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""## **Tempo da última medição de temperatura até a liberação***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')].loc[df_vd['tempo_apos_medicao']<12.7]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['tempo_apos_medicao'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['tempo_apos_medicao'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['tempo_apos_medicao'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['tempo_apos_medicao'], alternative = 'two-sided')

"""## **Posição sequencial***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')].loc[df_vd['X7 Posição Sequencial']!='Solteira']
pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'])

pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X7 Posição Sequencial'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X7 Posição Sequencial'],temp['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""## **Tempo liberação do refino até início de lingotamento***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X16 Tempo de Liberação Refino até Abertura CCM'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['X16 Tempo de Liberação Refino até Abertura CCM'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X16 Tempo de Liberação Refino até Abertura CCM'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['X16 Tempo de Liberação Refino até Abertura CCM'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X16 Tempo de Liberação Refino até Abertura CCM'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X16 Tempo de Liberação Refino até Abertura CCM'], alternative = 'two-sided')

"""## **Tempo da panela no refino**

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')].loc[df_vd['X15 Tempo da Panela no Refino']<280]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X15 Tempo da Panela no Refino'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

fig = pyplot.scatter(temp['X15 Tempo da Panela no Refino'],temp['Perda Térmica (Cº/min)'])
plt.xlabel("X15 Tempo da Panela no Refino")
plt.ylabel("Perda Térmica (Cº/min)")
pyplot.show()

a=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'].mean()
b=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'].mean()
c=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'].mean()
print('As médias dos tempos da panela no refino são:\nFrias -> '+str(a)+'\nObjetivada -> '+str(b)+'\nQuentes -> '+str(c))

stats.shapiro(temp['X15 Tempo da Panela no Refino'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

"""# **VD (BC)**

## **Condição da panela**
"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
pd.crosstab(temp['X14 Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X14 Discreto'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X14 Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['X14 Discreto'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['X14 Discreto'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Mais de 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Mais de 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'].mean()
print('As médias da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Perda Térmica (Cº/min)'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Perda Térmica (Cº/min)'].mean()
print('As médias da perda térmica são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

stats.shapiro(temp['Perda Térmica (Cº/min)'])

stats.mannwhitneyu(x=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'] ,y=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'], alternative = 'two-sided')

"""## **Quantidade de ligas e fundentes adicionados**"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'], temp['Y Quente ou frio'])

pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""## **Tempo da última medição de temperatura até a liberação***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')].loc[df_vd['tempo_apos_medicao']<12.7]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['tempo_apos_medicao'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['tempo_apos_medicao'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['tempo_apos_medicao'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['tempo_apos_medicao'], alternative = 'two-sided')

"""## **Posição sequencial***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')].loc[df_vd['X7 Posição Sequencial']!='Solteira']
pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'])

pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X7 Posição Sequencial'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X7 Posição Sequencial'],temp['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""## **Tempo liberação do refino até início de lingotamento***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X16 Tempo de Liberação Refino até Abertura CCM'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['X16 Tempo de Liberação Refino até Abertura CCM'])

stats.ttest_ind(temp.loc[(temp['Y Quente ou frio']==0)]['X16 Tempo de Liberação Refino até Abertura CCM'] ,temp.loc[(temp['Y Quente ou frio']==1)]['X16 Tempo de Liberação Refino até Abertura CCM'], alternative = 'two-sided')

stats.ttest_ind(temp.loc[(temp['Y Quente ou frio']==0)]['X16 Tempo de Liberação Refino até Abertura CCM'] ,temp.loc[(temp['Y Quente ou frio']==2)]['X16 Tempo de Liberação Refino até Abertura CCM'], alternative = 'two-sided')

"""## **Tempo da panela no refino**

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')].loc[df_vd['X15 Tempo da Panela no Refino']<250]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X15 Tempo da Panela no Refino'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

fig = pyplot.scatter(temp['X15 Tempo da Panela no Refino'],temp['Perda Térmica (Cº/min)'])
plt.xlabel("X15 Tempo da Panela no Refino")
plt.ylabel("Perda Térmica (Cº/min)")
pyplot.show()

a=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'].mean()
b=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'].mean()
c=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'].mean()
print('As médias dos tempos da panela no refino são:\nFrias -> '+str(a)+'\nObjetivada -> '+str(b)+'\nQuentes -> '+str(c))

stats.shapiro(temp['X15 Tempo da Panela no Refino'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

"""# **Confiabilidade temperatura recomendada de liberação**

## **Verificando confiabilidade**
"""

for index, row in df.iterrows():
  df.loc[index,'diferenca_temperatura_recomendada'] =  (df.loc[index,'REF Última Medição Valor'] - df.loc[index,'Temp. Lib. Calc.'])
  if (df.loc[index,'REF Última Medição Valor'] - df.loc[index,'Temp. Lib. Calc.']) <-5:
    df.loc[index,'cumpriu_temperatura_recomendada'] =  'Abaixo da recomendada'
  if (df.loc[index,'REF Última Medição Valor'] - df.loc[index,'Temp. Lib. Calc.']) >5:
    df.loc[index,'cumpriu_temperatura_recomendada'] =  'Acima da recomendada'
  if (df.loc[index,'REF Última Medição Valor'] - df.loc[index,'Temp. Lib. Calc.']) >=-5 and (df.loc[index,'REF Última Medição Valor'] - df.loc[index,'Temp. Lib. Calc.']) <=5:
    df.loc[index,'cumpriu_temperatura_recomendada'] =  'Na temperatura recomendada'

pd.crosstab(df['cumpriu_temperatura_recomendada'], df['Y Quente ou frio'])

pd.crosstab(df['cumpriu_temperatura_recomendada'], df['Y Quente ou frio'],normalize='index')

stats.shapiro(df['Diferenca_temperatura'])

stats.kruskal(df.loc[df['cumpriu_temperatura_recomendada']=='Na temperatura recomendada']['Diferenca_temperatura'] ,df.loc[df['cumpriu_temperatura_recomendada']=='Acima da recomendada']['Diferenca_temperatura'])

stats.kruskal(df.loc[df['cumpriu_temperatura_recomendada']=='Na temperatura recomendada']['Diferenca_temperatura'] ,df.loc[df['cumpriu_temperatura_recomendada']=='Abaixo da recomendada']['Diferenca_temperatura'])

df = df.loc[df['cumpriu_temperatura_recomendada']=='Acima da recomendada']
df_fp = df.loc[df['X18 Rota']=='FP']
df_vd = df.loc[df['X18 Rota']=='VD']

"""## **FP**

### **Condição da panela***
"""

temp = df_fp.loc[(df_fp['Y Quente ou frio']==0)|(df_fp['Y Quente ou frio']==2)]
pd.crosstab(df_fp['X14 Discreto'], df_fp['Y Quente ou frio'])

pd.crosstab(df_fp['X14 Discreto'], df_fp['Y Quente ou frio'],normalize='index')

temp = df_fp.loc[(df_fp['Y Quente ou frio']==0)|(df_fp['Y Quente ou frio']==2)]
ctab = pd.crosstab(temp['X14 Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 2 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 2 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Até 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Até 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Diferenca_temperatura'], order = ['Até 2 horas','Até 3 horas','Mais de 3 horas'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
b = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
c = np.percentile(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
print('O 3º quartil da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

a = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
b = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
c = np.percentile(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
print('A mediana da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Perda Térmica (Cº/min)'],order = ['Até 2 horas','Até 3 horas','Mais de 3 horas'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Perda Térmica (Cº/min)'].mean()
print('As médias da perda térmica são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

stats.shapiro(temp['Perda Térmica (Cº/min)'])

stats.mannwhitneyu(x=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'] ,y=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'], alternative = 'two-sided')

"""### **Quantidade de ligas e fundentes adicionados***"""

temp = df_fp
pd.crosstab(df_fp['Discreto_Quantidade_ligas_e_fundentes'], df_fp['Y Quente ou frio'])

pd.crosstab(df_fp['Discreto_Quantidade_ligas_e_fundentes'], df_fp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_fp.loc[df_fp['X14 Discreto']=='Até 2 horas']

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_fp.loc[(df_fp['X14 Discreto']=='Mais de 3 horas')|(df_fp['X14 Discreto']=='Até 3 horas')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_fp.loc[df_fp['X14 Discreto']=='Até 2 horas']
temp = temp.loc[(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 1 ton')|(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 3 ton')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_fp.loc[(df_fp['X14 Discreto']=='Mais de 3 horas')|(df_fp['X14 Discreto']=='Até 3 horas')]
temp = temp.loc[(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 1 ton')|(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 3 ton')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_fp.loc[(df_fp['X14 Discreto']=='Mais de 3 horas')|(df_fp['X14 Discreto']=='Até 3 horas')]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Discreto_Quantidade_ligas_e_fundentes'],temp['Diferenca_temperatura'], order = ['Ate 1 ton','Ate 2 ton','Ate 3 ton','Ate 4 ton','Mais que 4 ton'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""### **Tempo da última medição de temperatura até a liberação***

"""

temp = df_fp.loc[df_fp['tempo_apos_medicao']<15]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['tempo_apos_medicao'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['tempo_apos_medicao'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['tempo_apos_medicao'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['tempo_apos_medicao'], alternative = 'two-sided')

temp = df_fp.loc[df_fp['tempo_apos_medicao']<15]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['tempo_apos_medicao'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['tempo_apos_medicao'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['tempo_apos_medicao'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['tempo_apos_medicao'], alternative = 'two-sided')

"""### **Posição sequencial***

"""

temp = df_fp.loc[df_fp['X7 Posição Sequencial']!='Solteira']
pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'])

pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X7 Posição Sequencial'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X7 Posição Sequencial'],temp['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""### **Tempo liberação do refino até início de lingotamento***

"""

temp = df_fp
ctab = pd.crosstab(temp['X16_Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_fp.loc[(df_fp['X14 Discreto']=='Mais de 3 horas')|(df_fp['X14 Discreto']=='Até 3 horas')]
pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'],normalize='index')

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X16_Discreto'],temp['Diferenca_temperatura'],order=["Ate 10 min","Ate 15 min","Ate 20 min","Ate 25 min","Mais que 25 min"])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

temp = df_fp.loc[df_fp['X14 Discreto']=='Até 2 horas']
pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'],normalize='index')

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X16_Discreto'],temp['Diferenca_temperatura'],order=["Ate 10 min","Ate 15 min","Ate 20 min","Ate 25 min","Mais que 25 min"])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""### **Tempo da panela no refino**



"""

temp = df_fp.loc[df_fp['X15 Tempo da Panela no Refino']<210]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X15 Tempo da Panela no Refino'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'].mean()
b=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'].mean()
c=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'].mean()
print('As médias da diferença entre as temperaturas objetivadas são:\nFrias -> '+str(a)+'\nObjetivada -> '+str(b)+'\nQuentes -> '+str(c))

stats.shapiro(temp['X15 Tempo da Panela no Refino'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

temp = df_fp.loc[df_fp['X15 Tempo da Panela no Refino']<210]
temp = temp.loc[temp['X14 Discreto']=='Até 2 horas']
stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

temp = df_fp.loc[df_fp['X15 Tempo da Panela no Refino']<210]
temp = temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]
stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

"""## **VD (AC e MC)**

### **Condição da panela***
"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
pd.crosstab(temp['X14 Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X14 Discreto'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X14 Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['X14 Discreto'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['X14 Discreto'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Mais de 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Mais de 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Até 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Até 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Diferenca_temperatura'], order = ['Até 2 horas','Até 3 horas','Mais de 3 horas'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
b = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
c = np.percentile(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
print('O 3º quartil da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

a = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
b = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
c = np.percentile(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
print('A mediana da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'].mean()
print('As médias da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Perda Térmica (Cº/min)'], order = ['Até 2 horas','Até 3 horas','Mais de 3 horas'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Perda Térmica (Cº/min)'].mean()
print('As médias da perda térmica são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

stats.shapiro(temp['Perda Térmica (Cº/min)'])

stats.mannwhitneyu(x=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'] ,y=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'], alternative = 'two-sided')

"""### **Quantidade de ligas e fundentes adicionados**"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'], temp['Y Quente ou frio'])

pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
temp = temp.loc[temp['X14 Discreto']=='Até 2 horas']

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
temp = temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
temp = temp.loc[temp['X14 Discreto']=='Até 2 horas']
temp = temp.loc[(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 4 ton')|(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 2 ton')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
temp = temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]
temp = temp.loc[(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 2 ton')|(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 3 ton')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""### **Tempo da última medição de temperatura até a liberação***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')].loc[df_vd['tempo_apos_medicao']<12.7]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['tempo_apos_medicao'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['tempo_apos_medicao'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['tempo_apos_medicao'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['tempo_apos_medicao'], alternative = 'two-sided')

"""### **Posição sequencial***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')].loc[df_vd['X7 Posição Sequencial']!='Solteira']
pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'])

pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X7 Posição Sequencial'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X7 Posição Sequencial'],temp['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""### **Tempo liberação do refino até início de lingotamento**

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')]
ctab = pd.crosstab(temp['X16_Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]
pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'],normalize='index')

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X16_Discreto'],temp['Diferenca_temperatura'],order=["Ate 10 min","Ate 15 min","Ate 20 min","Ate 25 min","Mais que 25 min"])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

temp = df_fp.loc[df_fp['X14 Discreto']=='Até 2 horas']
pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'],normalize='index')

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X16_Discreto'],temp['Diferenca_temperatura'],order=["Ate 10 min","Ate 15 min","Ate 20 min","Ate 25 min","Mais que 25 min"])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""### **Tempo da panela no refino**

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Alto Carbono')|(df_vd['Teor_carbono']=='Medio Carbono')].loc[df_vd['X15 Tempo da Panela no Refino']<280]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X15 Tempo da Panela no Refino'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

fig = pyplot.scatter(temp['X15 Tempo da Panela no Refino'],temp['Perda Térmica (Cº/min)'])
plt.xlabel("X15 Tempo da Panela no Refino")
plt.ylabel("Perda Térmica (Cº/min)")
pyplot.show()

a=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'].mean()
b=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'].mean()
c=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'].mean()
print('As médias dos tempos da panela no refino são:\nFrias -> '+str(a)+'\nObjetivada -> '+str(b)+'\nQuentes -> '+str(c))

stats.shapiro(temp['X15 Tempo da Panela no Refino'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

"""## **VD (BC)**

### **Condição da panela***
"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
pd.crosstab(temp['X14 Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X14 Discreto'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X14 Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['X14 Discreto'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==1)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['X14 Discreto'] , temp.loc[(temp['Y Quente ou frio']==0)|(temp['Y Quente ou frio']==2)]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Mais de 3 horas')]['X14 Discreto'] , temp.loc[(temp['X14 Discreto']=='Até 2 horas')|(temp['X14 Discreto']=='Mais de 3 horas')]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Diferenca_temperatura'], order = ['Até 2 horas','Até 3 horas','Mais de 3 horas'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
b = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
c = np.percentile(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'], 75, interpolation = 'midpoint')
print('O 3º quartil da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

a = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
b = np.percentile(temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
c = np.percentile(temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Diferenca_temperatura'], 50, interpolation = 'midpoint')
print('A mediana da diferença entre as temperaturas objetivadas são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X14 Discreto'],temp['Perda Térmica (Cº/min)'], order = ['Até 2 horas','Até 3 horas','Mais de 3 horas'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

a=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'].mean()
b=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'].mean()
c=temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')]['Perda Térmica (Cº/min)'].mean()
print('As médias da perda térmica são:\nAté 2 horas -> '+str(a)+'\nAté 3 horas -> '+str(b)+'\nMais de 3 horas -> '+str(c))

stats.shapiro(temp['Perda Térmica (Cº/min)'])

stats.mannwhitneyu(x=temp.loc[(temp['X14 Discreto']=='Até 2 horas')]['Perda Térmica (Cº/min)'] ,y=temp.loc[(temp['X14 Discreto']=='Até 3 horas')]['Perda Térmica (Cº/min)'], alternative = 'two-sided')

"""### **Quantidade de ligas e fundentes adicionados**"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'], temp['Y Quente ou frio'])

pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
temp = temp.loc[temp['X14 Discreto']=='Até 2 horas']

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
temp = temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
temp = temp.loc[temp['X14 Discreto']=='Até 2 horas']
temp = temp.loc[(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 4 ton')|(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 2 ton')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
temp = temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]
temp = temp.loc[(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 2 ton')|(temp['Discreto_Quantidade_ligas_e_fundentes']=='Ate 3 ton')]

ctab = pd.crosstab(temp['Discreto_Quantidade_ligas_e_fundentes'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

"""### **Tempo da última medição de temperatura até a liberação***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')].loc[df_vd['tempo_apos_medicao']<12.7]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['tempo_apos_medicao'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

stats.shapiro(temp['tempo_apos_medicao'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['tempo_apos_medicao'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['tempo_apos_medicao'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['tempo_apos_medicao'], alternative = 'two-sided')

"""### **Posição sequencial***

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')].loc[df_vd['X7 Posição Sequencial']!='Solteira']
pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'])

pd.crosstab(temp['X7 Posição Sequencial'], temp['Y Quente ou frio'],normalize='index')

ctab = pd.crosstab(temp['X7 Posição Sequencial'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Meio")|(temp['X7 Posição Sequencial']=="Primeira")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

ctab = pd.crosstab(temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['X7 Posição Sequencial'] , temp.loc[(temp['X7 Posição Sequencial']=="Primeira")|(temp['X7 Posição Sequencial']=="Última")]['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X7 Posição Sequencial'],temp['Diferenca_temperatura'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""### **Tempo liberação do refino até início de lingotamento**

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
ctab = pd.crosstab(temp['X16_Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')]
temp = temp.loc[(temp['X16_Discreto']=='Ate 25 min')|(temp['X16_Discreto']=='Ate 15 min')]
ctab = pd.crosstab(temp['X16_Discreto'] , temp['Y Quente ou frio'])
U1,p,a,b = stats.chi2_contingency(ctab)
if p < 0.05: print("Existe uma diferença significativa.\np = "+str(p)) 
else: print("Não existe uma diferença significativa.\np = "+str(p))

temp = temp.loc[(temp['X14 Discreto']=='Mais de 3 horas')|(temp['X14 Discreto']=='Até 3 horas')]
pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'],normalize='index')

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X16_Discreto'],temp['Diferenca_temperatura'],order=["Ate 10 min","Ate 15 min","Ate 20 min","Ate 25 min","Mais que 25 min"])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

temp = df_fp.loc[df_fp['X14 Discreto']=='Até 2 horas']
pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'])

pd.crosstab(temp['X16_Discreto'], temp['Y Quente ou frio'],normalize='index')

fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['X16_Discreto'],temp['Diferenca_temperatura'],order=["Ate 10 min","Ate 15 min","Ate 20 min","Ate 25 min","Mais que 25 min"])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

"""### **Tempo da panela no refino**

"""

temp = df_vd.loc[(df_vd['Teor_carbono']=='Baixo Carbono')].loc[df_vd['X15 Tempo da Panela no Refino']<250]
fig, ax = plt.subplots()
fig.set_size_inches(10,10)
sbrn.boxplot (temp['Y Quente ou frio'],temp['X15 Tempo da Panela no Refino'])
plt.grid(axis='y',linestyle='--', linewidth=0.9)
fig.show()

fig = pyplot.scatter(temp['X15 Tempo da Panela no Refino'],temp['Perda Térmica (Cº/min)'])
plt.xlabel("X15 Tempo da Panela no Refino")
plt.ylabel("Perda Térmica (Cº/min)")
pyplot.show()

a=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'].mean()
b=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'].mean()
c=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'].mean()
print('As médias dos tempos da panela no refino são:\nFrias -> '+str(a)+'\nObjetivada -> '+str(b)+'\nQuentes -> '+str(c))

stats.shapiro(temp['X15 Tempo da Panela no Refino'])

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==1)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')

stats.mannwhitneyu(x=temp.loc[(temp['Y Quente ou frio']==0)]['X15 Tempo da Panela no Refino'] ,y=temp.loc[(temp['Y Quente ou frio']==2)]['X15 Tempo da Panela no Refino'], alternative = 'two-sided')