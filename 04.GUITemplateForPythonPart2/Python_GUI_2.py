#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This GUI program is designed to be used as a simple front end for the Python
command line programs that require both numerical and textual input data, and
multiple input files.
 
The Tkinter widgets that it uses are for managing multiple input text files,
but may easily be adapted to other file types. The techniques it employs are
explained, both for file management and for input checking, so that they may be
reused and re-purposed for users' command line programs.
 
When run, it will present the user with a simple front end dashboard for the
Python command line program Markov.py to select the files it will use to build
its Markov word chains. It will also ask the user to define the order of the
Markov chains to use, and the size of the output paragraph to create, saving
the results in a file name of the user's choice.
 
@author: matta_idlecoder@protonmail.com
"""
 
"""All imported TK functions and variables have been named. The first four
lines could all have been replaced by:

    from tkinter import *

This way, you know where these functions and variables came from, and you
don't have any unknown functions or variables floating around. It also provides
an explicit inventory of what is being imported and used, which is useful for
porting to other GUI systems later, should you ever want to do so:
"""

from tkinter import Tk, Frame, StringVar, IntVar
from tkinter import RAISED, END, E, W, EW, NS, CENTER, LEFT, RIGHT
from tkinter import Button, NORMAL, DISABLED
from tkinter import Toplevel, Entry, Label
import tkinter.constants, tkinter.filedialog
import tkinter.messagebox, tkinter.font
import os 
import platform
 
debugging = False
 
"""This is where you import your own underlying logic file as a Python module
and name your functions you will be calling. It's a shorter way of saying:
from Markov.py import create_markov_text_from()
"""
from Markov import create_markov_text_from
 
 
def Cardinal(integer):
    """Converts an integer from 1-4 into a cardinal text string
    """
    if integer == 1:
        return 'one'
    elif integer == 2:
        return 'two'
    elif integer == 3:
        return 'three'
    elif integer == 4:
        return 'four'
    elif integer == 5:
        return 'five'
    elif integer == 6:
        return 'six'
    elif integer >= 7:
        return str(integer)
 
 
class PythonGUI_2(Frame):
    """The object space for creating your dashboard and launching your app
 
    Within this class, every function can see every other's self.variables.
    In this way, the self-space scope within a class can be thought of as
    halfway between local and global.
    """
    def __init__(self, root):
        """This is where you define & initialise all your GUI variables
        """
        Frame.__init__(self, root)
        self.master = root
 
        self.NormalFont = ('Helvetica', 14)
        self.FancyFont = ('Caladea', 15)
 
        """To print a list of all the available fonts you can use on your
        own platform, temporarily un-comment the following 4 lines and it will
        print the available font list to your terminal window when you run:
 
        font_list = list(tkinter.font.families())
        font_list.sort()
        print("\nNumber of available fonts = {}, and here they are:".format(len(font_list)))
        print("\nfont_list = {}\n\n".format(font_list))
        """
 
        # define the default button appearance: wrap any text to 6cm wide block:
        self.std_button_opts = {'wraplength':"6c", 'relief':RAISED, 'bd':4,
                                'padx':10, 'pady':10}
 
 
        """ Define the default file options for opening files:
        """
        self.file_opt = {}
 
 
        """this is appended to any filename the user offers as a filename,
        if they forget to add an extension:
        """
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
 
        self.save_path_and_name = None
        self.path_list = []
 
 
        """ Define and initialise here any info status variables that will
        be set and displayed by widgets, or that you will want to pass to your
        underlying logic after setting them in your GUI. They must be defined
        in tkinter terms of StringVar(), IntVar() and DoubleVar() if they are
        to be set by widgets. Note that there is no Boolean() type. Is this is
        required, use IntVar() and set it to either 0 or 1. Python will
        interpret these values as True or False:
        """
        self.fileSelector = StringVar()
        self.FileCountButton = StringVar()
        self.fileSelector.set('Select files')
        self.FileCountButton.set('No files selected')
 
        self.FirstWordsButtonName = StringVar()
        self.FirstWordsDisp = StringVar()
        self.FirstWordsString = StringVar()
 
        self.OrderButtonName = StringVar()
        self.ParaLenButtonName = StringVar()
 
        self.MarkovOrder = IntVar()
        self.ParaLength = IntVar()
 
        self.MarkovOrder.set(2)
        self.ParaLength.set(200)
 
        self.OrderButtonName.set('Markov Order will be {:d}'.format(self.MarkovOrder.get()))
        self.ParaLenButtonName.set('Paragraph:{} words long'.format(self.ParaLength.get()))
 
        self.reset_first_words()
 
        # Call your dashboard:
        self.YourAppDashboard()
        return
 
 
    def YourAppDashboard(self):
        """The function that creates your dashboard and all its widgets
 
        Widgets only need the 'self' prefix if other functions within the class
        need to configure them. Otherwise, they can just be local.
        """
 
        # default options for widgets on this dashboard:
        std_pack_opts = {'padx':10, 'pady':10}
 
        BlankLine = ' ' * 80  # Simple way to space things out
 
        Label(self, text="\nMarkov Random Text Generator", font=('MS Gothic', 16)).pack()
        Label(self, text=BlankLine).pack()
 
        """This button is only made active when there are actually files to
        see. Its change of state happens in self.GetFileList, when files are
        chosen. Once self.path_list is a non-empty list, it becomes active,
        and the user can click on it. When it is clicked, OnListFile will
        simply list the filenames found in self.path_list:
        """
        self.ListFilesButton = Button(self, textvariable=self.FileCountButton,
                                font=self.NormalFont, command=self.ListFiles,
                                state=DISABLED, **self.std_button_opts)
        self.ListFilesButton.pack(**std_pack_opts)
 
        """This calls a tkinter widget that fetches multiple filenames:
        """
        Button(self, textvariable=self.fileSelector, command=self.GetFileList,
                               font=self.FancyFont,
                               **self.std_button_opts).pack(**std_pack_opts)
 
        Label(self, text=BlankLine).pack()
 
        """The same widget and underlying function that was used to set the
        start and stop triggers in the TextualAnalysis GUI:
        """
        Button(self, textvariable=self.FirstWordsButtonName,
                                command=self.GetFirstWords,
                                font=self.NormalFont,
                                **self.std_button_opts).pack(**std_pack_opts)
 
        """ These two widgets and their inderlying functions are for inputting
        and value checking numerical data. Here I'm passing input checking
        instructions to the function self.UpdateNumberButton() called by these
        widgets. These instructions are used in the function to check and set
        the variables, button names and tailor advice in the sub-windows.
 
        Note 1: normally, tkinter will not allow variables to be passed to the
        function called by the activation of the widget, which tk calls the
        handler. To get around this, you call a lambda function and pass the
        variables in the lambda call.
 
        Note 2: see the comments in self.onUpdateNumberButton() for what is
        happening with the formatting instructions being passed here.
 
        Note 3: There is no reason for using kwargs in the function call other
        than to make the code more readable. The normal reasons for using
        them - setting defaults, using optional parameters in function
        calls - may apply, but they are not the primary reason for using them:
        """
        self.OrderButton = Button(self, textvariable=self.OrderButtonName,
                                cursor='plus', font=self.NormalFont,
                                command=lambda:
                                self.UpdateNumberButton(Parent='self',
                                Variable='self.MarkovOrder',
                                ButtonName='self.OrderButtonName',
                                Font=self.NormalFont,
                                ButtonFormat='.set("Markov Order will be {:d}".format(NewValue))',
                                Title='Order',
                                Instruction='\nEnter the Markov order\nyou want to use:',
                                Advice='   Number should be between {:d} and {:d}.   ',
                                Currency='',
                                Minimum = 1, Maximum = 4),
                                **self.std_button_opts)
        self.OrderButton.pack(**std_pack_opts)
 
        self.ParaLenButton = Button(self, textvariable=self.ParaLenButtonName,
                                cursor='plus', font=self.NormalFont,
                                command=lambda:
                                self.UpdateNumberButton(Parent='self',
                                Variable='self.ParaLength',
                                ButtonName='self.ParaLenButtonName',
                                Font=self.NormalFont,
                                ButtonFormat='.set("Paragraph: {:d} words long".format(NewValue))',
                                Title='Length',
                                Instruction='\nEnter the length of paragraph\nyou want to create:',
                                Advice='   Number should be between {:d} and {:d}.   ',
                                Currency='',
                                Minimum = 100, Maximum = 1000),
                                **self.std_button_opts)
        self.ParaLenButton.pack(**std_pack_opts)
 
        Label(self, text=BlankLine).pack()
 
        # This button calls a handler function that calls your underlying logic
        Button(self, text='Create Markov Text >>>', command=self.run_my_code,
                                font=self.FancyFont,
                                **self.std_button_opts).pack(**std_pack_opts)
 
        Label(self, text=BlankLine).pack()
 
        Button(self, text='Quit', command=self.quit, font=self.NormalFont,
                                **self.std_button_opts).pack(**std_pack_opts)
        return
 
 
 
    def onAdviceOKButton(self, parent):
        """Kills the parent window when OK is clicked
        """
        self.InfoWindow.grab_release()
        eval(parent + '.grab_set()')
        self.InfoWindow.destroy()
 
 
    def InfoBox(self, Parent='root', Title='', Font=('Helvetica', 12),
                Text='Missing text'):
        """General utility for getting user confirmation on a status
        """
        self.InfoWindow = Toplevel(self)
        eval(Parent + '.grab_release()')
        self.InfoWindow.grab_set()
        geom_string = "+{}+{}".format(w-25, h+120)
        self.InfoWindow.geometry(geom_string)
        self.InfoWindow.title(Title)
 
        Label(self.InfoWindow, text=Text, width=30, font=Font,
              wraplength=200).pack(padx=10)
 
        Button(self.InfoWindow, text='OK', justify=CENTER, font=Font,
               padx=15, pady=5, command=lambda:
               self.onAdviceOKButton(Parent)).pack(pady=10)
        return
 
 
    def ListFiles(self, parent='root', MaxShow=10):
        """List the files selected by the user
        """
        NameList, FileCount = [], 0
        NumFiles = len(self.path_list)
 
        if NumFiles > MaxShow:
            if NumFiles==(MaxShow+1):
                MaxShow -=1   # avoids using a line to say  'Plus one more'
            FilesLeft = NumFiles - MaxShow  # now will always be at least 2 more
 
        for path in self.path_list:
            Folder, FileName = os.path.split(path)
            NameList.append(FileName)
            FileCount += 1
            if FileCount == MaxShow:
                if NumFiles > MaxShow:
                    NameList.append("   Plus {} more...".format(Cardinal(FilesLeft)))
                break
 
        FileList = "\n"
        FileList += "\n\n".join(NameList)
        FileList += "\n"
 
        self.InfoBox(Parent=parent, Title="Files Chosen:", Text=FileList,
                     Font=self.NormalFont)
        return
 
 
    def reset_first_words(self):
        """Resets all variables related to the opening words in the paragraph
        """
        self.FirstWordsButtonName.set('No opening words are set: choose a group at random')
        self.FirstWordsDisp.set('=== COPY & PASTE YOUR OPENING WORDS HERE ===')
        self.FirstWordsString.set("")
        return
 
 
    def onStartButton1(self):
        """This is called when the user wants to save the pasted opening words
        """
        if (self.FirstWordsDisp.get()[:3] == '===')  or \
            (len(self.FirstWordsDisp.get()) == 0):
            self.reset_first_words()
        else:
            """Newline forces button text to 2 lines, which maintains the
            button shape when the text gets longer when the words are shown:
            """
            self.FirstWordsString.set(self.FirstWordsDisp.get())
            self.FirstWordsButtonName.set('Opening words will be: "{}"...'.
                                          format(self.FirstWordsDisp.get()))
 
        self.FirstWordsWin.destroy()
        return
 
 
    def onStartButton2(self):
        """Called when the user decides not to save the pasted opening words
        """
        self.reset_first_words()
        self.FirstWordsWin.destroy()
        return
 
 
    def GetFirstWords(self):
        """Opens Entry dialog box for user to paste their opening words into
        """
        self.FirstWordsWin = Toplevel(self)
        root.grab_release()
        self.FirstWordsWin.grab_set()
 
        # This should line up the sub-windows with the buttons that called them:
        geom_string = "+{}+{}".format(w-120, h+90)
        self.FirstWordsWin.geometry(geom_string)
 
        self.FirstWordsWin.title('Pick your opening words')
 
        Instruction = "\nType or copy & paste some opening words from one of your "
        Instruction += "chosen text files into the space below. The random "
        Instruction += "Markov text will begin with these words. "
        Instruction += "Don't worry about putting them in quotation marks:"
 
        # Wrap the above text into an 11cm wide paragraph:
        Label(self.FirstWordsWin, text=Instruction, font=self.NormalFont,
              wraplength="11c").pack(pady=5)
 
        FirstWordsEntry = Entry(self.FirstWordsWin, font=self.NormalFont,
                             textvariable=self.FirstWordsDisp,
                             width=80, justify='center')
        FirstWordsEntry.pack(pady=5)
        FirstWordsEntry.focus_set()  # make the Entry box the active widget
        FirstWordsEntry.select_range(0, END) # highlight all the text
 
        button_1_title = "START my Markov paragraph with the above words"
        Button(self.FirstWordsWin, text=button_1_title, font=self.NormalFont,
               padx=5, pady=5, command=self.onStartButton1).pack(pady=5)
 
        button_2_title = "Don't worry about the opening words. Start my Markov "
        button_2_title += "nonsense text with a randomly selected sequence of "
        button_2_title += "words from one of my text files."
 
        Button(self.FirstWordsWin, text=button_2_title, font=self.NormalFont,
               command=self.onStartButton2, **self.std_button_opts).pack(pady=5)
        return
 
 
    def ValidateInt(self, new_text):
        '''Checks every char UpdateNumberButton() gets is part of a valid int
 
        Ignores entered chars that would make the total number not an int. This
        is a general purpose input type-enforcing function that ignores unwanted
        input. To force inputs of type float or string, simply create new
        functions called ValidateFloat() or ValidateString() from this code and
        use float(new_text) and str(new_text) as the first line of the try
        statement block below:
        '''
        if not new_text: # the field is being cleared
            return True
 
        try:
            """You don't care about entered_number. The point is to see if
            there is an error when you try to convert the input to the kind
            of data you want:
            """
            entered_number = int(new_text)
            self.UpdateButton.config(state=NORMAL)
            return True
 
        except ValueError:
            return False
 
 
    def onUpdateNumberButton(self, parent, minimum, maximum, variable,
                             button_name, button_format):
        """Checks the value entered is correct. Updates variable and button name
 
        This function checks that the value entered is within the correct
        range, between minimum and maximum. If not, it ignores the input and
        gives a warning beep. The parent window's Update button remains
        disabled until the input is valid. Once it is, it first updates
        variable to NewNumEntry, then updates button_name using button_format,
        by evaluating the Python meaning of strings passed down to it, e.g.
 
            buttonname = 'self.FundButtonName'
            and
            ButtonFormat = '.set("${:,}".format(NewValue))'
 
        which, when unpacked and executed consecutively by eval(), create a
        Python command which is then executed. This is a nice way to pass
        down a Tk StringVar variable and to modify both the variable and any
        widget that shows its value, once the 'Update' button has been
        pressed in the child window.
 
        Note 1: this is the right place to update the variable(s). To put the
        set() command in the parent function would only capture the initial
        value that the variable was set to when the parent window was first
        called into existence and drawn.
 
        Note 2: don't put any newlines into the button_format string. The
        newlines confuse the eval() function.
        """
        NewValue = int(self.NewNumEntry.get())
 
        if ((maximum is not False) and (minimum <= NewValue <= maximum)) or \
            ((maximum is False) and (minimum <= NewValue)):
 
            eval(variable + '.set({})'.format(NewValue))
            eval(button_name + button_format)
 
            self.NewNumberEntryWin.grab_release()
            eval(parent + '.grab_set()')
            self.NewNumberEntryWin.destroy()
            return
 
        else:
            self.NewNumEntry.bell()
            self.UpdateButton.config(state=DISABLED)
            self.NewNumEntry.delete(0, END)
            return
 
 
    def UpdateNumberButton(self, Parent='root', Variable='self.DollarAmount',
                    ButtonName='self.NoButtonName', Font=('Helvetica', 11),
                    ButtonFormat='.set("${:,.0f}".format(NewValue))',
                    Title='Unknown Update',
                    Instruction='Check your code: window needs an instruction',
                    Minimum=0, Maximum=1, Width=9,
                    Advice='   Figure should be between ${:0,.0f} and ${:0,.0f}.   ',
                    Currency='          $', Suffix=''):
        """Opens a child Entry window to ask for the new number
 
        This function uses the grid() geometry, which is OK as it is the only
        geometry used in the new window self.NumberInputWindow. By using the
        row=r, column=c system, the position of the widgets can easily be
        interchanged if you are designing a larget dashboard. This useful
        little window can be used to enter and check integers and floats,
        allowing the assignment of currency symbols and units and after the
        entry window.
 
        The Currency prefix and the Suffix can be set at the calling function
        to define what the number means. The function defaults to a currency
        update. The suffix can be set to units, or percentage.
 
        There's no reason for using kwargs in the function call other than to
        make the code infinitely more readable. The normal reasons for using
        them - setting defaults, using optional parameters in function
        calls - do not apply here. Had ButtonName and ButtonFormat simply been
        passed as strings in the function call, six months from now even I
        would have trouble working out why, and what those strings did.
        Alternatively, if positional variable names had been assigned and used,
        the variables would still have had to be assigned in 5-6 lines of code
        before the lambda was used, looking much like the list above.
        And making the parent code very cluttered.
        """
        self.NewNumberEntryWin = Toplevel(self)
        eval(Parent + '.grab_release()')
        self.NewNumberEntryWin.grab_set()
 
        geom_string = "+{}+{}".format(w-25, h+300)
        self.NewNumberEntryWin.geometry(geom_string)
 
        self.NewNumberEntryWin.title(Title)
 
        r=0; c=0
        self.NewCashInstruction = Label(self.NewNumberEntryWin, text=Instruction, font=Font)
        self.NewCashInstruction.grid(row=r, column=c, columnspan=3, padx=10)
 
        r+=1; c=0
        Label(self.NewNumberEntryWin, text=Currency, justify=RIGHT, font=Font).grid(
                                row=r, column=c, sticky=E)
 
        c+=1
        vcmd = self.NewNumberEntryWin.register(self.ValidateInt)
        self.NewNumEntry = Entry(self.NewNumberEntryWin, validate="key",
                                justify=CENTER, validatecommand=(vcmd, '%P'),
                                width=Width, font=Font)
        self.NewNumEntry.grid(row=r, column=c, pady=5)
        self.NewNumEntry.focus_set()
 
        c+=1
        Label(self.NewNumberEntryWin, text=Suffix, justify=LEFT, font=Font).grid(row=r,
                                column=c, sticky=W)
 
        c+=1
        self.UpdateButton = Button(self.NewNumberEntryWin, text='Update', font=Font,
                                justify=LEFT, state=DISABLED, width=6,
                                command=lambda:
                                    self.onUpdateNumberButton(Parent, Minimum,
                                    Maximum, Variable, ButtonName, ButtonFormat))
        self.UpdateButton.grid(row=r, column=c, padx=5, pady=5)
 
        r+=1; c=0
        if not Maximum:
            self.NewNumAdvice = Label(self.NewNumberEntryWin, text=Advice.format(
                                Minimum), font=Font)
        else:
            self.NewNumAdvice = Label(self.NewNumberEntryWin, text=Advice.format(
                                Minimum, Maximum), font=Font)
        self.NewNumAdvice.grid(row=r, column=c, pady=5, columnspan=4)
        return
 
 
    def GetFileList(self):
        """Returns a list of path names for your own code to open elsewhere
 
        This is different to GetNameOfTextToAnalyse() used in the previous
        post. Instead, this function returns multiple filenames by calling
        the tk file handler askopenfilenames(), rather than the singular
        askopenfilename(). It assigns a list of full file paths to
        self.path_list[]
        """
        if self.path_list != []:
            # a set of files have been chosen before. Go to the same place:
            self.file_opt['initialdir'], an_old_text_name = os.path.split(self.path_list[0])
        else:
            old_path_list = self.path_list
            self.file_opt['initialdir'] = '.'
            """ This is where you would define a separate default folder for
            your input text files, should you decide to keep input, config and
            output files apart. Make sure the folder exists before you run the
            code:
            #self.file_opt['initialdir'] = '../Input_Files'
            """
        old_path_list = self.path_list
 
        # Detects whether user's computer is Mac or not:
        Key = 'CTRL'if platform.mac_ver()[0] == '' else 'Command'
 
        # Define what the user will see in the open file window.
        self.file_opt['title'] = 'Use SHIFT-click and {}-click to pick multiple text files:'.format(Key)
 
        self.file_opt['initialfile'] = '*.txt'
 
        # returns a tuple of file paths, or the empty tuple ():
        self.path_list = list(tkinter.filedialog.askopenfilenames(**self.file_opt))
 
        if self.path_list != []:
            # User picked some files, and didn't hit cancel:
 
            path_list_copy = self.path_list.copy()
            for index, path in enumerate(path_list_copy):
                if "*.txt" in path:
                    del self.path_list[index]  # fixes a Tk implementation bug in Linu
                    break
 
            num_files_chosen = len(self.path_list)
            verb = 'Add' if num_files_chosen == 1 else 'Change'
            plural = 's' if num_files_chosen > 1 else ''
            self.fileSelector.set('{} files'.format(verb))
            self.reset_first_words()
            number = Cardinal(num_files_chosen)
            self.FileCountButton.set('{} file{} selected'.format(number.capitalize(), plural))
 
        else:
            # Reset pathlist to last valid list:
            self.path_list = old_path_list
            # button names and opening words should be unchanged
 
        if self.path_list != []:
            # activate the next button down to allow the user to see the files selected:
            self.ListFilesButton.config(state=NORMAL)
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
            code:
            #self.file_opt['initialdir'] = '../Output Files'
            """
        OldSaveFilePath = self.save_path_and_name
 
        # Define what the user will see in the save file window:
        self.file_opt['title'] = "Save results to:"
        self.file_opt['initialfile'] = 'Markov_Result.txt'
 
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
 
 
    def run_my_code(self):
        """A simple wrapper to pass your dashboard-set variables to your logic
        """
        result = ''
        FirstWords = self.FirstWordsString.get()
 
        """Place any error checking here for the variables set by your dashboard,
        before you send them to your logic. You have to process the errors
        in windows, and allow the program to continue execution:
        """
        if self.path_list == []:
            tkinter.messagebox.showinfo(title='No text files chosen   ',
                message="Please choose some texts to\nturn into meaningless gibberish.", icon='error')
 
        elif FirstWords != '' and (len(FirstWords.split()) != self.MarkovOrder.get()):
            tkinter.messagebox.showinfo(title='Markov Error   ',
                message="The number of opening words\nmust equal the Markov order.",
                icon='error')
 
        else:
            """You don't explicitly have to set and pass EVERY one of your
            variables to your logic. If some are not named, they will assume
            the defaults you have given them in your function's kwarg
            declarations. Others can be hard preset here by name, rather than
            cluttering up the GUI with options that will probably never change,
            or that the user doesn't need to see:
            """
            result, error  = create_markov_text_from(self.path_list,
                                    markov_order=self.MarkovOrder.get(),
                                    word_len=self.ParaLength.get(),
                                    starting_words=self.FirstWordsString.get())
            if error != 'OK':
                self.InfoBox(Parent='root', Title="Error", Text=error, Font=self.NormalFont)
                return
            else:
                self.save_as_file(result)
        return
 
 
 
 
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
    PythonGUI_2(root).pack()
 
    root.mainloop()

