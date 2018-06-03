# encoding: windows-1252
#!/usr/bin/env python

import pandas as pd
import numpy as np
import io
import csv

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
						dataDeAquisicao.append(list[1])
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
		

def main():	
	name = 'dadosImoveisPrefeituraAlegrete'
	df = read_csv_and_normalize(name)
	
	#quantos imoveis há por localizacao?
	#print df.groupby('localizacao').count()
	
	#quantos imoveis há por departamento(urbanos e rurais)?
	#print df['departamento'].value_counts()

	#Quantos imoveis foram adquiridos antes do ano 1999?


main()
