class human(object):

	latin_name='homo sapien' #Attribute for the class
	
	#Add attributes for the instances.
	def __init__(self, age, sex, name=None): #initializer or constructor
		self.age = age
		self.name = name
		self.sex = sex
	
	
	#Add some functions
	
	def speak(self, words=None):
		return words

	def introduce(self):
		if self.name==None: return self.class_introduce()
		else:
			if self.sex=='Female': return self.speak("Hello, I'm Ms. %s" % self.name)
			elif self.sex=='Male': return self.speak("Hello, I'm Mr. %s" % self.name)
			else: return self.speak("Hello, I'm %s" % name)
	
	def __str__(self):
		return 'Human: %d year-old %s.' % (self.age, self.sex)
	
	@classmethod
	def class_introduce(cls):
		return 'Here is humanity!'
	
