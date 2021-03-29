import random
import re

def compile_regex(pattern):
	return re.compile(pattern, re.IGNORECASE)

def select_random(list, count = None):
	if count is None: count = len(list) - 1
	return list[random.randint(0, count)]
