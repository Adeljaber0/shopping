shopping_list=[]

#اضافة العناصر 
def add_list():
    item =input("ُEnter the item name to add:")
    # فحص اذا كان في فراغ اطبع الرسالة الي تحت واطلع من البرنامج
    if item.strip()==" ":
        print ("It is not allowed to enter without value")
        return
    #افحص اذا كان العنصر 3 احرف او اكثر
    if len(item)< 3 :
        print("Enter an element that contains at least three letters")
        return
    #productافحص انه المدخل فيه كلمة
    if "product" not in item:
        print("Enter an element that contains Product keyword")
        return 

    shopping_list.append(item)
    print (f"{item} In addition to the shopping menu")
  
  
  
def show_list():
#كل اشي بدخل على القائمة حطه ب  x واطبع
    print ("list items:")
    for x in shopping_list:
        print (x)

def delete_item():
    #لحذف بعض العناصر 
    item=input("Enter the item name to delete:")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}'It was successfully deleted")    
    else:
        print (f"'{item}'The element does not exist")
     
def exit_item():
    print ("exit pro")
 
 
 
 
user= int (input("enter the opertion 1.add - 2.show  -3.delete:"))

if user==1:
        add_list()

elif user==2:
        show_list()

elif user==3:
        delete_item()
                
else:
        print("erore")
        
