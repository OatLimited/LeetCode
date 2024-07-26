import re
import sqlite3
from sqlite3 import Error

class User_interface:
    def __init__(self) -> None:
        self.date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')


    ## UI Main menu (Display only)
    def main_menu(self):
        print(f'{"______"*20}')
        print(f'{"Welcome to Expense tracker program":^120}')
        print(f'{"______"*20}')
        print(f'Choose your action :')
        print()
        print(f'1. Create new expense')
        print(f'2. Update exsit expense')
        print(f'3. Display expense')
        print(f'4. Quit')
        print(f'{"______"*20}')

    ## check user input 
    def correction_input(self,typing,type):
        ## Date check
        if type == "Date : ":
            while True:
                if self.date_pattern.match(typing):
                        return typing
                else:
                    print("Invalid format. Please enter the date in the format yyyy-mm-dd.")
                typing = str(input(type))
        ## Int check
        elif type == "Amount : " :
            while True:
                try :
                    if int(typing) :
                        return typing
                except:
                    print("please input only integer")
                typing = str(input(type))
        else:
            return typing

    ## User input function 
    def action(self): 
        expense = []
        typing = str(input("Action :"))
        ##Check input must in format
        if typing not in ['1', '2', '3', '4']: 
            print("Your input wrong choice !!")
            return 'Error'
        if typing == '1': 
            expense.append(typing)
            for type in ["Category : ","Description : ","Date : ","Amount : "]:
                typing = str(input(type))
                typing = self.correction_input(typing, type)
                expense.append(typing)
        if typing == '2':
            expense.append(typing)
            for type in ["Description: ","Amount : "]:             
                typing = str(input(type))
                expense.append(typing)
        if typing == '3':
            expense.append(typing)
        if typing == '4' :
            expense.append(typing)
        print(f'{"______"*20}')
        return expense

class Category:
    def __init__(self) -> None:
        self.database = "category.db"

    def create_connection(self):
        self.cnx = None
        try: 
            self.cnx = sqlite3.connect(self.database)
        except Error as e:
            print(e)
       
    # create table if its doesnt exist   
    def create_table(self):
        sql ="""
            CREATE TABLE IF NOT EXISTS category(
            id integer PRIMARY KEY,
            category_name text NOT NULL,
            expense_name text NOT NULL            
            )            
            """

        try:
            c = self.cnx.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

    def add_category(self, category_name, expense_name):
        sql =   """
                INSERT INTO category(category_name, expense_name)
                VALUES (?,?)
                """
        params = (category_name, expense_name)
        try:
            c = self.cnx.cursor()
            c.execute(sql, params)
            self.cnx.commit()
        except Error as e:
            print(e)
        

    def update_category(self, category_name, expense_name):
        sql =   """
                UPDATE category
                SET category_name = ?
                WHERE expense_name = ?
                """
        params = (category_name, expense_name)
        try : 
            c = self.cnx.cursor()
            c.execute(sql, params)
            self.cnx.commit()
        except Error as e:
            print(e)

    def list_category(self):
        sql =   """
                SELECT * from category, expense
                WHERE category.id = expense.id
                """
        try :
            c = self.cnx.cursor()
            c.execute(sql)
            categorys = c.fetchall()
            return categorys
        except Error as e:
            print(e)

class Expenses:
    def __init__(self) -> None:
        self.database = "category.db"

    def create_connection(self):
        self.cnx = None
        try: 
            self.cnx = sqlite3.connect(self.database)
        except Error as e:
            print(e)
        ##return self.cnx
    
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS expense(
            id integer PRIMARY KEY,
            description text NOT NULL,
            date text NOT NULL,
            amount integer NOT NULL  
            )   
"""
        try:
            c = self.cnx.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

    def add_expense(self, description, date, amount):
        sql =   """
                INSERT INTO expense(description, date, amount)
                VALUES (?,?,?)
                """
        params = (description, date, int(amount))
        try:
            c = self.cnx.cursor()
            c.execute(sql, params)
            self.cnx.commit()
        except Error as e:
            print(e)
            raise e
        return c.lastrowid ##Return ออกมาเพื่อ Check result    

    def update_expense(self, description, amount):
        # Update amount data 
        sql =   """
                UPDATE expense
                SET amount = ?
                WHERE description = ?
                """
        params = (int(amount), description)
        try : 
            c = self.cnx.cursor()
            c.execute(sql, params)
            self.cnx.commit()
        except Error as e:
            print(e)
            raise e

    def display_expense(self):
        c = self.cnx.cursor()
        c.execute("SELECT * FROM expense")
        db = c.fetchall()
        print(db)

def main():
    ## inital program
    category = Category()
    expenses = Expenses()
    category.create_connection()
    category.create_table()
    expenses.create_connection()
    expenses.create_table()
    ##User interface
    ui = User_interface()           
    ui.main_menu()
    ##Input checking and processing
    while True :                   
        user_input = ui.action()
        if user_input[0] == '1':
        ## user_input = [choice, category_name, expense_nmae, date, amount]
            category.add_category(user_input[1], user_input[2])
            expenses.add_expense(user_input[2], user_input[3], user_input[4])
        elif user_input[0] == '2':
        ## user_input = [choice, expense_name, amount]
            expenses.update_expense(user_input[1], user_input[2])
        elif user_input[0] == '3':
        ## user_input = [choice]
            display = category.list_category()
            for i in display:
                print(f'ID : {i[0]}, i : {i[1]}, Expane name : {i[2], }, Date : {i[5]}, Amount : {i[6]}')  
        else :
            print("exist program")
            break


if __name__ == "__main__":
    main()

## link multiple database
## display database