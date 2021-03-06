## **What can you do with this module ?**

- Encrypt 
- Decrypt
- See available list of characters to work with

## **How to use this module ?**

Firstly, you must import it with : 
> from caesar import Caesar

Then, you need to initialize the Caesar object :<br>
The *first parameter* is an integer that represents the key value, which must be in the range of available characters.<br>
The *second parameter* is the minimal value that represents the lowest limit of this characters range.<br>
The *third parameter* is the maximal value that represents the highest limit of this characters range.<br>
Note that the two lasts parameters are set to 0x20 and 0x7E by default : this is the range of printable ASCII characters.<br>
> caesar = Caesar(1)    #here, the key equals 1 and the range of available characters is set between 0x20 and 0x7E

If you want to encrypt a message and print it, here is how it works : 
> print(caesar.encrypt("Hello World !"))

Do you want to decrypt the message ? This is the same process :
> print(caesar.decrypt("Hello World !"))

Instead of creating other objects, you can change the key value using updateKey method. It takes in parameter the new key : 
> caesar.updateKey(2)   #here, the key equals 2

Finally, if you want to see the available list of characters, you can simply do:
> print(caesar.availableChars())

##
Do not hesitate to contact me if there are things to improve :smiley:
