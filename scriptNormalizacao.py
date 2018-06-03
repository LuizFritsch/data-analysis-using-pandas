# encoding: windows-1252
#!/usr/bin/env python

import pandas as pd
import numpy as np
import io
import csv

def read_csv_and_normalize(name):
	filename = name+'.csv'
	try:
		'''
		with io.open(filename,'r',encoding='utf8',errors="ignore") as f:
			lines = f.readlines()
			count = 0
			for line in lines:
				localizacao [] = line
		'''
		#localizacao,descricao,data,dep,obs = []
		
		dict = {'_localizacao':[],'_descricaoImovel':[],'_dataDeAquisicao':[],'_departamento':[],'_observacoes':[]}
		
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
						#for com qtd de vezes iterando em nmrPorSetor 
						#localizacao.append(list[0])
					
					#E os que contem informacoes sobre a quantidade de terrenos naquele bairro, setor ou etc
					else:
						nmrPorSetor = int(list[0].split(' ', 1)[0])
				
				#para os elementos que tem 4, sabemos que eles contem informacoes sobre o terreno em si
				if len(list)==4:
					try:
						descricao.append(list[0])
						dataDeAquisicao.append(list[1])
						departamento.append(list[2])
						observacoes.append(list[3])
					except Exception as e:
						print ("\nError.: "+str(e))

				for x in range(0,nmrPorSetor):
					localizacao.append(local)
				i+=1
		
			dict['_localizacao'].append(localizacao)
			dict['_descricaoImovel'].append(descricao)
			dict['_dataDeAquisicao'].append(dataDeAquisicao)
			dict['_departamento'].append(departamento)
			dict['_observacoes'].append(observacoes)

		return dict
	
	except Exception as e:
		print ("\nError.: "+str(e))
		quit()
		
		'''
		arquivos = open('csv.txt', 'w')
		f.close()
		arquivos.writelines(arquivo)
		return arquivos
		'''
def main():	
	name = 'dadosImoveisPrefeituraAlegrete'
	dict =  read_csv_and_normalize(name)
	df = pd.DataFrame.from_dict(dict)

main()
