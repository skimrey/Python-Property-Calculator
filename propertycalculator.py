import tkinter as tk


def propertyCalc():
    
    def getIncome():
        
        rental = int(e1.get() or "0")
        laundry = int(e2.get() or "0")
        storage = int(e3.get() or "0")
        misc = int(e4.get() or "0")
        income = misc + storage + laundry + rental
        return income
        
    def getExpenses():
        
        mortgage = int(e5.get() or "0")
        hoa = int(e6.get() or "0")
        lawnsnow = int(e7.get() or "0")
        vacancy = int(e8.get() or "0")
        repairs = int(e9.get() or "0")
        capex = int(e10.get() or "0")
        propmgmt = int(e11.get() or "0")
        tax = int(e12.get() or "0")
        insurance = int(e13.get() or "0")
        electric = int(e14.get() or "0")
        water = int(e15.get() or "0")
        sewer = int(e16.get() or "0")
        gas = int(e17.get() or "0")
        totalexpense = gas + sewer + water + electric + insurance + tax + propmgmt + capex + repairs + vacancy + lawnsnow + hoa + mortgage
        return totalexpense
        
            
    def determineFlow():
        
            cashflow = getIncome() - getExpenses()
            return cashflow
        
        
    def getROI():
        
        downpayment = int(e18.get() or "0")
        closingcosts = int(e19.get() or "0")
        rehab = int(e20.get() or "0")
        misc = int(e21.get() or "0")
        totalinvestment = downpayment + closingcosts + rehab + misc
        annualcashflow = determineFlow() * 12
        ROI = (annualcashflow / totalinvestment) * 100
        return ROI
        
    def startCalc():
        
        cashflow = determineFlow()
        totalexpenses = getExpenses()
        income = getIncome()
        ROI = getROI()
        result= tk.Tk()
        tk.Label(result, 
             text=f"Your monthly income is ${income}",).grid(row=0, column=3)
        tk.Label(result, 
             text=f"Your monthly expenses are ${totalexpenses}").grid(row=1, column=3)
        tk.Label(result, 
             text=f"This means your monthly cash flow is ${cashflow}").grid(row=2, column=3)
        tk.Label(result, 
             text=f"Your cash on cash ROI is therefore {ROI}%").grid(row=3, column=3)
            
        
    master = tk.Tk()
    
    tk.Label(master, 
             text="Income ", font='bold').grid(row=0)
    tk.Label(master, 
             text="Rental: ").grid(row=1)
    tk.Label(master, 
             text="Laundry: ").grid(row=2)
    tk.Label(master, 
             text="Storage: ").grid(row=3)
    tk.Label(master, 
             text="Misc: ").grid(row=4)
    tk.Label(master, 
             text=" ").grid(row=5)
    tk.Label(master, 
             text="Expenses ", font='bold').grid(row=6)
    tk.Label(master, 
             text="Mortgage:  ").grid(row=7)
    tk.Label(master, 
             text="HOA: ").grid(row=8)
    tk.Label(master, 
             text="Lawn/Snow: ").grid(row=9)
    tk.Label(master, 
             text="Vacancy: ").grid(row=10)
    tk.Label(master, 
             text="Repairs:  ").grid(row=11)
    tk.Label(master, 
             text="CapEx: ").grid(row=12)
    tk.Label(master, 
             text="Prop. Management:").grid(row=13)
    tk.Label(master, 
             text="Tax: ").grid(row=14)
    tk.Label(master, 
             text="Insurance:  ").grid(row=15)
    tk.Label(master, 
             text="Electric: ").grid(row=16)
    tk.Label(master, 
             text="Water: ").grid(row=17)
    tk.Label(master, 
             text="Sewer: ").grid(row=18)
    tk.Label(master, 
             text="Gas:  ").grid(row=19)
    tk.Label(master, 
             text="  ").grid(row=20)
    tk.Label(master, 
             text="Cash on Cash ROI  ", font= 'bold').grid(row=21)
    tk.Label(master, 
             text="Down Payment: ").grid(row=22)
    tk.Label(master, 
             text="Closing Costs: ").grid(row=23)
    tk.Label(master, 
             text="Rehab Budget:  ").grid(row=24)
    tk.Label(master, 
             text="Misc Budget: ").grid(row=25)
    tk.Label(master, 
             text="").grid(row=26)
    
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e5 = tk.Entry(master)
    e6 = tk.Entry(master)
    e7 = tk.Entry(master)
    e8 = tk.Entry(master)
    e9 = tk.Entry(master)
    e10 = tk.Entry(master)
    e11 = tk.Entry(master)
    e12 = tk.Entry(master)
    e13 = tk.Entry(master)
    e14 = tk.Entry(master)
    e15 = tk.Entry(master)
    e16 = tk.Entry(master)
    e17 = tk.Entry(master)
    e18 = tk.Entry(master)
    e19 = tk.Entry(master)
    e20 = tk.Entry(master)
    e21 = tk.Entry(master)
    e22 = tk.Entry(master)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)

    e5.grid(row=7, column=1)
    e6.grid(row=8, column=1)
    e7.grid(row=9, column=1)
    e8.grid(row=10, column=1)
    e9.grid(row=11, column=1)
    e10.grid(row=12, column=1)
    e11.grid(row=13, column=1)
    e12.grid(row=14, column=1)
    e13.grid(row=15, column=1)
    e14.grid(row=16, column=1)
    e15.grid(row=17, column=1)
    e16.grid(row=18, column=1)
    e17.grid(row=19, column=1)
    
    e18.grid(row=22, column=1)
    e19.grid(row=23, column=1)
    e20.grid(row=24, column=1)
    e21.grid(row=25, column=1)

    
    tk.Button(master, 
              text='Calculate', 
              command=startCalc).grid(row=27, 
                                        column=0, 
                                        sticky=tk.W,padx=40)
   
    tk.mainloop()
    
propertyCalc()
