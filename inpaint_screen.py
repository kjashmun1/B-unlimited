import tkinter
import customtkinter
from tkinter import filedialog

class InpaintScreen:
	def __init__(self, parent, screen_handler):
		super ().__init__()

		# configure main frame that will hold other frames
		self.main_frame = customtkinter.CTkFrame(master=parent, width=1280, height=720)
		self.main_frame.pack(expand=True, fill="both")

		# configure frame on right side for buttons
		self.button_frame = customtkinter.CTkFrame(master=self.main_frame, width=240, height=704)
		self.button_frame.pack(padx=8, pady=8, side="right")
		
		# configure frame for image display/image choosing
		self.image_frame = customtkinter.CTkFrame(master=self.main_frame, width=1008, height=704)
		self.image_frame.pack(padx=8, pady=8, side="left")

		# configure the buttons in the button frame 
		self.inpaint_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Inapint/Erase", border_width=2, command=self.inpaint)
		self.inpaint_button.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER) 
		self.inpaint_slider = customtkinter.CTkSlider(master=self.button_frame, from_=1, to=100, number_of_steps=99, command=self.inpaint_brush_size)
		self.inpaint_slider.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
		self.inpaint_slider_text = customtkinter.CTkLabel(master=self.button_frame, height=10, width=20, font=("Segoe UI", 8), text=int(self.inpaint_slider.get()))
		self.inpaint_slider_text.place(relx=0.89, rely=0.092)

		self.zoom_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Zoom In/Zoom Out", border_width=2, command=self.zoom)
		self.zoom_button.place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)
		self.zoom_slider = customtkinter.CTkSlider(master=self.button_frame, from_=25, to=400, number_of_steps=75, command=self.zoom_slider)
		self.zoom_slider.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)
		self.zoom_slider_text = customtkinter.CTkLabel(master=self.button_frame, height=10, width=20, font=("Segoe UI", 8), text=int(self.zoom_slider.get()))
		self.zoom_slider_text.place(relx=0.89, rely=0.212)

		self.undo_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Undo Last Change", border_width=2, command=self.undo)
		self.undo_button.place(relx=0.5, rely=0.29, anchor=tkinter.CENTER)

		self.reset_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Reset to Original", border_width=2, command=self.reset)
		self.reset_button.place(relx=0.5, rely=0.41, anchor=tkinter.CENTER)

		self.newimage_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Start New Image", border_width=2, command=self.start_new_image)
		self.newimage_button.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

		self.back_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Back to Home", border_width=2, command=lambda: self.back(screen_handler))
		self.back_button.place(relx=0.5, rely=0.71, anchor=tkinter.CENTER)
		
		self.saveas_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Save Image As", border_width=2, command=self.save_as)
		self.saveas_button.place(relx=0.5, rely=0.79, anchor=tkinter.CENTER)

		self.edit_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Edit Image", border_width=2, command=lambda: self.edit(screen_handler))
		self.edit_button.place(relx=0.5, rely=0.87, anchor=tkinter.CENTER)

		self.finished_button = customtkinter.CTkButton(master=self.button_frame, height=50, width=200, text="Finished", border_width=2, command=self.finished)
		self.finished_button.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

		# configure the button for image selection frame
		self.image_selection_button = customtkinter.CTkButton(master=self.image_frame, height=100, width=400, text="Click here to select an image", border_width=2, command=self.image_selection)
		self.image_selection_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

	# method will 
	def inpaint(self):
		print("Inpaint/Erase button has been pressed")

	# method will handle the changing of teh brush size from the slider
	def inpaint_brush_size(self, value):
		print(f"Current brush size: {value}")
		self.inpaint_slider_text.configure(text=int(value))

	# method will enable the zoom slider
	def zoom(self):
		print("Zoom In/Zoom Out button has been pressed")

	# method will handle the changing of the zoom factor from the sldier
	def zoom_slider(self, value):
		print(f"Current zoom value: {value}")
		self.zoom_slider_text.configure(text=int(value))

	# method will undo last thing the user did to the image 
	def undo(self):
		print("Undo button has been pressed")

	# method will remove current image from the left and replace with button to choose new image
	def start_new_image(self):
		print("Start new image button has been pressed")

	# method will take user back to the previous screen (home screen)
	def back(self, screen_handler):
		print("Back button has been pressed")
		screen_handler.to_home_screen()

	# method will reset the image back to its original form when user selected it
	def reset(self):
		print("Reset button has been pressed")

	# method will signify user is done with inpaitning and will run the inpainting logic
	def finished(self):
		print("Finished button has been pressed")

	# method will open up file explorer for user to choose image they want to inpaint on
	def image_selection(self):
		print("Image selection button has been pressed")
		filepath = filedialog.askopenfilename(title="Choose the image file you wish to inpaint on.", filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg")))
		print(filepath)

	# method will only allow user to hit save as button if finished button has been pressed and will allow user to save image to chosen file
	def save_as(self):
		print("Save As button has been pressed")

	# method will only allow user to hit edit button if finished button is pressed and will allow user to go to the edit screen
	def edit(self, screen_handler):
		print("Edit button has been pressed")
		screen_handler.to_edit_screen()