#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	
from bs4 import BeautifulSoup
import urllib2 

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())

#Open a .csv file
f = open('test.csv', 'wb')
my_writer = csv.DictWriter(f, fieldnames=("Name", "Subfield","Title","E-mail","Web-page"))
my_writer.writeheader()


subfields=soup.find_all('h3') #Get a list of all subfields.


#Function to get personal page and email from the professor's page
def profinfo_frompage(prof_address):
	prof_page=urllib2.urlopen(prof_address)
	prof_soup=BeautifulSoup(prof_page.read())
	prof_personalpage, prof_email= 'NA', 'NA'
	for a_tag in prof_soup.find_all('a'):
		try: #use try, except is b.c. not all a_tag has ['href'], to ignore the errors
			if 'mailto' in a_tag['href'] and a_tag.string!='polisci@wustl.edu':
				prof_email=a_tag.string
			elif a_tag.string in ['Personal Homepage','Personal Website']:
				prof_personalpage=a_tag['href'] 
		except:
			pass
	return {'email':prof_email,'personalpage':prof_personalpage}


#Function to write professor's information to a .csv file
def process_profinfo(div_tag,subfield):
	name=div_tag.a.string  #can call the a tag directly, don't need to go through the hierarchy: div_tag.strong.a
	subfield=subfield.string
	title=div_tag.contents[-1]
	prof_address='https://polisci.wustl.edu/'+div_tag.a['href']
	otherinfo=profinfo_frompage(prof_address)
	my_writer.writerow({"Name":name, "Subfield":subfield,"Title":title,"E-mail":otherinfo['email'],"Web-page":otherinfo['personalpage']})


#Loop through the subfields and write the info for all professors using the previous function	
#a good way to navigate the tree, to match the professors and sub-fields. they are at the same level. 	
for subfield in subfields:
	for sibling in subfield.next_siblings: #iterate over the siblings of the current subfield
		if sibling in subfields: 
			break #if the sibling is one of the subfields, the inner loop is broken
		else:
			try:  #use try and except to escape the empty lines. the empty lines will run into error in the process_profinfo function.
				process_profinfo(sibling,subfield)
			except:
				pass
	
f.close()
			
				
				
				