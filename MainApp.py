import tkinter as tk
from tkinter import ttk


class ItemDisplay(ttk.Frame):

    def __init__(self,parent,numPeople):
        ttk.Frame.__init__(self,parent)
        self.__entriesFrame = ttk.Frame(self)
        self.__entriesFrame.grid(row=0,column=0)
        self.__peopleFrame = ttk.Frame(self)
        self.__peopleFrame.grid(row=0,column=1)
        self.__name = tk.StringVar(self)
        self.__price = tk.DoubleVar(self)
        self.__people = []
        self.__build_ui()
        for _ in range(numPeople):
            self.add_person()

    def __build_ui(self):
        ttk.Entry(self.__entriesFrame,textvariable=self.__name).grid(row=0,column=0)
        ttk.Entry(self.__entriesFrame,textvariable=self.__price,width=6).grid(row=0,column=1)

    def get_name(self):
        return self.__name.get()

    def get_price(self):
        return self.__price.get()

    def add_person(self):
        self.__people.append(tk.BooleanVar())
        newCheck = ttk.Checkbutton(self.__peopleFrame, variable=self.__people[-1], onvalue=True, offvalue=False)
        newCheck.pack(side="left")

    # TODO return list of bool
    def get_people(self):
        return [i.get() for i in self.__people]

    def to_string(self):
        return f"Item {self.get_name()} at ${self.get_price()}: {self.get_people()}"


class ReceiptDisplay(ttk.Frame):

    __UNIQUE_ID = 0

    def __init__(self,parent,numPeople=0):
        ttk.Frame.__init__(self,parent)
        self.__id = ReceiptDisplay.__UNIQUE_ID
        self.__name = tk.StringVar()
        self.__name.set(f"Receipt {self.__id}")
        ReceiptDisplay.__UNIQUE_ID += 1
        self.__items = []
        self.__numPeople = numPeople
        self.__build_ui()

    def __build_ui(self):
        self.__headerFrame = ttk.Frame(self)
        self.__headerFrame.grid(row=0,column=0,sticky="w")
        ttk.Button(self.__headerFrame,text="Add Item",command=self.__add_item).grid(row=0,column=1)
        self.__itemsFrame = ttk.Frame(self)
        self.__itemsFrame.grid(row=1,column=0)

        self.__add_item()

    def __add_item(self):
        itemFrame = ttk.Frame(self.__itemsFrame)
        itemFrame.pack(side="top")
        newDisp = ItemDisplay(itemFrame,self.__numPeople)
        newDisp.grid(row=0,column=0)
        # button & command to remove the added item
        removeCommand = lambda:self.__remove_item(newDisp,itemFrame)
        ttk.Button(itemFrame,text="x",command=removeCommand,width=2).grid(row=0,column=1)

        self.__items.append(newDisp)

    def __remove_item(self,item,frame):
        self.__items.pop(self.__items.index(item))
        frame.destroy()

    def set_name(self,newname):
        self.__name.set(newname)
        
    def get_name(self):
        return self.__name.get()

    def to_string(self):
        out = f"Receipt {self.__id}:\n"
        for item in self.__items:
            out += f"\t{item}\n"
        return out.strip()

    # return list of floats
    def calc(self):
        assert(self.__numPeople > 0)
        result = [0.0 for i in range(self.__numPeople)]
        for item in self.__items:
            if sum(item.get_people()) <= 0:
                continue
            p = item.get_people()
            individualPrice = item.get_price()/sum(p)
            for i in range(len(p)):
                if p[i]:
                    result[i] += individualPrice
        return result

    def add_person(self):
        self.__numPeople += 1
        for item in self.__items:
            item.add_person()
            
            
class MainApp(tk.Frame):
    
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.__numPeople = 0
        self.__receipts = []
        self.__receiptNotebook = ttk.Notebook(self)
        self.__receiptNotebook.grid(row=0,column=0)
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(row=1,column=0)
        #ttk.Button(buttonFrame,text="Print",command=lambda:print(rd)).grid(row=0,column=0)
        #ttk.Button(buttonFrame,text="Calculate",command=lambda:print(rd.calc())).grid(row=0,column=1)
        ttk.Button(buttonFrame,text="Add Person",command=self.__add_person).grid(row=0,column=2)
        ttk.Button(buttonFrame,text="Add Receipt",command=self.__add_receipt).grid(row=0,column=3)
        
        
    def __add_receipt(self):
        newReceipt = ReceiptDisplay(self.__receiptNotebook,self.__numPeople)
        self.__receipts.append(newReceipt)
        self.__receiptNotebook.add(newReceipt,text=newReceipt.get_name())
        
    def __add_person(self):
        self.__numPeople += 1
        for r in self.__receipts:
            r.add_person()

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root).pack()
    root.mainloop()
