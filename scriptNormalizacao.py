# encoding: windows-1252
#!/usr/bin/env python

import pandas as pd
import numpy as np
import io
import csv
import re
from datetime import datetime

def read_csv_and_normalize(name):

	filename = name+'.csv'

	try:

		localizacao = []
		descricao = []
		dataDeAquisicao = []
		departamento = []
		observacoes = []
		nmrPorSetor = 0

		with io.open(filename,'r',encoding='utf8',errors="ignore",newline='') as f:

			reader = csv.reader(f)

			i = 0

			for row in reader:
				#Cada linha virava uma lista				
				#transformo todos elementos dessa lista numa string unica
				str1 = ''.join(row)

				#crio uma lista com elementos que vao ate ;,  
				list = str1.split(';')

				#no csv temos dois tipos de elementos com apenas um indice
				if len(list)==1:

					#os que contem apenas o nome do bairro
					if "na divis" not in list[0]:
						local = list[0]
					
					#E os que contem informacoes sobre a quantidade de terrenos naquele bairro, setor ou etc
					else:
						nmrPorSetor = int(list[0].split(' ', 1)[0])
						for x in range(0,nmrPorSetor):
							localizacao.append(local)

				#para os elementos que tem 4, sabemos que eles contem informacoes sobre o terreno em si
				if len(list)>1:
					try:
						descricao.append(list[0])
						data = str(list[1])
						try:
							dataDeAquisicao.append(datetime.strptime(data,"%d/%m/%Y"))
						except Exception as e:
							print data
							print ("Erro ao converter uma data: ",e)
						departamento.append(list[2])
						observacoes.append(list[3])
					except Exception as e:
						print ("\nError.: "+str(e))
				i+=1
				

		df = pd.DataFrame({'localizacao':localizacao,
		                   'descricao':descricao,
		                   'dataDeAquisicao':dataDeAquisicao,
		                   'departamento':departamento,
		                   'observacoes':observacoes})
		
		'''
		#Escrever um csv correto com os dados
		texto = []
		texto.append('localizacao;descricao;dataDeAquisicao;departamento;observacoes')
		for l in range(0,len(descricao)):
			texto.append(localizacao[l]+';'+descricao[l]+';'+dataDeAquisicao[l]+';'+departamento[l]+';'+observacoes[l])
		try:
			resultFyle = open("saida.csv",'w')
			for r in texto:
			    resultFyle.write(r + "\n")
			resultFyle.close()
					
		except Exception as e:
			print ("\nError.: "+str(e))
			quit()
		'''
		return df
	
	except Exception as e:
		print ("\nError1.: "+str(e))
		quit()

def criaData(dataDesejada):
	try:
		data = datetime.strptime(dataDesejada,"%d/%m/%Y")
		return data
	except Exception as e:
		print (" Data invalida: "+str(e))

def calculaQuantosMenorQueData(df,dataDesejada):

	count = 0

	for d in df['dataDeAquisicao']:
				
		if d<dataDesejada:
			count+=1

	return count


def calculaQuantosMaiorQueData(df,dataDesejada):

	count = 0

	for d in df['dataDeAquisicao']:
	
		try:
			if d>dataDesejada:
				count+=1
		except Exception as e:
			pass
		
	return count

def imoveisPorMandato(df,dataInicio,dataFim):
	
	count = 0

	for d in df['dataDeAquisicao']:
	
		try:
			if d>=dataInicio and d<=dataFim:
				count+=1
		except Exception as e:
			pass

	return count

def containsObs(df,stg):
	try:
		count = df['observacoes'].str.contains(stg,regex=False).value_counts()
		return count
	except Exception as e:
		print("Nao foi possivel calcular quantos imoveis contem em sua observacao a string "+stg+" :(") 
	


def main():	
	name = 'dadosImoveisPrefeituraAlegrete'
	df = read_csv_and_normalize(name)
	
	#quantos imoveis há por localizacao?
	#print df.groupby('localizacao').count()
	
	#quantos imoveis há por departamento(urbanos e rurais)?
	#print df['departamento'].value_counts()

	#Quantos imoveis foram adquiridos antes do ano 1/1/1999?
	#print calculaQuantosMenorQueData(df,datetime.strptime("1/1/1111","%d/%m/%Y")) 

	#Quantos imoveis foram adquiridos depois do ano 1/1/1999?
	#print calculaQuantosMaiorQueData(df,criaData("1/1/1999")) 

	#Quantos imoveis foram adquiridos por mandato?
	#print len(t[(t.year >= 1950) & (t.year <= 1959)])
	'''

	print imoveisPorMandato(df,criaData("1/1/1968"),criaData("31/12/1972")) 
	print imoveisPorMandato(df,criaData("1/1/1973"),criaData("31/12/1976")) 
	print imoveisPorMandato(df,criaData("1/1/1977"),criaData("31/12/1982"))
	print imoveisPorMandato(df,criaData("1/1/1983"),criaData("31/12/1988"))
	print imoveisPorMandato(df,criaData("1/1/1989"),criaData("31/12/1992"))
	print imoveisPorMandato(df,criaData("1/1/1993"),criaData("31/12/1996"))
	print imoveisPorMandato(df,criaData("1/1/1997"),criaData("31/12/2000"))
	print imoveisPorMandato(df,criaData("1/1/2001"),criaData("31/12/2004"))
	print imoveisPorMandato(df,criaData("1/1/2005"),criaData("31/12/2007"))
	print imoveisPorMandato(df,criaData("1/1/2008"),criaData("31/12/2011"))
	print imoveisPorMandato(df,criaData("1/1/2012"),criaData("31/12/2016"))
	print imoveisPorMandato(df,criaData("1/1/2016"),criaData("31/12/2018"))
	'''
	#quantos imoveis estao na zona leste?
	#print containsObs(df,"zona leste")

	#quantos imoveis no bairro capao do angico
	#print df['localizacao'].value_counts()
	#print df.localizacao[df.localizacao == "CAPO DO ANGICO"].count()
 
 
 	

main()
