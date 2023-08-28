# coding=UTF-8

import value as value
import pandas as pd

def openSped(file):
	sped={}
	fil = open(file,'r',encoding='utf-8')
	for f in fil.readlines():
		f=f.split('\n')[0]
		f=f.split('|')[1:-1]
		if(f[0] in sped.keys()):
			sped[f[0]].append(f)
		else:
			sped[f[0]]=[]
			sped[f[0]].append(f) 
	return sped

def match(sped,tam):
	spedatt = []
	for s in sped:
		if(len(s)<tam):
			spedatt.append(s+['']*(tam-len(s)))
		else:
			spedatt.append(s)
	return spedatt

def createDFs(blocks,sped):
	dfs = {}
	for b in blocks.keys():
		try:
			s=match(sped[b],len(blocks[b]))	
		except Exception as e:
			s=[['']*len(blocks[b])]
		dfs[b] = pd.DataFrame(s,columns=blocks[b])
	return dfs

def get_col_widths(dataframe):
	idx_max = max([len(str(s)) for s in dataframe.index.values] + [len(str(dataframe.index.name))])
	return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]

def format(ws,df):
	for i, width in enumerate(get_col_widths(df)):
		ws.set_column(i, i, width)
	return

def createTable(dfs,f):
	writer = pd.ExcelWriter(f+'.xlsx', engine='xlsxwriter')
	for d in dfs.keys():
		dfs[d].to_excel(writer, sheet_name=d)
		worksheet = writer.sheets[d]
		format(worksheet,dfs[d])		
	writer.close()
	return f+'.xlsx'

def main(file,novo):
	sped = openSped(file)
	dfs = createDFs(value.blocos,sped)
	try:
		file=file.split('.')[0]
	except:
		pass				
	novo=createTable(dfs,novo)
	return novo

