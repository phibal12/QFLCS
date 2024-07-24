##########################
#---UNDER CONSTRUCTION
#--- SAFE MODE QFLCC AND 
#--- QDF GAME GUI
##########################
import importlib

# The following starts the QAI-game-gui.py 
qflcaX = importlib.import_module("QAI-LCode_QFLCC")
#qflcaX. .... call for specific function 
# To exit and jump into the GUI program press 'nn' or disable the previous line by comment. 
# The imported program assures running up to the game. The game interface cannot be run properly
# from the qflcaX, unless properly called like the user help code for example. Need to check frequently until the stable 
# version is released. 
# Accessing the variable dynamically, like e.g. global variables
print(qflcaX.pngfile) 

# Importing required library
import math, csv
import numpy as np
import pandas as pd
import sys # This module provides signal interruption services, or access to the variables 
           # and functions that interact strongly with the interpreter.
import keyboard # For a specific command or key stroke as an interrupt signal coming from the keyboard by user.
import winsound # For system sound representing a state of event or algorithm step. 
#from playsound import playsound.

import colorama
import time   # To delay at certain checkpoints for viewing I/O data or calculation results
from time import sleep
import datetime  # For recording r/w file time entry 
import threading
from pathlib import Path  # For accessing and conduct operations on files/directories 
import os

import subprocess # To record I/O terminal events
from joblib import Parallel
import multiprocessing
import threading
from multiprocessing.pool import ThreadPool
from random import random
from threading import Thread
import concurrent.futures, shutil # For copying I/O data files from other directories concurrently 
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back  # To print certain text in standard color for highlighting 
                                 # quantum points vs. classical points about the measurement dataset
from colored import fg, bg

import click
@click.group()
def cli():
    """Main entry point."""

@cli.command()
@click.option("-d", "--debug", help="Include debug output.")
def build(debug):
    """- Build production assets."""

#-------------------------------------------------------------------------------------------------
# Colored foreground (fg) and background (bg) Classes for sectioning and highlighting the code 
# according to a specific QF-LCC algorithm step, checkpoint, computer operation, error, or HALT. 
#-------------------------------------------------------------------------------------------------
class fg:
        black='\033[30m'
        silver="\033[0;38;5;7m"
        red='\033[31m'
        green='\033[32m'
        orange='\033[40m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
      
        """- Colored foreground (fg) class for sectioning and highlighting the 
        QF-LCC algorithm step, checkpoint, computer operation, error, or HALT."""

class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

        """- Colored background (bg) class for sectioning and highlighting the 
        QF-LCC algorithm step, checkpoint, computer operation, error, or HALT."""

####################---Previous lines test the QFLCC python program---#################
### Following lines are the actual GUI being constructed for the QDF game #
import time   # To delay at certain checkpoints for viewing I/O data or calculation results
from time import sleep

from tkinter import *
import tkinter as tk
from itertools import cycle
import pygame  # To play music or sounds in the QDF game.

from tkinter import ttk
import asyncio 

root = Tk()

#################################################################################
# Alice & Bob's Quantum Doubles game starts from here to validate data results...
#################################################################################
__game_version__ = "ver.1.0"

