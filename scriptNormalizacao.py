# encoding: windows-1252
#!/usr/bin/env python

import pandas as pd
import numpy as np
import io
import csv

def readfile(name, column):
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
		descricao = []
		dataDeAquisicao = []
		departamento = []
		observacoes = []
		with io.open(filename,'r',encoding='utf8',errors="ignore",newline='') as f:
			reader = csv.reader(f)
			i = 0
			for row in reader:
				str1 = ''.join(row)
				list = str1.split(';')
				if len(list)==4:
					try:
						descricao.append(list[0])
						dataDeAquisicao.append(list[1])
						departamento.append(list[2])
						observacoes.append(list[3])
					except Exception as e:
						print ("\nError.: "+str(e))
				i+=1
												
		dict = {'_localizacao':[],'_descricaoImovel':descricao,'_dataDeAquisicao':dataDeAquisicao,'_departamento':departamento,'_observacoes':observacoes}
		#print len(dict.get('_departamento'))

	except Exception as e:
		print ("\nError.: "+str(e))
		quit()
		
		'''
		arquivos = open('csv.txt', 'w')
		f.close()
		arquivos.writelines(arquivo)
		return arquivos
		'''

name = 'dadosImoveisPrefeituraAlegrete'
csv =  readfile(name,0)
