import sqlite3
import time
import datetime

conn = sqlite3.connect('Dictionary.db')
c = conn.cursor()


def print_usage():
	print("| 1 - ADD      |")
	print("| 2 - EDIT     |")
	print("| 3 - SETTINGS |")
	print("| 4 - START    |")
	print("| 5 - EXIT     |")

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS vocabulary(datestamp TEXT, deword TEXT, ruword TEXT, miss INTEGER)')

def add_word_to_table():
	date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
	word1 = input('Enter de language word:')
	word2 = input('Enter ru language word:')
	print(word2)
	miss = 0
	c.execute("INSERT INTO vocabulary(datestamp, deword, ruword, miss) VALUES (?, ?, ?, ?)", 
		  (date, word1, word2.encode('UTF-8'), miss))
	conn.commit()

def print_table():
	print("Your dictionary:")
	c.execute("SELECT * FROM vocabulary")
	for date, word1, word2, miss in c.fetchall():
		print(date, word1, word2.decode('UTF-8'), miss)

def print_edit_menu():
	print("| 1 - EDIT     |")
	print("| 2 - DELETE   |")
	print("| 3 - RETURN   |")
	
def edit_word():
	print_edit_menu()

	edit_choice = input('Enter your input:')

	if edit_choice == '1':
		edit_word = input('DE word to edit:')
		new_de_word = input('Enter de language word:')
		new_ru_word = input('Enter ru language word:')
		c.execute("UPDATE vocabulary SET deword = ?, ruword = ? WHERE deword = ?", (new_de_word, new_ru_word, edit_word))
		conn.commit()

	elif edit_choice == '2':
		del_word = input('DE word to delete:')
		c.execute("DELETE FROM vocabulary WHERE deword = {}".format(del_word))
		conn.commit()
		
	elif edit_choice == '3':
		print('Exit from edit')

def main():
        create_table()

        sleep_time = 2
        exit = True
        while exit:
                print_usage()
                choice = input('Enter command:')

                if choice == '1':
                        add_word_to_table()

                elif choice == '2':
                        print_table()
                        edit_word()
                                
                elif choice == '3':
                        sleep_time = float(input('Enter sleep time:'))

                elif choice == '4':
                        print("(-_-)")

                elif choice == '5':
                        exit = False
                        break

                time.sleep(sleep_time)
                
        c.close()

if __name__ == "__main__":
	main()
