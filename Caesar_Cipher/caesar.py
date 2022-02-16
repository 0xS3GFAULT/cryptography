"""
author  : 0xS3GFAULT
brief   : This is a python3.X module about cryptography using caesar cipher
"""

class Caesar:
	"""
	This class can initialise caesar objects and use encryption/decryption functions that return encrypted/decrypted strings
	using the caesar encryption
	"""
	def __init__(self,key,min_char=0x20,max_char=0x7E):
		"""
		The constructor initializes the key and the range of characters to work with after checking for errors.
		The range of characters is defined by the minimum and the maximum character value.
		This range is set by default from the printable ASCII table (from 0x20 to 0x7E)
		"""
		try:
			self.min_char = int(min_char)
			self.max_char = int(max_char)
			assert (min_char >= 0x20) and (max_char >= 0x20) and (max_char != min_char)
		except ValueError:
			print("[!] The limit values of range of characters must be set as integers !")
			exit()
		except AssertionError:
			print("[!] The limit values of range of characters are incorrect !")
			exit()
		try:
			self.key = int(key)
			max_value = self.max_char - self.min_char + 1
			assert max_value >= self.key >= -max_value 
		except ValueError:
			print("[!] The caesar key must be an integer !")
			exit()
		except AssertionError:
			print("[!] The caesar key value must be between {} and {} !".format(-max_value,max_value))
			exit()

	def encrypt(self,message):
		""" 
		This method takes in parameter the message to encrypt and returns the encrypted message
		"""
		return "".join([chr((ord(char) - self.min_char + self.key) % (self.max_char - self.min_char + 1) + self.min_char) for char in message])

	def decrypt(self,message):
		""" 
		This method takes in parameter the message to decrypt and returns the decrypted message
		"""
		return "".join([chr((ord(char) - self.min_char - self.key) % (self.max_char - self.min_char + 1) + self.min_char) for char in message])

	def availableChars(self):
		""" 
		This method returns the available chars to work with.
		This available chars list is set from self.min_char and self.max_char
		"""
		return "".join([chr(i) for i in range(self.min_char,self.max_char+1)])
