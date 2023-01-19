import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
	def __init__(self):
		super ().__init__()

		# configue the window
		self.geometry(f"{1280}x{720}")
		self.title("Image Editing Screen")
		self.resizable(0, 0)

		# configure frame on right side for edit buttons
		self.edit_frame = customtkinter.CTkFrame(master=self, width=240, height=704)
		self.edit_frame.pack(padx=8, pady=8, side="right", fill="both", expand=True)

		# configure frame on left side for displaying/handling image
		self.image_frame = customtkinter.CTkFrame(master=self, width=960, height=704)
		self.image_frame.pack(padx=8, pady=8, side="left", fill ="both", expand=True)
	
	def create_buttons(self):
		# configure edit buttons that will be in the edit button frame
		self.colorselect_optionmenu = customtkinter.CTkOptionMenu(master=self.edit_frame, height=50, width=200, values=["Default", "other"], anchor=tkinter.CENTER, command = self.color_select)
		self.colorselect_optionmenu.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

		self.design_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Select Design", border_width=2, command=self.design_select)
		self.design_button.place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)

		self.zoom_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Zoom In/Zoom Out", border_width=2, command=self.zoom)
		self.zoom_button.place(relx=0.5, rely=0.29, anchor=tkinter.CENTER)
		self.zoom_slider = customtkinter.CTkSlider(master=self.edit_frame, from_=25, to=400, number_of_steps=75, command=self.zoom_slider)
		self.zoom_slider.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)

		self.undo_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Undo Last Change", border_width=2, command=self.undo)
		self.undo_button.place(relx=0.5, rely=0.41, anchor=tkinter.CENTER)

		self.reset_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Reset to Original", border_width=2, command=self.reset)
		self.reset_button.place(relx=0.5, rely=0.53, anchor=tkinter.CENTER)

		self.back_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Back to Home", border_width=2, command=self.back)
		self.back_button.place(relx=0.5, rely=0.87, anchor=tkinter.CENTER)

		self.saveas_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Save Image As", border_width=2, command=self.save_as)
		self.saveas_button.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

	# method will handle the changing of the color after the user has selected and option from the dropdown
	def color_select(self, choice):
		print(f"Color select menu clicked, color selected: {choice}")
	
	# method will allow the user to choose an image file that is a design to add onto the clothing
	def design_select(self):
		print("Design selection button has been pressed")

	# method will handle the zooming in and out of the selected image to edit
	def zoom(self):
		print("Zoom button has been pressed")

	def zoom_slider(self, value):
		print(f"Zoom slider has been adjusted, new value: {value}")

	# un does the last change the user made to the image
	def undo(self):
		print("Undo button has been pressed")
	
	# resets the selected image to its default when it was first selected
	def reset(self):
		print("Reset button has been pressed")

	# takes the user back to the home screen
	def back(self):
		print("Back button has been pressed")

	# prompts the user to save the newly edited image to their computer
	def save_as(self):
		print("Save As button has been pressed")

if __name__ == "__main__":
	app = App()
	app.create_buttons()
	app.mainloop()
