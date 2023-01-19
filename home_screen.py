import tkinter
import customtkinter

class HomeScreen:
	def __init__(self, parent):
		super ().__init__()
		# create the main frame for the home screen and the required navigation buttons
		self.main_frame = customtkinter.CTkFrame(master=parent, width=1280, height=720).pack(padx=8, pady=8, fill="both", expand=True)

		self.inpaint_screen_button = customtkinter.CTkButton(master=self.main_frame, height=100, width=400, text="Go to Inpaint Screen", border_width=2, command=self.to_inpaint_screen).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

		self.edit_screen_button = customtkinter.CTkButton(master=self.main_frame, height=100, width=400, text="Go to Edit Screen", border_width=2, command=self.to_edit_screen).place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

		self.exit_program_button = customtkinter.CTkButton(master=self.main_frame, height=100, width=400, text="Exit Program", border_width=2, command=self.exit_program).place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

	def to_inpaint_screen(self):
		print("Going to inpaint screen")

	def to_edit_screen(self):
		print("Going to edit screen")

	def exit_program(self):
		print("Exiting the program")