__game_logo__="""
\033[92m  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
\033[92m ( o.o )( o.o )( o.o )( o.o )( x.x )( o.o )( o.o )( o.o )( o.o )( o.o )( x.- )( o.o )( o.o )( o.o )( -.- )
\033[92m  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
\033[92m  /\_/\  \033[96m    ___ __                   ___     ____         ___                                   \033[92m   /\_/\ 
\033[92m ( o.o ) \033[96m   / _ \\ \                 /   \   |  _ \       / _ \ //                               \033[92m   ( o.o )
\033[92m  > ^ <  \033[96m  | |_| |\ \  ___   _____   \ O /   | |_) ) ___ | |_) )/____                            \033[92m   > ^ < 
\033[92m  /\_/\  \033[96m  |  _  | > \| \ \ / / __)  / _ \/\ |  _ ( / _ \|  _ < /  ._)                           \033[92m   /\_/\ 
\033[92m ( x.o ) \033[96m  | | | |/ ^ \ |\ v /> _)  ( (_>  < | |_) | (_) ) |_) | () )                            \033[92m  ( x.x )
\033[92m  > ^ <  \033[96m  |_| |_/_/ \_\_)> < \___)  \___/\/ |____/ \___/|  __/ \__/                             \033[92m   > ^ < 
\033[92m  /\_/\  \033[96m    ____        / ^ \                           | |                _____                \033[92m   /\_/\ 
\033[92m ( o.x ) \033[96m   / __ \      /_/ \_\                          |/\               / _ \ \               \033[92m  ( o.o )
\033[92m  > ^ <  \033[96m  | |__| |_   _  __  ___  _____ _   _ _   _     /  \   ___  _   _| |_) ) \   ___ ____   \033[92m   > ^ < 
\033[92m  /\_/\  \033[96m  |  __  | | | |/  \/ / |/ (   ) | | | | | |   / /\ \ / _ \| | | |  _ < > \ / __)  ._)  \033[92m   /\_/\ 
\033[92m ( o.o ) \033[96m  | |__| | |_| ( ()  <| / / | || |_| | |_| |  / /__\ ( (_) ) |_| | |_) ) ^ \> _| () )   \033[92m  ( -.x )
\033[92m  > ^ <  \033[96m   \____/ \___/ \__/\_\__/   \_)\___/| ._,_| /________\___/ \___/|  __/_/ \_\___)__/    \033[92m   > ^ < 
\033[92m  /\_/\  \033[96m                                     | |                         | |                    \033[92m   /\_/\ 
\033[92m ( -.- ) \033[96m                                     |_|                         |_|                    \033[92m  ( o.o )
\033[92m  > ^ <  \033[96m  \033[91m v.1.0                                                                                \033[92m   > ^ < 
\033[92m  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
\033[92m ( o.x )( o.o )( o.o )( o.o )( -.- )( o.o )( o.o )( x.x )( o.o )( o.o )( o.o )( -.x )( o.o )( x.- )( o.o )
\033[92m  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
"""
###############################################################################
# Instantiating variables and constants of animated states of loser, winner, 
# dual(superposition), unknown. Alternatively, lists can be created in the 
# future tests after threads, timer or sleep() and subprocess runs for combined 
# datasets. For example, the constants excited1 and excited2 can be redefined 
# in a list as excited = [excited1, excited2], or by the removal of the two 
# constants hardcoding the emojis in excited = ["─=≡Σ((( つ◕ل͜◕)つ", 
# "─=≡Σ(((✌(✰ ͜ʖ ✰)✌ [✰]"] and later called for the participant's win, as 
# animated by the function winner_show() within its for-loop. 
###############################################################################
prize="[✰]"
alice="[♠]"
bob="[○]"
eve="[♣]"
audience="[♦]"
crownBob="♕💪🤴👍♕"
crownAlice="♔👸♔"
here="👇"
go="👉"

excited1 = "─=≡Σ((( つ◕ل͜◕)つ"
excited2 = "─=≡Σ(((✌(✰ ͜ʖ ✰)✌ [✰]"

grounded1= "─=≡Σ(((┏(° ʖ̯ ͡°)┛"
grounded2= "─=≡Σ(((┗(° ʖ̯ ͡°)┛"
grounded3= "─=≡Σ(((┏(╥ ʖ̯ ╥)┓"

dual3="─=≡Σ((👎 (11 ͜ʖ͠ 00)👍"
dual1="─=≡Σ((🖐 (10 ͜ʖ͠ 01)👍"
dual2="─=≡Σ((☝ (01 ͜ʖ͠ 10)🖐"

guesser1="─=≡Σ(((💪(◐ ͜ʖ͠◐ )👉"
guesser2="─=≡Σ(((☝(◐ ͜ʖ͠◐ )👍"
guesser3="─=≡Σ(((👉(❂ ͜ʖ͠❂ )👉[$̲̅ |"

classical1="─=≡Σ((🖐(° ͜ʖ ͡°)🖐"
classical2="─=≡Σ((👍(° ͜ʖ ͡°)👍"
classical3="─=≡Σ(((👉(❂ ͜ʖ͠❂ )👉[$̲̅ |"

errorP1=" ¯\_( ͠◐ ͜ʖ͠◐ )_/¯"
errorP2=" ¯\_( ͠◕ ͜ʖ͠◕ )_/¯"

