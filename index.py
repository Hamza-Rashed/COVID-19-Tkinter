from tkinter import * ## for drowing a disktop application
from tkinter.font import Font
import matplotlib.pyplot as plt
from PIL import ImageTk , Image

class Window: # OOP
    
    """
    This class for create a multibal windows with same props
    """
    def __init__(self, root):
        self.root = root

    def welcomePage(self):
        """
        This function for welcome page and contain The styles for the Items
        """
        global FontWelcomeButton
        global FontWelcomeLable
        global FontMainButton
        FontWelcomeLable = Font(
                        family="Times",
                        size=42,
                        weight="bold",
                        slant="roman"
                    )
        FontWelcomeButton = Font(
                        family="Times",
                        size=30,
                        weight="bold",
                        slant="roman"
                    )
        FontMainButton = Font(
                        family="Times",
                        size=35,
                        weight="bold",
                        slant="roman"
                    )

        my_image = ImageTk.PhotoImage(Image.open('images_prev_ui.png')) # for Image in welcome page
        Label(self.root, image = my_image).pack(side = LEFT)

        Label(self.root, text="We are AL-Nkhba Team Preasnted \n to you a simple program for covid-19 \n around the world !!" , width = 100 , height = 7 , font = FontWelcomeLable , bg = '#f0f0f0').pack()
        Button(self.root, text="Next", command=self.mainPage , bg = 'blue' , width = 10 , height = 2 , font = FontWelcomeButton , fg = "white").pack()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight() # for size the window on welcome page
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.configure(background = '#f0f0f0') # for background
        self.root.mainloop() # for turn on the function 

    def mainPage(self):
        """
        This Function For main page which contain on all Mains Buttons
        """
        global rootMain
        rootMain = Tk()
        Button(rootMain, text="Number Of Injuries" , command = self.numberOfInjuries , bg = 'blue' , width = 22 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootMain, text="Number Of Recovery" , command = self.numberOfRecovery , bg = 'blue' , width = 22 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT)
        Button(rootMain, text="Number Of Deaths" , command = self.numberOfDeaths , bg = 'blue' , width = 22 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootMain, text="Number Of Fortified" , command = self.numberOfFortified , bg = 'blue' , width = 22 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT)
        rootMain.title("Main Page")
        w, h = rootMain.winfo_screenwidth(), rootMain.winfo_screenheight()
        rootMain.geometry("%dx%d+0+0" % (w, h))
        rootMain.configure(background = '#f0f0f0')
        rootMain.mainloop()

    def numberOfInjuries(self):
        rootMain.destroy()
        global rootInjuries
        rootInjuries = Tk()
        Label(rootInjuries, text="The number of cases of Covid-19 around the world!!" , width = 100 , height = 7 , font = FontWelcomeLable , bg = '#f0f0f0').pack()

        def graphs():
            labels = 'World population', 'Percentage of injured'
            sizes = [7800000000, 144250358]
            colors = ['blue', 'red']
            explode = (0, 0)

            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True)

            plt.axis('equal')
            plt.show()

        def graphsDate():
            months = ['3/2020', '4/2020', '5/2020', '6/2020', '7/2020', '8/2020',
                      '9/2020', '10/2020', '11/2020', '12/2020', '1/2021', '2/2021', '3/2021', '4/2021']
            Numbers = [89000, 140000, 158000, 180000, 290000, 295000,
                       322000, 551000, 595000, 760000, 530000, 400000, 650000, 832000]
            plt.plot(months, Numbers, linestyle='dashed', color='blue')
            plt.xticks(months, months)
            plt.ylabel('The number of injured')
            plt.xlabel('Months')
            plt.show()

        Button(rootInjuries, text="Percentage of the number \n of injured", command=graphs , bg = 'purple' , width = 30 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootInjuries, text="The rate of increase in injuries \n with dates",
               command=graphsDate , bg = 'purple' , width = 30 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT)
        Button(rootInjuries, text="Back To Main Page" , command = self.mainPage , bg = 'blue' , width = 22 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        rootInjuries.title("Cases of injuries")
        w, h = rootInjuries.winfo_screenwidth(), rootInjuries.winfo_screenheight()
        rootInjuries.geometry("%dx%d+0+0" % (w, h))
        rootInjuries.configure(background = '#f0f0f0')
        rootInjuries.mainloop()

    def numberOfRecovery(self):
        rootMain.destroy()
        global rootRecovery
        rootRecovery = Tk()
        Label(rootRecovery, text="Cases that have recovered from Covid 19 around the world!!" , width = 100 , height = 7 , font = FontWelcomeLable , bg = '#f0f0f0').pack()

        def graphs():
            labels = 'Percentage of Recovered', 'Percentage of injured'
            sizes = [122712466, 144250358]
            colors = ['blue', 'red']
            explode = (0.1, 0)

            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True)

            plt.axis('equal')
            plt.show()

        def graphsDate():
            months = ['3/2020', '4/2020', '5/2020', '6/2020', '7/2020', '8/2020',
                      '9/2020', '10/2020', '11/2020', '12/2020', '1/2021', '2/2021', '3/2021', '4/2021']
            Numbers = [49000, 135000, 136000, 120360, 245000, 222500,
                       318000, 535000, 580000, 756000, 580000, 367000, 590000, 750600]
            plt.plot(months, Numbers, linestyle='dashed', color='blue')
            plt.xticks(months, months)
            plt.ylabel('The number of Recovered')
            plt.xlabel('Months')
            plt.show()

        Button(rootRecovery, text="Percentage of the number \n of recovered", command=graphs , bg = 'purple' , width = 30 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootRecovery, text="The rate of increase in recovered \n with dates",
               command=graphsDate , bg = 'purple' , width = 30 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootRecovery, text="Back To Main Page" , command = self.mainPage , bg = 'blue' , width = 22 , height = 5 , font = FontMainButton, fg = "white").pack(side = LEFT , padx = 50)
        rootRecovery.title("Cases of Recovered")
        w, h = rootRecovery.winfo_screenwidth(), rootRecovery.winfo_screenheight()
        rootRecovery.geometry("%dx%d+0+0" % (w, h))
        rootRecovery.configure(background = '#f0f0f0')
        rootRecovery.mainloop()

    def numberOfDeaths(self):
        rootMain.destroy()
        global rootDeaths
        rootDeaths = Tk()
        Label(rootDeaths, text="The number of Deaths Because of Covid-19 around the world" , width = 100 , height = 7 , font = FontWelcomeLable , bg = '#f0f0f0').pack()

        def graphs():
            labels = 'Percentage of Deaths', 'Percentage of injured'
            sizes = [3073896, 144250358]
            colors = ['blue', 'red']
            explode = (0.1, 0)

            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True)

            plt.axis('equal')
            plt.show()

        def graphsDate():
            months = ['3/2020', '4/2020', '5/2020', '6/2020', '7/2020', '8/2020',
                      '9/2020', '10/2020', '11/2020', '12/2020', '1/2021', '2/2021', '3/2021', '4/2021']
            Numbers = [4300, 7200, 4400, 5310, 6507, 4200,
                       5700, 6710, 7820, 14100, 17100, 6300, 12000, 14125]
            plt.plot(months, Numbers, linestyle='dashed', color='blue')
            plt.xticks(months, months)
            plt.ylabel('The number of Recovered')
            plt.xlabel('Months')
            plt.show()

        Button(rootDeaths, text="Percentage of the number \n of Deaths", command=graphs , bg = 'purple' , width = 30 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootDeaths, text="The rate of increase in Deaths \n with dates",
               command=graphsDate , bg = 'purple' , width = 30 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootDeaths, text="Back To Main Page" , command = self.mainPage , bg = 'blue' , width = 22 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        rootDeaths.title("Cases of Deaths")
        w, h = rootDeaths.winfo_screenwidth(), rootDeaths.winfo_screenheight()
        rootDeaths.geometry("%dx%d+0+0" % (w, h))
        rootDeaths.configure(background = '#f0f0f0')
        rootDeaths.mainloop()

    def numberOfFortified(self):
        rootMain.destroy()
        global rootFortified
        rootFortified = Tk()
        Label(rootFortified, text="Cases that have Fortified from Covid 19 around the world!!" , width = 100 , height = 7 , font = FontWelcomeLable , bg = '#f0f0f0').pack()

        def graphs():
            labels = 'Percentage of Fortified', 'Percentage of injured'
            sizes = [217000000, 144250358]
            colors = ['blue', 'red']
            explode = (0.1, 0)

            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True)

            plt.axis('equal')
            plt.show()

        def graphsDate():
            months = ['2/2021', '3/2021', '4/2021']
            Numbers = [45600000, 65450000, 105950000]
            plt.plot(months, Numbers, linestyle='dashed', color='blue')
            plt.xticks(months, months)
            plt.ylabel('The number of Fortified')
            plt.xlabel('Months')
            plt.show()

        Button(rootFortified, text="Percentage of the number \n of Fortified", command=graphs , bg = 'purple' , width = 30 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootFortified, text="The rate of increase in Fortified \n with dates",
               command=graphsDate , bg = 'purple' , width = 30 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        Button(rootFortified, text="Back To Main Page" , command = self.mainPage , bg = 'blue' , width = 22 , height = 5 , font = FontMainButton , fg = "white").pack(side = LEFT , padx = 50)
        rootFortified.title("Cases of Fortified")
        w, h = rootFortified.winfo_screenwidth(), rootFortified.winfo_screenheight()
        rootFortified.geometry("%dx%d+0+0" % (w, h))
        rootFortified.configure(background = '#f0f0f0')
        rootFortified.mainloop()


if __name__ == '__main__': # for turn on the welcome page
    root = Tk()
    mainRoot = Window(root)
    mainRoot.welcomePage()
