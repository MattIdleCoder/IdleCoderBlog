#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple graphical user interface (GUI) template for use as a front-end for
configuring and launching any Python code that manipulates text and files from
the command line.
 
Designed for fast development of user interfaces for Python programs that
read and manipulate text from a small number of input files.
 
Please read the comments and follow the instructions to adapt it for launching
your own code.
 
@author: matta_idlecoder@protonmail.com
"""
 
"""All imported tkinter functions and variables have been named.
The first four lines could all have been replaced by:

    from tkinter import *

This way, you keep track of the source of your functions, and have an
explicit inventory of what is being imported from where, which is useful for
porting to other GUI systems later, should you ever want to do so:
"""
from tkinter import Tk, Frame, StringVar, IntVar
from tkinter import NORMAL, DISABLED, RAISED, END
from tkinter import Button, Radiobutton, Checkbutton
from tkinter import Toplevel, Entry, Label
import tkinter.constants, tkinter.filedialog
import tkinter.messagebox
import os
 
"""This is where you import your own underlying logic file as a Python module
and name your functions you will be calling. It's a shorter way of saying:
"from AnalyseThis.py import analyse_this() and all the functions it uses"
"""
from AnalyseThis import analyse_this
 
 
class PythonGUI(Frame):
    """The object space for creating your dashboard and launching your app
 
    Within this class, every function and widget can see every other's
    self.variables. In this way, the self-space scope within a class can be
    thought of as halfway between local and global.
    """
    def __init__(self, root):
        """This is where you define & initialise all your GUI variables
        """
        Frame.__init__(self, root)
        self.master = root
 
        # define the default button appearance: wrap any text to 6cm wide block:
        self.std_button_opts = {'wraplength':"6c", 'relief':RAISED, 'bd':4, 'pady':5}
 
 
        """ Define the default file options for opening files:
        """
        self.file_opt = {}
 
        """this is appended to any filename the user offers as a filename,
        if they forget to add an extension: """
        self.file_opt['defaultextension'] = '.txt'
 
        """ This can be set to a default filename. Here, I'm just using it
        as a reminder to the user :
        self.file_opt['initialfile'] = '*.txt'
        """
 
        """ This is where you tell tkinter what type of files you want to show
        the user when they open a tkinter file open/save window, 'e.g:
        self.file_opt['filetypes'] =  [('PNG files', '*.png'),
        ('JPEG files', '*.jpg'), ('PDF files', '*.pdf')]
        """
        self.file_opt['filetypes'] = [('text files', '.txt')]
 
        """ '.' is the current folder, i.e. where this prog was launched from
        If you have different folders for input and output files, redefine
        this variable in each file open/save function that is called:
        """
        self.file_opt['initialdir'] = '.'
 
        # the window to disable when the file open/save window opens on top of it:
        self.file_opt['parent'] = root
 
        self.text_name = 'None chosen'
        self.text_path_and_name = None
        self.save_path_and_name = None
 
        self.dict_path_and_name = './EnglishDictionary.txt'
        """ ^^^ This is the line where you would define a separate
        default folder for your config files, should you decide to keep
        input, config and output files apart. Make sure the folder exists
        before you run the code. e.g:
        self.dict_path_and_name = '../ConfigFiles/ConfigSettings.txt'
        """
 
 
        """ Define and initialise any info status variables here that will
        be set and displayed by widgets:
        """
        # default text strings to be displayed on buttons:
        self.textstatus = StringVar()
        self.textstatus.set('Choose a text file to analyse')
 
        self.dictstatus = StringVar()
        self.dictstatus.set('Change the dictionary')
 
        self.StartTrigButtonName = StringVar()
        self.StopTrigButtonName = StringVar()
        self.StartTriggerDisp = StringVar()
        self.StopTriggerDisp = StringVar()
 
 
        """ Define and initialise all the variables here you will want to pass
        to your underlying logic after setting them in your GUI. They must be
        defined in tkinter terms of StringVar(), IntVar() and DoubleVar(). Note
        that there is no Boolean() type. Is this is required, use IntVar() and
        set it to 0 or 1. All types can also be set to None if not set:
        """
        self.StartTrigger = StringVar()
        self.StopTrigger = StringVar()
 
        self.SortByAlpha = IntVar()
        self.ListContractions = IntVar()
        self.IgnoreAndListPropers = IntVar()
        self.SplitCompoundsAndList = IntVar()
        self.spellcheck = IntVar()
 
        self.SortByAlpha.set(1)
        self.ListContractions.set(1)
        self.IgnoreAndListPropers.set(1)
        self.SplitCompoundsAndList.set(1)
        self.spellcheck.set(1)
 
        # initialise all string variables that will need reset when the
        # input file changes:
        self.reset_all_start_trigger_vars()
        self.reset_all_stop_trigger_vars()
 
        # Call your dashboard:
        self.YourAppDashboard()
        return
 
 
    def YourAppDashboard(self):
        """The function that creates your dashboard and all its widgets
        """
 
        # default options for widgets on this dashboard:
        std_pos_opts = {'fill':tkinter.constants.BOTH, 'padx':10}
 
        BlankLine = ' ' * 80  # Simple way to space things out
 
        """ This is a basic GUI fetch filename widget, calling on a specific
        function that knows what kind of filename to look for.
 
        self.textstatus = what will be displayed on the Button
 
        self.textvariable = the variable that will be set by the user
        interacting with the button.
 
        In this case they are the same, which has the effect that the button
        can be used to show the name of the file ] you pick. Note that it is
        just a name. The file will be opened later by your underlying logic:
        """
        Button(self, textvariable=self.textstatus, font=('Helvetica', 16),
               command=self.GetNameOfTextToAnalyse,
               **self.std_button_opts).pack(pady=20, **std_pos_opts)
 
        """ Two simple widgets for asking the user for text strings. Most of
        the complexity is beneath the hood in the commands they call:
        """
        Button(self, textvariable=self.StartTrigButtonName,
               command=self.GetStartTrig, **self.std_button_opts).pack(pady=5,
               **std_pos_opts)
 
        Button(self, textvariable=self.StopTrigButtonName,
               command=self.GetStopTrig, **self.std_button_opts).pack(pady=5,
               **std_pos_opts)
 
        Label(self, text=BlankLine).pack()
 
        """These three are all do the same thing. Each defines a checkbutton,
        and the variable that will be set to either 0 or 1 by the user
        clicking on the Checkbutton:
        """
        Checkbutton(self, text="List proper nouns separately",
                    variable=self.IgnoreAndListPropers).pack(**std_pos_opts)
 
        Checkbutton(self, text='List contractions used',
                    variable=self.ListContractions).pack(**std_pos_opts)
 
        Checkbutton(self, text='List hyphenated compounds\nwords separately',
                    variable=self.SplitCompoundsAndList).pack(**std_pos_opts)
 
        Label(self, text=BlankLine).pack()
 
        """This widget uses the value of self.spellcheck to control whether the
        widget bwlow it is enabled or disabled, i.e whether the user can click
        on it or not. If the user disables the spellcheck, he/she isn't going
        to need a dictionary. Each time this Checkbutton widget is checked or
        unchecked, the handler function self.onSpellCheck() above looks at the
        new value of the variable self.spellcheck and either enables or
        disables the widget self.SelectDictButton below: """
        Checkbutton(self, text='Do a spell check', variable=self.spellcheck,
                    command=self.onSpellCheck).pack(**std_pos_opts)
 
        """ This is the same basic fetch filename and path widget that was used
        to call self.GetNameOfTextToAnalyse at the top of this function. This
        time it calls self.GetNameOfDictToUse to allow the user to select a
        different dictionary. Its default state is NORMAL, which means
        'enabled'. The handler self.onSpellCheck called by the above widget
        will enable or disable this widget, depending on the value of
        self.spellcheck: """
        self.SelectDictButton = Button(self, text=self.dictstatus,
               textvariable=self.dictstatus, command=self.GetNameOfDictToUse,
               state=NORMAL, **self.std_button_opts)
 
        """When giving a widget a name (to allow its configuration options to
        be set elsewhere) you need to separate the Button definition above
        from its geometry drawing command (i.e. pack, grid or place) so that
        the name you assign to it (in this case self.SelectDictButton=) is
        not None: """
        self.SelectDictButton.pack(**std_pos_opts)
 
        Label(self, text=BlankLine).pack()
 
        """These two radiobuttons are connected by the same variable, in this
        case SortByAlpha. However, each widget will set SortByAlpha to a
        different value. Since the Radiobuttons also reflect the current value,
        by selecting one, you therefore de-select the other:
        """
        Radiobutton(self, text='Sort word frequency analysis\nalphabetically by word',
                    variable=self.SortByAlpha, value=1).\
                    pack(**std_pos_opts)
 
        Radiobutton(self, text='Sort word frequency analysis\nby word frequencies',
                    variable=self.SortByAlpha, value=0).\
                    pack(**std_pos_opts)
 
        # This button calls a handler function that calls your underlying logic
        Button(self, text='Analyse', command=self.run_my_code, relief=RAISED,
               bd=4, padx=10, pady=5, font=('Helvetica', 16)).pack(padx=10, pady=10)
 
        """ self.quit is a built-in tkinter function defined as "Quit the
        interpreter. All widgets will be destroyed." Resistance is futile:
        """
        Button(self, text='Quit', command=self.quit, relief=RAISED,
               bd=4, padx=10, pady=5, font=('Helvetica', 16)).pack(padx=5, pady=10)
        return
 
 
    def GetNameOfTextToAnalyse(self):
        """Returns a filename for your own code to open elsewhere
        """
        if self.text_path_and_name: # a text has been chosen before
            self.file_opt['initialdir'], old_text_name = os.path.split(self.text_path_and_name)
        else:
            old_text_name = self.text_name
            self.file_opt['initialdir'] = '.'
            """ This is where you would define a separate default folder for
            your input text files, should you decide to keep input, config and
            output files apart. Make sure the folder exists before you run the
            code:
            self.file_opt['initialdir'] = '../Input Files'
            """
 
        OldTextFilePath = self.text_path_and_name
 
        # Define what the user will see in the open file window:
        self.file_opt['title'] = 'Choose a text file to analyse:'
        self.file_opt['initialfile'] = ''
 
        # returns a file path and name, or '':
        self.text_path_and_name = tkinter.filedialog.askopenfilename(**self.file_opt)
        if self.text_path_and_name:  # if it's not '':
            # User didn't hit cancel:
            text_path, self.text_name = os.path.split(self.text_path_and_name)
            self.reset_all_start_trigger_vars()
            self.reset_all_stop_trigger_vars()
        else:
            # User hit cancel. Reset path to last value:
            self.text_path_and_name = OldTextFilePath
            self.text_name = old_text_name
 
        self.textstatus.set('TEXT: ' + self.text_name)
        return
 
 
    def save_as_file(self, result):
        """ Saves the result of your program to a file
        """
        if self.save_path_and_name:
            # a file has been saved before. Go to the same place:
            self.file_opt['initialdir'], save_name = os.path.split(self.save_path_and_name)
        #else:
            """ This is where you would define a separate default folder for
            your output files, should you decide to keep input, config and
            output files apart. Make sure the folder exists before you run the
            code.
            self.file_opt['initialdir'] = '../Output Files'
            """
 
        OldSaveFilePath = self.save_path_and_name
 
        # create the name of your results file:
        if "." in self.text_name:
            basename, suffix = self.text_name.split(".")
        else:
            # Just in case the text chosen does not have a .txt suffix:
            basename = self.text_name
 
        # Define what the user will see in the save file window:
        self.file_opt['title'] = "Save results to:"
        self.file_opt['initialfile'] = basename + '.Analysis.txt'
 
        # returns a file path and name, or '':
        self.save_path_and_name = tkinter.filedialog.asksaveasfilename(**self.file_opt)
        if self.save_path_and_name:  # if it's not '':
            # user didn't hit cancel:
            file = open(self.save_path_and_name, 'w')
            file.write(result)
            file.close
            self.file_opt['initialdir'], save_name = os.path.split(self.save_path_and_name)
        else:
            # User hit cancel. Reset path to last value:
            self.save_path_and_name = OldSaveFilePath
        return
 
 
    def GetNameOfDictToUse(self):
        """Called when the user wants to select another dictionary file to use
        """
        OldDictPath = self.dict_path_and_name
        self.file_opt['initialdir'], old_dict_name = os.path.split(OldDictPath)
 
        # Define what the user will see in the choose config file window:
        self.file_opt['title'] = 'Choose a dictionary to use:'
        self.file_opt['initialfile'] = ''
 
        # returns a file path and name, or '':
        self.dict_path_and_name = tkinter.filedialog.askopenfilename(**self.file_opt)
        if self.dict_path_and_name:
            # User didn't hit cancel:
            dict_path, new_dict_name = os.path.split(self.dict_path_and_name)
        else:
            # User hit cancel. Reset path to dictionary to last value:
            self.dict_path_and_name = OldDictPath
            new_dict_name = old_dict_name
 
        self.dictstatus.set('Dictionary chosen: ' + new_dict_name)
        return
 
 
    def GetStartTrig(self):
        """Opens Entry dialog box to paste start trigger text into
        """
        self.StartTrigWin = Toplevel(self)
        root.grab_release()
        self.StartTrigWin.grab_set()
 
        # This should almost line up the sub-windows up with the buttons that
        # called them, but may need adjusting for different platforms/screens:
        geom_string = "+{}+{}".format(w-120, h+90)
        self.StartTrigWin.geometry(geom_string)
 
        self.StartTrigWin.title('Set Your Start Trigger')
 
        Instruction = "\nCut and paste a suitable START text trigger from your "
        Instruction += "text file into the space below. Don't worry about "
        Instruction += "putting it in quotation marks. The analysis will only "
        Instruction += "begin AFTER this text string has been found. It need"
        Instruction += " not be long - or unique - but it must be the first "
        Instruction += "time it occurs in the text file, and identify the point "
        Instruction += "after which the actual literary work begins (after the"
        Instruction += " publisher's preamble, forewords, etc):"
 
        # Wrap the above text into an 11cm wide paragraph:
        Label(self.StartTrigWin, text=Instruction, wraplength="11c").pack(pady=5)
 
        TriggerEntry = Entry(self.StartTrigWin, textvariable=self.StartTriggerDisp,
                             width=80, justify='center')
        TriggerEntry.pack(pady=5)
        TriggerEntry.focus_set()  # make the Entry box the active widget
        TriggerEntry.select_range(0, END)  # highlight all the text
 
        button_1_title = "START analysing my text file only after finding the "
        button_1_title += "above text trigger."
        Button(self.StartTrigWin, text=button_1_title,
               command=self.onStartButton1,
               **self.std_button_opts).pack(pady=5)
 
        button_2_title = "Don't worry about using a start trigger. Start "
        button_2_title += "analysing my text file from the BEGINNING."
        Button(self.StartTrigWin, text=button_2_title,
               command=self.onStartButton2,
               **self.std_button_opts).pack(pady=5)
        return
 
 
    def onStartButton1(self):
        """This is called when the user wants to save the pasted start trigger
        """
        if (self.StartTriggerDisp.get()[:3] == '===')  or \
            (len(self.StartTriggerDisp.get()) == 0):
            self.reset_all_start_trigger_vars()
        else:
            # Newline forces button to 2 lines, which maintains the layout:
            self.StartTrigger.set(self.StartTriggerDisp.get())
            self.StartTrigButtonName.set('START trigger is SET')
 
        self.StartTrigWin.destroy()
        return
 
 
    def onStartButton2(self):
        """Called when the user decides not to save the pasted start trigger
        """
        self.reset_all_start_trigger_vars()
        self.StartTrigWin.destroy()
        return
 
 
    def reset_all_start_trigger_vars(self):
        """Resets all variables related to the start triggers
        """
        self.StartTrigButtonName.set('No start trigger is set: analyse from the BEGINNING')
        self.StartTriggerDisp.set('=== COPY & PASTE YOUR START TRIGGER TEXT HERE ===')
        self.StartTrigger.set("")
        return
 
 
    def GetStopTrig(self):
        """Opens an Entry dialog box to paste the stop trigger text into
        """
        self.StopTrigWin = Toplevel(self)
        root.grab_release()
        self.StopTrigWin.grab_set()
 
        # This should almost line up the sub-windows up with the buttons that
        # called them, but may need adjusting for different platforms/screens:
        geom_string = "+{}+{}".format(w-120, h+150)
        self.StopTrigWin.geometry(geom_string)
 
        self.StopTrigWin.title('Set Your Stop Trigger')
 
        Instruction = "\nCut and paste a suitable STOP text trigger from your "
        Instruction += "text file into the space below. The analysis will stop "
        Instruction += "when this text is found. It need not be long, but it "
        Instruction += "must be the first time it occurs in the text file, and "
        Instruction += "identify the end of the actual literary work, before "
        Instruction += "the index, glossary, etc. It will not be part of the "
        Instruction += "analysis. Don't worry about putting it in quotation marks:"
 
        # Wrap the above text into an 11cm wide block:
        Label(self.StopTrigWin, text=Instruction, wraplength="11c").pack(pady=5)
 
        TriggerEntry = Entry(self.StopTrigWin,
                                  textvariable=self.StopTriggerDisp,
                                  width=80, justify='center')
        TriggerEntry.pack(pady=5)
        TriggerEntry.focus_set()  # make the Entry box the active widget
        TriggerEntry.select_range(0, END)  # highlight all the text
 
        button_1_title = "STOP analysing my text file when the the above STOP "
        button_1_title += "text trigger is found."
        Button(self.StopTrigWin, text=button_1_title,
               command=self.onStopButton1, **self.std_button_opts).pack(pady=5)
 
        button_2_title = "Don't worry about using a stop trigger. Analyse my"
        button_2_title += "text file all the way to the END."
        Button(self.StopTrigWin, text=button_2_title,
               command=self.onStopButton2,
               **self.std_button_opts).pack(pady=5)
        return
 
 
    def onStopButton1(self):
        """This is called when the user wants to save the pasted stop trigger
        """
        if (self.StopTriggerDisp.get()[:3] == '===') or \
            (len(self.StopTriggerDisp.get()) == 0):
            self.reset_all_stop_trigger_vars()
        else:
            # Newline forces button to 2 lines, which maintains the layout:
            self.StopTrigger.set(self.StopTriggerDisp.get())
            self.StopTrigButtonName.set('STOP trigger is SET')
 
        self.StopTrigWin.destroy()
        return
 
 
    def onStopButton2(self):
        """Called when the user decides not to save the pasted stop trigger
        """
        self.reset_all_stop_trigger_vars()
        self.StopTrigWin.destroy()
        return
 
 
    def reset_all_stop_trigger_vars(self):
        """Resets all variables related to the stop triggers
        """
        self.StopTrigButtonName.set('No stop trigger is set: analyse all the way to the END')
        self.StopTriggerDisp.set('=== COPY & PASTE YOUR STOP TRIGGER TEXT HERE ===')
        self.StopTrigger.set("")
        return
 
 
    def onSpellCheck(self):
        """Enables/disables dictionary selector button
        """
        if self.spellcheck.get():
            self.SelectDictButton.config(state=NORMAL)
        else:
            self.SelectDictButton.config(state=DISABLED)
        return
 
 
    def run_my_code(self):
        """A simple wrapper to pass your dashboard-set variables to your logic
        """
        result = ''
 
        if self.text_name == 'None chosen':
            tkinter.messagebox.showinfo(title='Error: no text file chosen.   ',
                message="Please choose a text to analyse.", icon='error')
 
        else:
            """You don't explicitly have to set and pass EVERY variable to your
            logic. Some can be preset here, while others by omission can assume
            their defaults as set in your logic's function definition. This
            makes your GUI tidier by omitting both types from your dashboard.
            For example, here the optional kwargs ListingArchaisms and
            RemovingRomans have assumed their defaults of True (by not being
            named). On the other hand, the kwargs ListingAdverbs and
            ListingGerunds have been explicitly disabled here, over-ruling
            their defined defaults:
            """
            result = analyse_this(self.text_path_and_name,
                        self.dict_path_and_name,
                        SortByAlpha=self.SortByAlpha.get(),
                        StartTrigger=self.StartTrigger.get(),
                        StopTrigger=self.StopTrigger.get(),
                        CheckingSpelling=self.spellcheck.get(),
                        SplitAndListCompounds=self.SplitCompoundsAndList.get(),
                        IgnoreNListProperNouns=self.IgnoreAndListPropers.get(),
                        ListingContractions=self.ListContractions.get(),
                        ListingAdverbs=False,
                        ListingGerunds=False)
 
            self.save_as_file(result)
        return  # control to your dashboard
 
 
if __name__=='__main__':
    root = Tk()
 
    HalfScreenWidth = int(root.winfo_screenwidth()/2)
    HalfScreenHeight = int(root.winfo_screenheight()/2)
 
    w = HalfScreenWidth - 200
    h = HalfScreenHeight - 350
    # Centre window:
    geom_string = "+{}+{}".format(w, h)
 
    root.geometry(geom_string)
    root.title('Dashboard')
    root.lift()
    PythonGUI(root).pack()
 
    root.mainloop()