aimTarget=" ||[̲̅$̲̅( ͡๑ ͜ʖ ͡๑)̲̅$̲̅]||"
helperTarget1=" |[✰]( ͡° ͜ʖ ͡°)[○]|"
helperTarget2=" |[♠]( ͡° ͜ʖ ͡°)[✰]|"

#-------------------------------------------------------------------------------------------------
# Code Use and Copyright Information
#-------------------------------------------------------------------------------------------------
__ORCID__ = "ORCID: https://orcid.org/0000-0003-1037-018X"
__copyright__ = "Copyright © 2022--2024"
__license__ = "Creative Commons (CC BY-NC-ND)"
__author__ = "Philip B. Alipour"
__location__ = "@ ECE Dept. University of Victoria, Victoria BC, Canada"
__version__ = "ver. 1.0"
__description__ = "This QFLCC version of the QAI-LCode is basic. More revisions to come, as the \
dataset grows on the number of trials on 1 or more QDF circuits occurs relative to improvements \
of dataset representation of quantum and classical parameters in observing a thermodynamic system \
based on Refs. [1-3,5] of the Data in Brief, Elsevier J article."
print(Back.BLUE + fg.lightgreen + __description__, "\n") 
print(Back.RESET+"Copyright information in Python code:\n") 
print("\033[0m"+__license__ , __author__, __location__+',', fg.blue+"\x1B[4m"+__ORCID__+"\x1B[0m", 
      __copyright__, __version__, fg.pink+bg.lightgrey)
sleep(5)
############################################################################################
# These are the QDF game description, logo and copyright details.
############################################################################################
__game_banner__ = """\n"\033[96m( ͡° ͜ʖ ͡°) vs ( ͡°( ͡° ͜ʖ ͡°(︡▧ ͜ʖ▧︠) ͡° ͜ʖ ͡°) ͡°) vs [̲̅$̲̅( ͡๑ ͜ʖ ͡๑)̲̅$̲̅]  vs ¯\_( ͠◐ ͜ʖ͠◐ )_/¯ vs \
─=≡Σ((( つ◕ل͜◕)つ [♥]]] [♦]]] [♣]]] [♠]]] ─=≡Σ(((✌(✰ ͜ʖ ✰)✌ ||||||||||||||||||||||| \033[92m"""
__game_description__= "Alice & Bob's Quantum Doubles... This QFLCC game version of the QAI-LCode is basic. \
More revisions to come, as the dataset grows on the number of trials on 1 or more QDF circuits for simulating. \
the QDF game. The QDF game simulates events of the dataset's quantum and classical parameters in observing a \
thermodynamic system = { QDF game environment and its participants Alice, Bob, Eve, Audience } based on Refs. [1-2,4] \
of the Data in Brief, Elsevier J article."
print(Back.RESET+fg.lightgreen,__game_logo__,__game_banner__ + __game_description__ , 
      Back.RESET+fg.silver+__game_version__,"\n"), sleep(2) 
"""- Colored banner to introduce the QDF game and its goal. These common constants and variables are
     frequently used during game play."""
entry_stage=0

"""def entry_add(): 
###########################################################################################
# This function logs program events onto the stdout file
############################################################################################
     global entry_stage  # redefine the entry count as global  
     entry_stage+=1
     idxplus = len(res)+entry_stage
     subprocess.run("echo {}- Checkpoint logged on {} for {}".format(idxplus, now.strftime("%Y-%m-%d %H:%M:%S"), 
                                                                     __game_banner__, __game_description__ ), 
                                                                     shell=True, stdout=file_)

entry_add()"""

def qdf_game_gui():
    ##################################################################
    # Initialize pygame, then sound mixer to play introductory retro 
    # music and welcome message sound files and create other windows 
    # as a GUI.
    ###################################################################
 def flash_color(object, color):
        object.config(foreground = next(color), bg='black')
        root.after(100, flash_color, object, color)
        """ Coloring the flash object from pygame for the user's interface (UI)."""

##################################################################
# Initialize pygame, then sound mixer to play introductory retro 
# music and welcome message sound files and create other windows 
# as a GUI.
###################################################################
from tkinter import *
import tkinter as tk
from itertools import cycle
import pygame  # To play music or sounds in the QDF game.

def flash_color(object, color):
    object.config(foreground = next(color), bg='black')
    root.after(100, flash_color, object, color)
""" Coloring the flash object from pygame for the user's interface (UI)."""

