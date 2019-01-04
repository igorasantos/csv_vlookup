import sys
import pandas as pd
import numpy as np
from io import StringIO

if len(sys.argv) != 4:
	print('''
		Usage: python3 csv_crossfilter.py <sourceData file> <lookupData file> <outputData file>
		Example1: python3 csv_crossfilter.py sourceData.csv lookupData.csv outputData.csv
		Examplo2: python3 csv_crossfilter.py empresas_ti.csv cnaes_secundarias.csv cnaes_sec_from_emp_ti.csv
		Exemplo3: python3 csv_crossfilter.py empresas_ti.csv socios.csv socios_from_emp_ti.csv
	''')
	sys.exit(-1)
else:
	srcData = sys.argv[1]
	lookupData = sys.argv[2]
	outputData = sys.argv[3]
	with open (lookupData) as e:
		firstLookupTxtLineIndex = 0
		for line in e:
			if firstLookupTxtLineIndex == 0:
				firstLookupColumnHeader = line
				break
		with open(outputData,"w")	as out:
			out.write(firstLookupColumnHeader)

	with open(srcData) as f:
		srcIndexCapture = int(input("Type the desired field index to be captured on the sourceData: "))
		lookupIndexCapture = int(input("Type the desired field index to be captured on the lookupData: "))
		srcTxtLineIndex = 0

		for line in f:
			if srcTxtLineIndex == 0:
				srcColumnHeader = line
				break
		for srcLine in f:
			srcTxtLineIndex += 1
			print('Verifying srcLine: '+str(srcTxtLineIndex))
			srcDataRaw = srcColumnHeader + srcLine
			src_df = pd.read_csv(StringIO(srcDataRaw))
			keyToCompare = src_df.iat[0,srcIndexCapture]
			with open(lookupData) as g:
				lookupTxtLineIndex = 0
				for line in g:
					if lookupTxtLineIndex == 0:
						lookupColumnHeader = line
						break
				for lookupLine in g:
					lookupDataRaw = lookupColumnHeader + lookupLine
					lookup_df = pd.read_csv(StringIO(lookupDataRaw))
					keyCompared = lookup_df.iat[0,lookupIndexCapture]

					if keyCompared == keyToCompare:
						out_df = lookup_df.iloc[0]
						out_series = out_df.values

						with open(outputData, 'a') as h:
							out_series.tofile(h, sep=',',format='%s')
							h.write('\n')
	print('end')
