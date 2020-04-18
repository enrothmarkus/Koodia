"""
A tool for converting units to another unit system
Markus Enroth, 266245

Käyttöohjeet:
1. Käynnistä ohjelma
2. Valitse valikosta, minkä yksikön haluat muuttaa
3. Painamalla "Switch places" nappulaa voi valita kummin päin haluaa yksiköt muuntaa
4. Kirjoita lukuarvo kenttään ja paina "Convert" nappulaa
5. Ohjelma muuntaa yksikön

"""

from tkinter import *

#unit types
dist_types = ["mile","km"]
volume_types = ["gallon", "litre"]
temp_types = ["fahrenheit", "celsius"]
# change ratios for units
mile_in_km = 1.609344
km_in_mile = 1/mile_in_km

litre_in_gallon = 0.264172052
gallon_in_litres = 1/litre_in_gallon

celsius_in_fahrenheit = 1.8
fahrenheit_in_celsius = 1/celsius_in_fahrenheit


class UnitConverter:
    """
    Class for converting units to another unit system
    :return: None
    """
    def convert(self,value,type):
        """
        Converts units
        :param value: amout of unit inputted
        :param type: which type of unit it is
        :return: converted value
        """
        if type in temp_types:
            return self.convert_temperature(value,type)

        if type in dist_types:
            return self.convert_distance(value,type)

        if type in volume_types:
            return self.convert_volume(value,type)

    def convert_distance(self, amount, type):
        """
        Converts miles to km and km to miles
        :param amount: amount of unit inputted
        :param type: which type of unit it is
        :return: converted value
        """
        if (type == "mile"):
            return mile_in_km * amount

        if (type == "km"):
            return km_in_mile * amount

        return 0

    def convert_volume(self, amount, type):
        """
        Converts gallons to litres and litres to gallons
        :param amount: amount of unit inputted
        :param type: which type of unit it is
        :return: converted value
        """
        if (type == "gallon"):
            return gallon_in_litres * amount

        if (type == "litre"):
            return litre_in_gallon * amount

        return 0

    def convert_temperature(self, amount, type):
        """
        Converts fahrenheit to celsius and celsius to fahrenheit
        :param amount: amount of unit inputted
        :param type: which type of unit it is
        :return: converted value
        """
        if (type == "fahrenheit"):
            if amount > 0:
                return (amount - 32)*fahrenheit_in_celsius
            else:
                return -(32-amount) * fahrenheit_in_celsius

        if (type == "celsius"):
            return 32 + amount * celsius_in_fahrenheit

        return 0


class GUI:
    """
    Graphical user interface, makes unit converter visual
    :return: None
    """
    def __init__(self, uc):
        """
        Sets all buttons and labels into place
        :param uc: Unit converter
        """
        #which type of unit we are converting
        self.__type = [None]
        #in which direction we are converting units
        self.__changer = 0
        self.__uc = uc
        #forming a window and headlines into it
        self.__window = Tk()
        self.__window.title("Unit converter")
        self.__textfield1 = Label(self.__window,text = "Select unit to convert")
        self.__textfield1.grid(row=0, column=1,sticky=N+S)
        #forming menu where you can choose which unit to convert
        default = StringVar()
        default.set("Unit")
        self.__UNITS = ["Distance", "Volume", "Temperature"]
        self.__menu = OptionMenu(self.__window,default,*self.__UNITS, command=self.get_menu_value)
        self.__menu.grid(row=0, column=2)
        #labels for units to convert
        self.__unit_to_convert = Label(self.__window, text="Unit")
        self.__unit_to_convert.grid(row=1, column=0)
        self.__unit_after_convert = Label(self.__window, text="Unit")
        self.__unit_after_convert.grid(row=2, column=0)
        #forming convert and switch buttons
        self.__convert_button = Button(self.__window, text = "Convert",command=self.convert)
        self.__convert_button.grid(row=2, column=2)
        self.__switch_button = Button(self.__window, text="Switch places", command=self.switch)
        self.__switch_button.grid(row=1, column=2)

        self.__input = Entry()
        self.__input.grid(row=1, column=1)
        self.__output = Label(self.__window,text = "0")
        self.__output.grid(row=2, column=1)

        self.__window.mainloop()

    def switch(self):
        """
        Switches which way units are converted
        :return: None
        """
        if self.__type == [None]:
            return

        if self.__changer == 0:
            self.__changer = 1
            self.__unit_to_convert.configure(text=f"{self.__type[1]}: ")
            self.__unit_after_convert.configure(text=f"{self.__type[0]}: ")
        else:
            self.__changer = 0
            self.__unit_to_convert.configure(text=f"{self.__type[0]}: ")
            self.__unit_after_convert.configure(text=f"{self.__type[1]}: ")

    def get_menu_value(self,value):
        """
        If unit to be converted is changed at the menu, this funktion makes the
        needed changes
        :param value: which unit to be converted next
        :return: None
        """
        if value == "Distance":
            self.__type = dist_types
        if value == "Volume":
            self.__type = volume_types
        if value == "Temperature":
            self.__type = temp_types

        self.__changer = 0
        self.__unit_to_convert.configure(text=f"{self.__type[0]}: ")
        self.__unit_after_convert.configure(text=f"{self.__type[1]}: ")

    def convert(self):
        """
        If input is valid, converts unit with uc (unit converter)
        :return: None
        """
        #if no unit selected
        if self.__type == [None]:
            self.__output.configure(text="Please select a unit to convert")
            return
        value = self.__input.get()
        #check if input is a number that can be converted
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            value = int(value)
            return_value = self.__uc.convert(value,self.__type[self.__changer])
            self.__output.configure(text=str(return_value))
        #if input is not valid
        else:
            self.__output.configure(text="Enter a number")


def main():
     uc = UnitConverter()
     GUI(uc)


main()