pygame.init() 
pygame.mixer.init()

game_sound = pygame.mixer.Sound('__snd__/game_music2.wav')
game_sound.play(), sleep(2)

game_sound = pygame.mixer.Sound('__snd__/welcome2.wav')
game_sound.play()

""" Initialize pygame and sound mixer to play introductory retro 
music and welcome message sound files and other windows as a GUI."""

from PIL import Image, ImageTk
import tkinter.messagebox as msgbox 

def display_bye_msg():
    # Play Windows exit sound.
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    root.wm_attributes("-topmost", 1)
    root.withdraw() # Hide this form.
    bye = msgbox.askquestion(title=f"Alice & Bob's Quantum Doubles {__game_version__} Message", 
                             message='Are you sure you want to exit? If Yes, ...🖐 (° ͜ʖ ͡°)🖐 Bye!', 
                             icon='warning', parent=root)
    if bye == 'yes':
        game_sound = pygame.mixer.Sound('__snd__/goodbye1.wav')
        game_sound.play()
        Quit()
    else:
        root.wm_attributes("-topmost", 1)
        root.deiconify() # Unhide this form. 
    """Exit game if user chooses after the bye message."""

def flagClose():    
    root.withdraw() # Hide this form.
    root.quit() 
    #---------------------------------------------------------------------------------
    # Enable the next lines to destroy this form after quit (or by duration afterwards 
    # using sleep) as a permanent close solution. This is to not revisit the dataset(s) 
    # load & play root form, as it is already destroyed after t seconds!
    #---------------------------------------------------------------------------------
    #sleep(50)       # Dont close for t = 50 seconds, for example...
    #root.destroy()  # To destroy the root form. 
    """Quit or destroy the game app form and get back to CLI as user's interface. The quit
command gives user the illusion that the form is closed/gone, which in fact can be later 
called upon by the option 'form' from the terminal. """

def Quit():
     game_sound = pygame.mixer.Sound('__snd__/goodbye1.wav')
     game_sound.play()
     print(fg.black + Back.YELLOW +'\nExiting program...🖐 (° ͜ʖ ͡°)🖐  Bye!'+ Back.RESET), sleep(3)
     print(fg.yellow + Back.RED+"The QFLCC program is terminated!" + Back.RESET)
     sys.exit(1) # Force this in case of abnormal exit or program termination. 
"""Exit program and system with a message before the terminal."""

def Help():
     msgbox.showinfo(title='Input Tips', message='Input tips:\n \n-Enter \'n\' key or \'next\' for \
the next message or input. \n-Enter \'h\' or \'help\' to display these tips. \n-Enter the number \
for a game player role when prompted. \n-Enter a value between 0 and 1, or 0 or 1 for a P \
value. \n-Enter \'s\' or \'speed\' to change the speed of game steps. \n-Enter \'v\' or \'volume\' for \
sound volume change during play. \n-Enter \'cv\' for sound volume change within CLI. \n-Enter \'f\' or \
\'form\' to reload this form. \n-Enter \'e\' or \'exit\' to exit the game.')
"""Helping tips to start the game by choosing participants and a P value, according to the QDF game model."""

def open_new_win():
   ##############################################################################
   # This function creates a new window based on the QDF game legend and rules. #
   ##############################################################################
   imagelist1 = ["game_legend.png"]
   photo = PhotoImage(file=imagelist1)
   width = photo.width()
   height = photo.height()
   fore_win=Toplevel(root)
   fore_win.wm_attributes("-topmost", 1) # these two lines will focus on the window not terminal 
   fore_win.focus_force()
   fore_win.title("Game Model Legend")
   fore_win.geometry("650x450")
   fore_win.configure(background='black')
   image = Image.open('game_legend.png').convert("RGB")
   resized = image.resize((550, 300),Image.LANCZOS) # Resize the image and antialias it from the uploaded file.
   display = ImageTk.PhotoImage(resized)
   
   # Display it within a label.
   label = Label(fore_win, image=display, background="black")
   legend_label = Label(fore_win, 
                        text=excited1+f' | Score = 10 points for {bob} or {alice} win {prize} via {eve} or {audience} \n'
                        + dual1+f' | Score = 3 points for {bob} via {eve}, or {alice}, \
superpose/entangle with {prize} between boxes \n'+ guesser3+f' Score = 2 points for {bob} or {alice} guess the {prize} \n'
                        +  grounded2+f' | Score = -5 points from {bob} or {alice} losing a/the {prize} \n'+ grounded3
                        +f' | Lose score < -9 points for {bob} or {alice} is game over \n'+ helperTarget1 
                        + f' | Score = 1 point for {bob} or {alice} guess the {prize}.  \n'+ crownBob+' | '+ crownAlice 
                        +f' | Score > 999 points for {bob} or {alice} is the final game win = level 8 complete.  \n' 
                        + alice + bob + eve + audience + prize +go 
                        +f' | Possible combination of doubles from selected dataset \
is = {qdf} vs its complement {bitpair}.  \n', justify="left" , bg="black",  fg="lightgreen").pack()  # important variable to recall/import from the qflcc file
   label.image = display
   label.pack()

   # Set minimum the foreground window size value
   fore_win.minsize(650, 450)
   
   # Set maximum the foreground window size value
   fore_win.maxsize(650, 450)

