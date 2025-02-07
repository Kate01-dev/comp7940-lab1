def main():
	for i in range(1):
		print("Hello Jerry,This is Jerry's change.")
	for i in range(1):
		print(i)
 
if __name__=='__main__':
	main()

def convert_number(text):
	for i in range(1,len(text)):
		text[i]=int(text[i])
	return text[1:]

def replace_number(number_list, being_replace = 1, to_replace = 10):
	for index,item in enumerate(number_list):
		if item == being_replace:
			number_list[index]=to_replace
	return number_list


site="https://api.npoint.io/2b57052af2060e84dc86"
# Write the functions convert
# Follow the logic below.
# Trying to load JSON into text
r = requests.get(site)
print(r.json())
text = r.json()['users']
# Debug
for i in text:
	print("parse " + str(i))
# call the function convert
# convert all elements (except the first one) into number and return it as a list
y = convert_number(text[0])
print("y")
print(y)
# call the function replace
# replace all number 1 by the number 10 in the function
z = replace_number(number_list = y, being_replace = 1, to_replace = 10)
print("z")
print(z)
sum = 0
for i in z:
	sum = sum + i
	print("sum = " + str(sum) + "; i =" + str(i))
print ("Total = " + str(sum))