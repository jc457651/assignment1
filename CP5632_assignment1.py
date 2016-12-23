_author_ ="Harpreet Kaur"
# Initialize the constants
BOOK_FILE="books.csv"

def main():
	print("Reading List 1.0 - by Harpreet Kaur ")
	#list_book=[['The Practice of Computing Using Python','Punch and Enbody',792,'r'],
	#		   ['The 360 Degree Leader','John Maxwell',369,'r'],
	#		   ['In Search of Lost Time','Marcel Proust',365,'c'],
	#		   ['Developing the Leader Within You','John Maxwell',225,'r']]
	list_book = []
	displaymenu()
	load_books(list_book)
	choice = input('>>>').upper()

	while choice != "Q":
		if choice == "R":
			list_required_books(list_book)
		elif choice == 'C':
			list_completed_books(list_book)
		elif choice == "A":
			add_new_book("book_list")
		elif choice ==  "N":
			mark_book_completed()
		else:
			print("please enter R,C,A,N or Q")
		displaymenu()
		choice = input('>>> ').upper()
	print("Have a nice day")


# end of main()
def displaymenu():
	print("Menu:")
	print("R - List required books")
	print("C - List completed books")
	print("A - Add new book")
	print("M - Mark a book as completed")
	print("Q - Quit")

def load_books(list_book):
	#temp_file = open("books.csv","r")
	# for line in temp_file:#
	# line = line.strip().split(",")
	# print(line)
	#  temp_file.close()
	print("load_books")
    # end of load_books()

def list_required_books(book_list):
	print("List_required_books")

def list_completed_books(book_list):
	print("list_completed_books")

def add_new_book(book_list):
	print("add_new_book")

def mark_book_completed(book_list):
	print("mark_book_completed")

def complete_a_book():
	"""

	"""
	print("complete a book")

# end of complete_a_book()

# Start the program
main()
