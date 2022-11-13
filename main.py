"""This Program Works with a Cinema Hall.
Created by: Md. Samiul Basir
Email: turjotasin@gmail.com
"""



import string


#QUESTION 1"""
class Star_Cinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall_no):
        self.hall_list.append(hall_no)

#QUESTION 2"""
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = int(rows)
        self.cols = int(cols)
        self. hall_no = hall_no
        self.seats = []
        self.show_list =[]
        self.show_id = []
        super().__init__()
        self.entry_hall(self.hall_no)

    #QUESTION 3"""
    def entry_show(self, id, movie_name, time):
        self.id = int(id)
        add = [id, movie_name, time]
        bro = tuple(add)
        tempseats = []
        self.show_list.append(bro)
        for items in enumerate(self.show_list):
            for i in range(self.rows):
                a = []
                for j in range(self.cols):
                    a.append(f'{i}{j}')
                tempseats.append(a)
        self.seats.append(tempseats)


        self.show_id. append(self.show_list[self.id-1][0])

    #QUESTION 4"""
    def book_seats(self, customer_name, phone_number, id, row, column):

        #QUESTION 9"""
        self.__customer_name = customer_name
        self.__phone_number = phone_number
        self.id = int(id)
        #Id of the show er oikhane giye seat book korte hobe
        a = int(row)
        b = int(column)
        self.seats[self.id-1][a][b] = 'X'

#QUESTION 5"""
    def view_show_list(self):
        for item in self.show_list:
            for values in item:
                print(values.ljust(20), end= '  ')
            print()

#QUESTION 6"""
    def view_available_seats(self, id):
        print('PRINTING THE AVAILABLE SEATS'.center(65))
        print('______________________________________________________________________'.center(50))
        print('----------------------------------------------------------------------'.center(50))
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.seats[int(id)-1][i][j].ljust(10), end='   ')
            print()

        print('----------------------------------------------------------------------\n\n')



a = Hall(4, 6, 12)
#Adding some shows here
a.entry_show(id= '1', movie_name= 'The Platform', time = 'Nov 15, 2022')
a.entry_show(id= '2', movie_name= 'Siccin', time = 'Nov 12, 2023')
a.entry_show(id= '3', movie_name= 'The Green Mile', time = 'Nov 14, 2023')

#"QUESTION 7"""
while(True):
    case = int(input('1. VIEW ALL SHOWS TODAY \n'
                     '2. VIEW ALL SEATS \n'
                     '3. BOOK TICKET\n'
                     '4. END PROCESS\n'))
    if case ==1:
        print('ID'.ljust(21), 'MOVIE NAME'.ljust(21), 'TIME'.ljust(20))
        print('_________________________________________________________')
        print('---------------------------------------------------------')
        a.view_show_list()
        print('---------------------------------------------------------')
        print('\n\n')
    elif case ==2:
        id = int(input('ENTER SHOW ID: '))
        a.view_available_seats(id)
    elif case ==3:

        customer_name = input('NAME:')
        phone_number =  input('PHONE NUMBER: ')

        # CHECKING THE SHOW ID IS CORRECT OR NOT
        while (True):
            id = input('ENTER SHOW ID: ')
            if id in a.show_id:
                break
            else:
                print(f"========================================")
                print(f"!!!WRONG SHOW ID! ENTER SHOW_ID AGAIN!!!")
                print(f"========================================")
                continue


        occupied = 0
        for item in a.seats:
            for inner_item in item:
                for ekdom_vitorer_item in inner_item:
                    if ekdom_vitorer_item =='X':
                        occupied += 1
        while(True):
            number_of_tickets = int(input(f"ENTER NUMBER OF TICKETS YOU WANT TO BUY (Max {24-occupied}): "))
            if number_of_tickets>(24-occupied):
                print("_____________ERROR KHAISEN VAI ABAR_____________".center(50))
                print("!!!ETOGULA SEAT NAI VAI AMADER! GUSHTI NIYA ASHBEN NAKI?!!!".center(50))
                print("___________________________________________________________".center(50))
            else:
                break



        booked_seats = []
        i=0
        while(i<number_of_tickets):
            seat_no = input('ENTER SEAT NO:')
            if ((int(seat_no[0]) < a.rows and int(seat_no[1]) < a.cols) and len(seat_no)==2):
                if a.seats[a.id - 1][int(seat_no[0])][int(seat_no[1])] != 'X':
                    a.book_seats(customer_name, phone_number, id, seat_no[0], seat_no[1])
                    i= i+1
                    booked_seats.append(seat_no)

            else:
                print('!!!  WRONG SEAT NUMBER. ENTER SEAT NUMBER AGAIN !!!')


        print("-------CONGRATUALATIONS! BOOKED SEATS SUCCESSFULLY-------".center(50))
        print(f"-------BOOKED SEATS: {booked_seats}-------".center(50))
        print("___________________________________________________________".center(50))
        a.view_available_seats(id)
        print("\n"*3)


    elif case ==4:
        break
    else:
        print("_____________ERROR KHAISEN VAI ABAR_____________".center(50))
        print('WRONG CHOICE! PLEASE ENTER CHOICE AGAIN')
        print("___________________________________________________________".center(50))



