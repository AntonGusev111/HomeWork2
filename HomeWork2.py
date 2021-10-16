from pprint import pprint
import os
import glob
import collections
#Tasks 1 and 2
class cooking:
    def __init__(self, name):
        self.name = name

    def load_file(self):
        path=os.path.join(os.getcwd(), self.name)
        with open(path,"r", encoding="utf-8") as f:
            cook_book = {}
            for dish in f:
                dish_name = dish.strip()
                counter = int(f.readline().strip())
                ingredients = []
                for i in range(counter):
                    ingredient_name,quantity,measure = f.readline().split("|")
                    ingredients.append({"ingredient_name":ingredient_name,"quantity":quantity,"measure":measure})
                cook_book[dish_name] = ingredients
                f.readline()
        return cook_book

    def ingredients_calc(self, dishes, person_count):
        cook_book=self.load_file()
        result={}
        for item in dishes:
            for r in cook_book.get(item):
                if r.get('ingredient_name') in result:
                    result[r.get('ingredient_name')]['quantity']+= int(r.get("quantity"))*person_count
                else:
                    result[r.get('ingredient_name')]= {'measure':r.get('measure').strip(),'quantity':int(r.get("quantity"))*person_count}
        return(result)

cook_set=cooking('recipes.txt')
pprint(cook_set.load_file())
pprint(cook_set.ingredients_calc(['Запеченный картофель','Омлет'],2))

#Task 3

def read_and_write (f_path):
    os.chdir(f_path)
    f_names=[]
    read_result={}
    for files in glob.glob("*.txt"):
        f_names.append(files)
    for i in range(len(f_names)):
        path=os.path.join(os.getcwd(), f_names[i])
        with open(path,"r", encoding="utf-8") as f:
            text=f.readlines()
            read_result[len(text)] = {"file_name":f_names[i],"text":text}
    read_result=collections.OrderedDict(sorted(read_result.items()))
    if not os.path.exists('result'):
        os.mkdir("result")
        os.chdir('result')
    else:
        os.chdir('result')
    with open('result.txt', 'w', encoding="utf-8") as f:
        for i in read_result:
            f.write(f"{read_result[i]['file_name']} \n")
            f.write(f'{str(i)}\n')
            f.write(f"{''.join(read_result[i]['text'])} \n")

read_and_write('task3')