def ord_int(integer):
	try: 
		if integer%1 ==0:
			print "This is an integer."
		else:
			raise Exception
	except TypeError:
		return "Enter a number."
	except:
		return "This number has decimal points."
	else:
		str_int = str(integer)
		if str_int =='11' or str_int =='12' or str_int =='13':
			return str_int +'th'
		elif str_int[-1] =='1':
			return str_int +'st'
		elif str_int[-1] =='2':
			return str_int +'nd'
		elif str_int[-1] =='3':
			return str_int +'rd'
		else:
			return str_int +'th'
	finally:
		print 'This is it.'

#to test the NameError for the integer part. 
#try: ord_int(blah)
#except NameError: 