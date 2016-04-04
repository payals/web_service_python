#!/usr/bin/python

import web
from fibonacci import fibonacci


urls = (
    "/", "index",
    "/fibonacci/(.*)", "fibonacc"
)

class index:
	def GET(self):
		return 'Welcome to the Fibonacci series generator web service. Append the url with fibonacci/<number> to generate the series.'

class fibonacc:
	def GET(self, num):
		try:
			num = int(num)
			series = fibonacci(num)
		except ValueError as e:
			return """{\n"Exception":"%s"\n}""" % (e) 

		return """{\n"fib_series":%s\n}""" % (series)

def run_serv():
	serv = web.application(urls, globals())
	serv.run()

if __name__ == '__main__':
    run_serv()
