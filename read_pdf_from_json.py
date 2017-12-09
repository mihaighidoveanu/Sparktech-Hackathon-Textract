import json


### sorts the json file located at @json_path by the y coordinate of words
### returns the sorted json data
def preformat_json(json_path):
	# read the json
	with open(json_path,'r') as inp:
		data = json.load(inp)

	#sort the json by the y index of words and drawn lines
	result = dict(data)
	for page in result :
		result[page]['drawn_lines'] = sorted(data['0']['drawn_lines'],key = lambda x : x['y'])
		result[page]['words'] = sorted(data['0']['words'],key = lambda x : x['y'])

	return result


def preformat_word(word):
	try:
		if word.bold == true:
			word.bold = 1
		else :
			word.bold = 0
		return word
	except AttributeError:
		return word

def read_pdf_from_json(json_path):

	pfjson = preformat_json(json_path)

	#make an array PDF[page][lines][words] = {word}
	PDF = []


	# #initialize the PDF for each page
	for page in pfjson:
		empty_page = [[{}]]
		PDF.append(empty_page)


	#add words from json to lines
	for page in pfjson:

		int_page = int(page)
		current_line = 0
		line_empty = True

		for word in pfjson[page]["words"]:


			# if line has no empty values, thus is not empty
			if all(PDF[int_page][current_line]):

				line_empty = False
				# print 'line is not empty'

				last_word = PDF[int_page][current_line][0]

				# if last word has same y as current word, add current word to the line
				#else change to a new line
				if last_word['y'] == word['y']:

					if word['bold'] == True :
						word['bold'] = 1
					else :
						word['bold'] = 0

					PDF[int_page][current_line].append(word)
				else :
					# print "trecem la linie noua"
					PDF[int_page].append([{}])
					current_line = current_line + 1
					line_empty = True
			else:

				if word['bold'] == True :
					word['bold'] = 1
				else :
					word['bold'] = 0

				if line_empty :
					PDF[int_page][current_line][0] = word
				else :
					PDF[int_page][current_line].append(word)

	return PDF
