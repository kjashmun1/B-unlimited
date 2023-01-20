import tkinter
import customtkinter

class HomeScreen:
	def __init__(self, parent, screen_handler):
		super ().__init__()
		# create the main frame for the home screen and the required navigation buttons
		self.main_frame = customtkinter.CTkFrame(master=parent, width=1280, height=720)
		self.main_frame.pack(padx=8, pady=8)

		self.inpaint_screen_button = customtkinter.CTkButton(master=self.main_frame, height=100, width=400, text="Go to Inpaint Screen", border_width=2, command=lambda: self.to_inpaint_screen(screen_handler))
		self.inpaint_screen_button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

		self.edit_screen_button = customtkinter.CTkButton(master=self.main_frame, height=100, width=400, text="Go to Edit Screen", border_width=2, command=lambda: self.to_edit_screen(screen_handler))
		self.edit_screen_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

		self.exit_program_button = customtkinter.CTkButton(master=self.main_frame, height=100, width=400, text="Exit Program", border_width=2, command=self.exit_program)
		self.exit_program_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

	def to_inpaint_screen(self, screen_handler):
		print("Going to inpaint screen")
		screen_handler.to_inpaint_screen()

	def to_edit_screen(self, screen_handler):
		print("Going to edit screen")
		screen_handler.to_edit_screen()

	def exit_program(self):
		print("Exiting the program")
		exit()