win_min=0
def restart_QFLCC():
########################################################
# The following restarts QFLCC for choosing a dataset  #
########################################################
   global win_min
   #root.iconify()
   win_min == True
   flagClose() # An option to choose between destroying/quit the present form. 
   subprocess.run(["python", "QAI-LCode_QFLCC.py"])

##########################################################
# Mimic an animated GIF displaying a series of GIFs an 
# animated GIF was used to create the series of GIFs with 
# a common GIF animator utility.
# Buttons and usage help options are appended and displayed 
# at the end of log file and other game file 
# installation/download.
##########################################################
from tkinter import ttk
import asyncio 

root = Tk()

# Adjust size...
#root.geometry("1550x600")
width = 1550 # Width 
height = 600 # Height 
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry('+%d+%d' % (x, y))
root.wm_attributes("-topmost", 1) # These two lines will focus on the window not terminal. 
root.focus_force()

def disable_event():
    pass
root.protocol("WM_DELETE_WINDOW", disable_event)  # This disables the [X] button on the root window to satisfy user's game options.
       # No matter how many times the user clicks on [X], nothing happens, and so is directed to other exit or resume game options. 

# Create a sprite bank (array list) to animate from files.
imagelist = ["__img__/logo_01.gif", "__img__/logo_01.gif", "__img__/logo_02.gif", "__img__/logo_02.gif", 
             "__img__/logo_02.gif", "__img__/logo_03.gif",  "__img__/logo_03.gif", "__img__/logo_04.gif", 
             "__img__/logo_05.gif", "__img__/logo_06.gif", "__img__/logo_06.gif", "__img__/logo_06.gif"]

# Create a sprite bank (array list) from the defined ASCII characters by their corresponding char variables. 
charslist = [f'{crownBob} | {dual1}' , f'{crownBob} | {dual1}', f'{crownBob} | {dual2}', 
             f'{crownBob} | {dual2}', f'{crownBob} | {dual3}', f'{crownBob} | {dual3},' f'{crownBob} | {excited1}', 
             f'{crownBob} | {excited1}', f'{crownBob} | {excited1}', f'{crownBob} | {excited2}', 
             f'{crownBob} | {excited2}', f'{crownBob} | {excited2}', f'{crownAlice} | {guesser1}', 
             f'{crownAlice} | {guesser1}', f'{crownAlice} | {guesser2}', f'{crownAlice} | {guesser2}', 
             f'{crownAlice} | {guesser3}', f'{crownAlice} | {guesser3}', f'{crownAlice} | {classical1}', 
             f'{crownAlice} | {classical1}', f'{crownAlice} | {classical2}', f'{crownAlice} | {classical3}', 
             f'{crownAlice} | {classical3}'] 
color_list = ["cyan", "yellow", "red", "yellow", "blue", "lightgreen"]

progressbar = ttk.Progressbar(length=750, style="green.Horizontal.TProgressbar")

# Full progress bar...
progressbar.step(99.9)
progressbar.place(x=950,y=550, width=560)

# Set minimum window size value.
root.minsize(1550, 600)
 
# Set maximum window size value.
root.maxsize(1550, 600)

# Extract width and height info.
photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()

canvas = Canvas(width=width, height=height)

# Position the canvas for the gif image.
canvas.place(x=30, y=20)

