import tkinter
import customtkinter
from inpaint_screen import InpaintScreen
from edit_screen import EditScreen
from home_screen import HomeScreen

class ScreenHandler:
	def __init__(self):
		# configure the window
		self.root = customtkinter.CTk()
		self.root.geometry(f"{1280}x{720}")
		self.root.title("Home Screen")
		self.root.resizable(0, 0)

		# initialze starting variables
		self.inpaint_screen = None
		self.edit_screen = None
		self.home_screen = None
		self.current_screen = None
		
		# calls method that will create the initial screen (home sceen)
		self.create_home_screen()

	def create_home_screen(self):
		self.home_screen = HomeScreen(self.root, self)
		self.current_screen = "home"

	def to_home_screen(self):
		if self.current_screen == "edit":
			self.edit_screen.main_frame.destroy()
		if self.current_screen == "inpaint":
			self.inpaint_screen.main_frame.destroy()
		if self.current_screen == "home":
			return
		self.home_screen = HomeScreen(self.root, self)
		self.current_screen = "home"	

	def to_inpaint_screen(self):
		if self.current_screen == "edit":
			self.edit_screen.main_frame.destroy()
		if self.current_screen == "inpaint":
			return
		if self.current_screen == "home":
			self.home_screen.main_frame.destroy()
		self.inpaint_screen = InpaintScreen(self.root, self)
		self.current_screen = "inpaint"

	def to_edit_screen(self):
		if self.current_screen == "edit":
			return
		if self.current_screen == "inpaint":
			self.inpaint_screen.main_frame.destroy()
		if self.current_screen == "home":
			self.home_screen.main_frame.destroy()
		self.edit_screen = EditScreen(self.root, self)
		self.current_screen = "edit"
