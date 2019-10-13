# -*- coding: utf-8 -*-
import jsonlines, json


# lines count
def getLinesCount(fileName):
	try:
		count = 0;
		f=open(fileName)

		for x in f:
			count = count + 1

		return count

	except NameError:
  		print("Invalid file name")
  	except:
  		print("An exception occurred")


def scanFile(fileName):
	f=open(fileName)
	cnt = 0
	for x in f:
		cnt = cnt +1
		obj = json.loads(x)
		print cnt, obj["url"]






fileName = "News-2019-02-01.json"

print getLinesCount(fileName)
scanFile("News-2019-02-01.json")