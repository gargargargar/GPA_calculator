import sys
import json
import math
import numpy
import plotly
import argparse
import csv
from pathlib import Path


GPA_standard = {"A+": 12/3, "A": 12/3, "A-": 11/3,
				"B+": 10/3, "B": 9/3, "B-": 8/3,
				"C+": 7/3, "C": 6/3, "C-": 5/3,
				"D+": 4/3, "D": 3/3, "D-": 2/3,
				"F": 0/3}
boost_dict = {}


def boost_dict_init(boost_filename = ""):
	
	if (boost_filename == ""):
		return

	try:
		with open(boost_filename) as boost_file:
			boost_reader = csv.reader(boost_file, delimiter = ',')

			#Read first line of csv file
			boost_header = next(boost_reader)

			#Determine the corresponding columns for boost type and boost
			boost_type_col = 0 #Type of course, e.g. AP, honors
			boost_col = 1
			for index in range(len(boost_header)):
				if (boost_header[index] == "type"):
					boost_type_col = index
				elif (boost_header[index] == "boost"):
					boost_col = index

			for entry in boost_reader:
				boost_dict[entry[boost_type_col]] = float(entry[boost_col])


	except FileNotFoundError:
		pass #Empty boost_dict


#Main calculating function
def GPA_calculator(filename = "grade_testfile.csv", boost_filename = "boost_testfile.csv", grade_boost = {},
				   maximum_unweighted_GPA = 4.000, decimal = 2, entrytype = "letter"):

	weighted_GPA_sum = 0.0
	unweighted_GPA_sum = 0.0
	maximum_weighted_GPA_sum = 0.0
	maximum_unweighted_GPA = round(maximum_unweighted_GPA, decimal)

	credit_count = 0.0


	#Initialize boost_dict
	boost_dict_init(boost_filename)


	#Raise invalid entry type exception
	if (entrytype != "letter" and entrytype != "gpa"):
		raise Exception("Invalid entry type: {}".format(entrytype))


	#Initiate actual file reading
	try:
		with open(filename) as grade_file:
			grade_reader = csv.reader(grade_file, delimiter = ',')


			#Letter grade to numerical grade conversion
			if (entrytype == "letter"):
				GPA_dict = GPA_standard.copy()
				GPA_dict["A+"] = maximum_unweighted_GPA

				#Round GPA values
				for grade in GPA_dict.keys():
					GPA_dict[grade] = round(GPA_dict[grade], decimal)


			#Read first line of csv file
			header = next(grade_reader)

			#Determine the corresponding columns for grade and credits
			grade_col = 0
			credit_col = 1
			type_col = 2 #Type of course, e.g. AP, honors
			for index in range(len(header)):
				if (header[index] == "grade"):
					grade_col = index
				elif (header[index] == "credit"):
					credit_col = index
				elif(header[index] == "type"):
					type_col = index


			#Iterate through csv file
			#Starting from second row
			for entry in grade_reader:
				credit = float(entry[credit_col]) #add "curr" or no? TODO
				grade = entry[grade_col]
				course_type = entry[type_col]

				credit_count += credit

				if (entrytype == "letter"):
					unweighted_GPA_sum += (GPA_dict[grade] * credit)
					weighted_GPA_sum += (GPA_dict[grade] * credit)
					
				elif(entrytype == "gpa"):
					#TODO: EXCEPTION HANDLING
					grade = float(grade)
					unweighted_GPA_sum += (grade * credit)
					weighted_GPA_sum += (grade * credit)


				#Add the corresponding weights
				if (entry[type_col] in boost_dict):
					weighted_GPA_sum += (boost_dict[course_type] * credit)
					maximum_weighted_GPA_sum += ((maximum_unweighted_GPA + boost_dict[course_type]) * credit)


			#Final GPA Calculation
			unweighted_GPA = round(unweighted_GPA_sum/credit_count, decimal)
			weighted_GPA = round(weighted_GPA_sum/credit_count, decimal)
			maximum_weighted_GPA = round(maximum_weighted_GPA_sum/credit_count, decimal)
			#TODO: Representing more decimal points

			return unweighted_GPA, weighted_GPA, maximum_weighted_GPA


	except FileNotFoundError:
		print("File {} does not exist! Program aborted.".format(args.filename))


	


#Run only if ran individually, doesn't run when imported
if __name__ == "__main__":

	#Parsing relevant parameters
	parser = argparse.ArgumentParser()
	parser.add_argument("--filename", type = str, default = "grade_testfile.csv")
	parser.add_argument("--boost_filename", type = str, default = "boost_testfile.csv")
	parser.add_argument("--maximum", type = float, default = 4.000)
	parser.add_argument("--decimal", type = int, default = 2)
	parser.add_argument("--entrytype", type = str, default = "letter")

	args = parser.parse_args()


	#Output relevant information for user confirmation(?) #TODO
	print("File name: {}".format(args.filename))
	print("Boost File name: {}".format(args.boost_filename))
	print("Maximum Unweighted GPA: {}".format(args.maximum))
	print("Entry Type: {}".format("Letter Grade" if args.entrytype == "letter" else "Explicit GPA"))
	print()


	#Calling main calculating function
	unweighted_GPA, weighted_GPA, maximum_weighted_GPA = GPA_calculator(filename = args.filename, boost_filename = args.boost_filename,
																		maximum_unweighted_GPA = args.maximum, decimal = args.decimal,
																		entrytype = args.entrytype)


	print(("Uneighted GPA: {0:." + str(args.decimal) + "f}/{0:." + str(args.decimal) + "f}").format(unweighted_GPA, args.maximum))
	print(("Weighted GPA: {0:." + str(args.decimal) + "f}/{0:." + str(args.decimal) + "f}").format(weighted_GPA, args.maximum))

	


