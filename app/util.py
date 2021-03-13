import random
import re

def compileRegex(pattern):
	return re.compile(pattern, re.IGNORECASE)

def selectRandom(list, count = None):
	if count is None: count = len(list) - 1
	return list[random.randint(0, count)]
