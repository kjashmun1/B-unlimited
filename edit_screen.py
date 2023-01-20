import tkinter
import customtkinter
from tkinter import filedialog

class EditScreen:
	def __init__(self, parent, screen_handler):
		super ().__init__()

		# configure the main frame to hold other frames
		self.main_frame = customtkinter.CTkFrame(master=parent, width=1280, height=720)
		self.main_frame.pack(fill="both", expand=True)

		# configure frame on right side for edit buttons
		self.edit_frame = customtkinter.CTkFrame(master=self.main_frame, width=240, height=704)
		self.edit_frame.pack(padx=8, pady=8, side="right")

		# configure frame on left side for displaying/handling image
		self.image_frame = customtkinter.CTkFrame(master=self.main_frame, width=1008, height=704)
		self.image_frame.pack(padx=8, pady=8, side="left")
	
		# configure edit buttons that will be in the edit button frame
		self.colorselect_optionmenu = customtkinter.CTkOptionMenu(master=self.edit_frame, height=50, width=200, values=["Default", "other"], anchor=tkinter.CENTER, command = self.color_select)
		self.colorselect_optionmenu.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

		self.design_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Select Design", border_width=2, command=self.design_select)
		self.design_button.place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)

		self.zoom_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Zoom In/Zoom Out", border_width=2, command=self.zoom)
		self.zoom_button.place(relx=0.5, rely=0.29, anchor=tkinter.CENTER)
		self.zoom_slider = customtkinter.CTkSlider(master=self.edit_frame, from_=25, to=400, number_of_steps=75, command=self.zoom_slider)
		self.zoom_slider.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)
		self.zoom_slider_text = customtkinter.CTkLabel(master=self.edit_frame, height=10, width=20, font=("Segoe UI", 8), text=int(self.zoom_slider.get()))
		self.zoom_slider_text.place(relx=0.89, rely=0.332)

		self.undo_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Undo Last Change", border_width=2, command=self.undo)
		self.undo_button.place(relx=0.5, rely=0.41, anchor=tkinter.CENTER)

		self.reset_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Reset to Original", border_width=2, command=self.reset)
		self.reset_button.place(relx=0.5, rely=0.53, anchor=tkinter.CENTER)
  
		self.toinpaint_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Inpaint on New Image", border_width=2, command=lambda: self.to_inpaint(screen_handler))
		self.toinpaint_button.place(relx=0.5, rely=0.79, anchor=tkinter.CENTER)

		self.back_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Back to Home", border_width=2, command=lambda: self.back(screen_handler))
		self.back_button.place(relx=0.5, rely=0.87, anchor=tkinter.CENTER)

		self.saveas_button = customtkinter.CTkButton(master=self.edit_frame, height=50, width=200, text="Save Image As", border_width=2, command=self.save_as)
		self.saveas_button.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

	# method will handle the changing of the color after the user has selected and option from the dropdown
	def color_select(self, choice):
		print(f"Color select menu clicked, color selected: {choice}")
	
	# method will allow the user to choose an image file that is a design to add onto the clothing
	def design_select(self):
		print("Design selection button has been pressed")
		filepath = filedialog.askopenfilename(title="Choose the design file you wish to add to image.", filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg")))
		filepath = filepath.split("/")
		self.design_button.configure(text=filepath[-1])

	# method will handle the zooming in and out of the selected image to edit
	def zoom(self):
		print("Zoom button has been pressed")

	def zoom_slider(self, value):
		print(f"Zoom slider has been adjusted, new value: {value}")
		self.zoom_slider_text.configure(text=int(value))

	# un does the last change the user made to the image
	def undo(self):
		print("Undo button has been pressed")
	
	# resets the selected image to its default when it was first selected
	def reset(self):
		print("Reset button has been pressed")
  
	# takes the user back to the inpaint screen
	def to_inpaint(self, screen_handler):
		print("To inpaint screen button has been pressed")
		screen_handler.to_inpaint_screen()

	# takes the user back to the home screen
	def back(self, screen_handler):
		print("Back button has been pressed")
		screen_handler.to_home_screen()

	# prompts the user to save the newly edited image to their computer
	def save_as(self):
		print("Save As button has been pressed")
