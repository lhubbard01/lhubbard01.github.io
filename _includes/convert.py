class HtmlFromMarkdown:
	def __init__(self, filename):
		if "\.md" not in filename:
			raise ValueError("filename must refer to a markdown file")
		else:
			self.old = "old__" + filename.split(".")[-2] + ".md" #lol whoops
			self.to  = filename	
		self.pushdown = []
		
























		self.new = []
		self.new_str = ""
	def convert(self):
		while (len(ele_list)) != 0:
			indent = len(self.pushdown)
			if "\{s\}" in line:
				if "\{\/\s\}" in line:
					self.local(line)
	def local(self, item):
		if 