# coding: UTF-8
import urllib.parse
import urllib.request
import socket

class code2Html():

	def __init__(self):
		self.outtime = 5
		self.reqcount = 21

	def openHtml(self, url):
		try:
			request = urllib.request.Request(url)
			request.add_header('user-agent', 'Mozilla/5.0')
			response = urllib.request.urlopen(request, timeout=self.outtime)
			html = response.read()
			mystr = html.decode("gbk")
			response.close()
		except Exception as e:
			print(e) 
		else:
			return mystr

	def getHtml(self, url):		
		try:
			for i in range(self.reqcount):
				print('第{}次请求'.format(i+1))
				html = self.openHtml(url)
				if html == self.reqcount:
					print('网页无响应')
					sys.exit()
				elif html == None:
					continue
				else:
					break
		except Exception as e:
			print(e) 
		else:
			return html

	def fastHtml(self, url):
		try:
			request = urllib.request.Request(url)
			response = urllib.request.urlopen(request, timeout=1)
			html = response.read()
			mystr = html.decode("gbk").split(',')
			response.close()
		except Exception as e:
			print(e) 
		else:
			return mystr




if __name__=='__main__':
	url = r'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/stockid/600519.phtml?year=2017&jidu=1'
	# url = r'http://www.google.com'
	hm = code2Html().getHtml(url)
	print(hm)
