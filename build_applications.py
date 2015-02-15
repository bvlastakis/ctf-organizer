import os, csv
import pandas.read_csv
import numpy as np
import html-generator as gen
import xhtml2pdf.pisa as pisa
import glob

#questions which will be printed to html
question_array = np.array([10,11,12,17,18,19,20,25,26,27,28,29,30,
						   31,32,33,34,35,36,37,39,40,41,42,43,
						   44,45,46,47,48,49,50,51,52,53,54,
						   55,56,58,59,60])

#questions to be parsed from multiple choice answers
parse_dict = { 17:{1:'Terminal Masters', 2:'PhD'},
			   20:{1:'Humanities', 2:'Social Sciences', 3:'Sciences'},
			   32:{1:'Yes', 2:'No'},
			   34:{1:'Yes', 2:'No'},
			   59:{1:'Yes', 2:'No'}
			   }

#questions which start a new section
title_array = np.array([10,25,39])

class Applicant(object):
	"""Gathers all of the downloaded info on an applicant so we can make
	pdf files of their applications. This class parses downloaded materials
	of each applicant and prints the information to an html file.
	"""

	def __init__(self, form):
		"""Determine applicants name from form"""
		self.form = form
		self.id = form[0]
		#last name plus the first initial of first name
		self.name = (form[11] + '_' + form[12][0]).lower()

	def buildTable(self, questions):
		"""Builds html file from downloaded form"""
		self.dir = apps_dir + self.name
		if os.path.exists(self.dir):
			self.dir += '2'
		os.makedirs(self.dir)
		self.html = self.dir + "/application.html"

		self.parseQuestions()
		with open(self.html, "wt") as table:
			table.write(gen.header(self.name) )
			for idx in question_array:
				if idx in title_array:
					if idx is not title_array[0]:
						table.write(gen.table_close())
					table.write( gen.table_header( questions[idx] ) )
				else:
					table.write( gen.table(questions[idx], str(self.form[idx])) )
			table.write(gen.close() )

	def exportTable(self):
		"""export html file as a pdf."""
		self.pdf = 	self.dir + "/application.pdf"
		pdf = pisa.CreatePDF(
			file(self.html, "r" ),
			file(self.pdf, "wb")
			)

	def parseQuestions(self):
		#replace raw response with intepreted response
		form = self.form
		for question, choice in parse_dict.iteritems():
			form[question] = choice[ int(form[question]) ]

	def loadMaterial(self):
		"""Loads all downloaded material into the correct directory"""
		if not os.path.exists(down_dir):
			raise TypeError("Directory 'downloads' with application materials must exist")

		for filename in glob.glob(down_dir + self.id+ "*"):
			destination = self.dir + "/"+ filename[(len(self.id)+11)::]
			os.rename(filename, destination)


class Applicants(object):
	"""Contains and controls a list of applicant objects"""

	def __init__(self):
		self.applicants = {}

		if not os.path.exists(apps_dir):
			#creates app_dir directory if it does not already exist
			with open(apps_dir, 'a') as ids:
				pass

	def updateImportList(self):
		"""checks if data downloaded from Qualtrics is new"""
		ids_new = self.ids
		ids_list = []

		if not os.path.exists(ids_file):
			with open(ids_file, 'a') as ids:
				pass

		with open(ids_file, "rb") as ids:
			ids_reader = csv.reader(ids)
			for row in ids_reader:
				ids_list.append(row[0])

		ids_new = set(ids_new) - set(ids_list)

		with open(ids_file, "a") as ids:
			ids_writer = csv.writer(ids)
			for idx in ids_new:
				ids_writer.writerow( str(idx) )

		self.ids = ids_new


	def importInfo(self, filename):
		"""Imports data downloaded from Qualtrics table."""
		data = pandas.read_csv(filename)
		self.questions = data.values[0]
		forms = data.values[2::]

		for form in forms:
			applicant = Applicant(form)
			self.applicants[applicant.id] = applicant

		self.ids = self.applicants.keys()

	def buildTables(self):
		for id in self.ids:
			self.applicants[id].buildTable(self.questions)

	def convertTables(self):
		for id in self.ids:
			self.applicants[id].buildTable(self.questions)
			self.applicants[id].exportTable()

	def loadMaterials(self):
		for id in self.ids:
			self.applicants[id].loadMaterial()

if __name__ == '__main__':
	""" Gather all information from imported comma-delimted file from Qualtrics for organization of all applications. This script will update its application list after each import and remove and redundant applications.
	"""
	#default directories
	ids_file = 'ids_list.txt'
	data_file = 'exported_data.csv'
	apps_dir = 'applications/'
	down_dir = 'downloads/'

	#run script
	apps = Applicants()
	apps.importInfo(data_file)
	apps.updateImportList()
	apps.buildTables()
	apps.loadMaterials()
