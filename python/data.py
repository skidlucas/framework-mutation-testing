#! /usr/bin/env python3.4

import sys
import os
from os import listdir
from os.path import isfile, join


#init count.txt
c = open('./python/count.txt', 'w')
c.write('0.0.0.0')
c.close()

#clean data.txt
open('./python/report/data.txt', 'w').close()



data = open('./python/report/data.txt', 'a')

testpath = './transformation-code/src/test/java/'
testfiles = [f for f in listdir(testpath) if isfile(join(testpath, f))]

state = 1 # etat du mutant

data.write('proc ' + sys.argv[1] + '\n')
for elt in testfiles:
	test = os.path.splitext(elt)[0]
	testreport = './transformation-code/target/surefire-reports/TEST-' + test + '.xml'
	try:
		xml = open(testreport, 'r')
	except IOError:
		print("ERROR can't open " + testreport + " (doesn't exist?)")
		state = 2 # mon mutant est mort-né
	else:
		for line in xml:
			clashSpace = line.strip()
			split = clashSpace.split(' ')
			if split[0] == '<testcase' :
				res = ' '.join(split).strip('></')
				data.write(res + '\n')
				# mon mutant peut survivre
				state = 1
			if split[0] == '<failure' :
				res = line.split('>')
				data.write(res[1])
				# mon mutant a été tué par un test
				state = 0
			if split[0] == '<error' :
				res = line.split('>')
				data.write(res[1])
				# mon mutant a fait echouer un test
				state = -1
		xml.close()


	# on update le count.txt
	cRead = open('./python/count.txt', 'r')
	for lineC in cRead :
		triple = lineC.split('.')
		d = triple[0] # nombre de mutant mort
		t = triple[1] # nombre de mutant faisant echouer les tests (donc mort)
		a = triple[2] # nombre de mutant vivant
		n = triple[3] # nombre de mutant mort-né
	cRead.close()

	cWrite = open('./python/count.txt', 'w')
	if (state == 1) : #vivant
		newD = int(d)
		newT = int(t)
		newA = int(a) + 1
		newN = int(n)
	elif (state == 0) : #fail
		newD = int(d) + 1
		newT = int(t)
		newA = int(a)
		newN = int(n)
	elif (state == -1) : #error
		newD = int(d)
		newT = int(t) + 1
		newA = int(a)
		newN = int(n)
	elif (state == 2) : #mort-né
		newD = int(d)
		newT = int(t)
		newA = int(a)
		newN = int(n) + 1
	cWrite.write(str(newD) + '.' + str(newT) + '.' + str(newA) + '.' + str(newN))
	cWrite.close()