root.title(f"Alice & Bob's Quantum Doubles {__game_version__}")
root.configure(background='black')

filename='shell_output.txt'

def update_text():
   # Configuring the text in Label widget.
   my_label0.configure(text="Loading the game model and circuit. Click START to continue...")
   subprocess.call(['game_model.png'], shell=True)
   subprocess.call([f'{pngfile}.png'], shell=True) # to import from the qflcc python file

def change_color():
   my_label0.config(bg= "gray51", fg= "red")

f = open("shell_output.txt", "r")
file_string = f.read()

my_label0 = tk.Label(root, text =  __license__ + __author__+ __location__+','
                     +__ORCID__+ __copyright__+ __version__
                     +"\n \n||||||||||||||||||||||||||||||||||||||||||||||||||\
|||||||||||||||--Reload Log_file--||||||||||||||||||||||||||||||||||||||||||||\
|||||||||||||||||||||||||||||\n \n"+str(file_string), fg="#000fff000", background="black", 
width=80, height =28, wraplength=525, anchor='n', justify="left")
my_label0.place(x=950, y=15)

# Create a list of image objects. 
giflist = [] # This is to store and run image sprite in .gif.
for imagefile in imagelist:
   photo = PhotoImage(file=imagefile)
   giflist.append(photo)

anim_label1 = tk.Label(root, text = '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .', 
                       fg="lightgreen" , background="black", width=80, height =2, wraplength=500, 
                       anchor="w", justify="left")
anim_label1.place(x= 950, y= 500)
anim_label0 = tk.Label(root, text = dual1, fg="cyan" , background="black", width=80, height=2, 
                       wraplength=500, anchor="w", justify="left")
anim_label0.place(x= 950, y= 500)

async def mainT():
  await asyncio.sleep(0.001)  # Sprite is updated every second and then other asynchronous updating tasks 
                              # take place in the outer loops. 

# Loop through the gif image objects for a while.
for j in range(0, 30):
    for gif in giflist:
        canvas.delete(ALL)
        canvas.create_image(width/2.0, height/2.0, image=gif)
        canvas.update()
        progressbar.step(j*5)
        anim_label0.place(x= 950+j*4, y= 500)
        #sleep(0.001) 
    for clr in color_list:
     for sprite in charslist:
          anim_label0.config(text=sprite+' . . . . . Loading . . .')
          anim_label0.update()
          #asyncio.run(mainT()) # Sprite is updated every second and then other asynchronous updating tasks 
                                # take place in the outer loops. 
          #asyncio.sleep(0.5)  # Sprite is updated every second and then other asynchronous updating tasks 
                               # take place in the outer loops. 
     anim_label0.config(fg=clr)
     anim_label0.update()
     sleep(0.02)

pygame.time.delay(2)

button0 = Button(root, text = 'START', bg='black', fg='white', command = flagClose)
button1 = Button(root, text = 'Input Tips', bg='black', fg='white', command = Help)
button3 = Button(root, text="QUIT", bg='black', fg='white', command = display_bye_msg)
button2 = Button(root, text="Show Game Model", bg='black', fg='white', command = open_new_win)
button4 = Button(root, text=f'Change Dataset: {qdf} vs Complement {bitpair}', bg='black', fg='white', 
                 justify=LEFT, wraplength=160, command = restart_QFLCC) #important variables to import from the QFLCC py file

button0.place(x=950, y=450, width=50)
button1.place(x=1010, y=450, width=80)
button2.place(x=1100, y=450, width=140)
button3.place(x=1250, y=450, width=80)
button4.place(x=1340, y=450, width=180)

for k in range(0, 1):
 for clr in color_list:
     for sprite in charslist:
          anim_label0.config(text='Configuring Logic Conditions for the chosen Circuit and Dataset...\n'+sprite, 
                             wraplength=400)
          anim_label0.update()
          #asyncio.run(mainT())
          anim_label0.place(x= 950-j/2+100, y= 500)
          sleep(0.1)  # Sprite is updated every second and then other asynchronous updating tasks take place in the outer loops. 
     anim_label0.config(fg=clr)
     anim_label0.update()

anim_label0.config(text=sprite+'\n QFLCC Game Circuit Configuration Complete. Click START to Continue...', 
                   wraplength=400)
anim_label0.update()

root.mainloop() # Run the Tkinter main loop.