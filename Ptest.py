import sys

def main(entity):
	print(entity)

if __name__ == '__main__':
	param1, param2, *entity = sys.argv[1:]
	print(param1 + " \n" + param2 + " \n")
	
	entities = []
	for x in entity :
		ent = x.split(",")
		for y in ent :
			entities.append(y)
			
	print("main function")
	main(entities)