import os
import pytesseract
from docx import Document
from PIL import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle
from docx2pdf import convert as docx_to_pdf_convert
from pdf2docx import Converter
from pdf2image import convert_from_path

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.2, 0.5, 0.7, 1)
        self.color = (1, 1, 1, 1)
        self.font_size = 22
        self.font_name = 'Roboto'
        self.bold = True
        with self.canvas.before:
            self.rect_color = Color(0.2, 0.5, 0.7, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[25])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class FileConverterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=25)

        self.label = Label(text="To Convert !", font_size=36, size_hint=(1, 0.2), bold=True)
        self.layout.add_widget(self.label)

        self.show_main_buttons()

        self.add_widget(self.layout)

    def show_main_buttons(self):
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.jpeg_button = RoundedButton(text="JPEG", size_hint=(1, 0.15))
        self.jpeg_button.bind(on_press=lambda x: self.manager.app.transition_to("jpeg_screen"))
        self.layout.add_widget(self.jpeg_button)

        self.docx_button = RoundedButton(text="DOCX/DOC", size_hint=(1, 0.15))
        self.docx_button.bind(on_press=lambda x: self.manager.app.transition_to("docx_screen"))
        self.layout.add_widget(self.docx_button)

        self.pdf_button = RoundedButton(text="PDF", size_hint=(1, 0.15))
        self.pdf_button.bind(on_press=lambda x: self.manager.app.transition_to("pdf_screen"))
        self.layout.add_widget(self.pdf_button)

        self.exit_button = RoundedButton(text="Exit", size_hint=(1, 0.15), background_color=(0.8, 0.2, 0.2, 1))
        self.exit_button.bind(on_press=lambda x: self.manager.app.stop() if self.manager else None)
        self.layout.add_widget(self.exit_button)

class JPEGScreen(FileConverterScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_options()

    def show_options(self):
        self.layout.clear_widgets()
        self.show_back_button()

        jpeg_to_pdf_button = RoundedButton(text="JPEG to PDF", size_hint=(1, 0.2))
        jpeg_to_pdf_button.bind(on_press=lambda x: self.manager.app.open_file_chooser("image_to_pdf"))
        self.layout.add_widget(jpeg_to_pdf_button)

        jpeg_to_docx_button = RoundedButton(text="JPEG to DOCX/DOC", size_hint=(1, 0.2))
        jpeg_to_docx_button.bind(on_press=lambda x: self.manager.app.open_file_chooser("jpeg_to_docx"))
        self.layout.add_widget(jpeg_to_docx_button)

    def show_back_button(self):
        anchor_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, 0.1))
        self.back_button = Button(size_hint=(None, None), size=(32, 32),
                                  background_normal='back_arrow.png',
                                  background_down='back_arrow.png',
                                  border=(0, 0, 0, 0))
        self.back_button.bind(on_press=lambda x: self.manager.app.transition_to("main_screen"))

        anchor_layout.add_widget(self.back_button)
        self.layout.add_widget(anchor_layout)

class DOCXScreen(FileConverterScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_options()

    def show_options(self):
        self.layout.clear_widgets()
        self.show_back_button()

        docx_to_pdf_button = RoundedButton(text="DOCX/DOC to PDF", size_hint=(1, 0.2))
        docx_to_pdf_button.bind(on_press=lambda x: self.manager.app.open_file_chooser("doc_to_pdf"))
        self.layout.add_widget(docx_to_pdf_button)
        
        docx_to_jpeg_button = RoundedButton(text="DOCX/DOC to JPEG", size_hint=(1, 0.2))
        docx_to_jpeg_button.bind(on_press=lambda x: self.manager.app.open_file_chooser("docx_to_jpeg"))
        self.layout.add_widget(docx_to_jpeg_button)

    def show_back_button(self):
        anchor_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, 0.1))
        self.back_button = Button(size_hint=(None, None), size=(32, 32),
                                  background_normal='back_arrow.png',
                                  background_down='back_arrow.png',
                                  border=(0, 0, 0, 0))
        self.back_button.bind(on_press=lambda x: self.manager.app.transition_to("main_screen"))

        anchor_layout.add_widget(self.back_button)
        self.layout.add_widget(anchor_layout)

class PDFScreen(FileConverterScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_options()

    def show_options(self):
        self.layout.clear_widgets()
        self.show_back_button()

        pdf_to_jpeg_button = RoundedButton(text="PDF to JPEG", size_hint=(1, 0.2))
        pdf_to_jpeg_button.bind(on_press=lambda x: self.manager.app.open_file_chooser("pdf_to_jpeg"))
        self.layout.add_widget(pdf_to_jpeg_button)

        pdf_to_docx_button = RoundedButton(text="PDF to DOCX/DOC", size_hint=(1, 0.2))
        pdf_to_docx_button.bind(on_press=lambda x: self.manager.app.open_file_chooser("pdf_to_docx"))
        self.layout.add_widget(pdf_to_docx_button)

    def show_back_button(self):
        anchor_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, 0.1))
        self.back_button = Button(size_hint=(None, None), size=(32, 32),
                                  background_normal='back_arrow.png',
                                  background_down='back_arrow.png',
                                  border=(0, 0, 0, 0))
        self.back_button.bind(on_press=lambda x: self.manager.app.transition_to("main_screen"))

        anchor_layout.add_widget(self.back_button)
        self.layout.add_widget(anchor_layout)

class FileConverterApp(App):
    def build(self):
        self.sm = ScreenManager(transition=SlideTransition())

        main_screen = FileConverterScreen(name="main_screen")
        jpeg_screen = JPEGScreen(name="jpeg_screen")
        docx_screen = DOCXScreen(name="docx_screen")
        pdf_screen = PDFScreen(name="pdf_screen")

        self.sm.add_widget(main_screen)
        self.sm.add_widget(jpeg_screen)
        self.sm.add_widget(docx_screen)
        self.sm.add_widget(pdf_screen)

        self.sm.app = self

        return self.sm

    def jpeg_to_docx(self, filename):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        if not filename.endswith('.docx'):
            filename += ".docx"

        try:
            doc = Document()
            for image_path in self.selected_files:
                text = pytesseract.image_to_string(Image.open(image_path))
                doc.add_paragraph(text)
            doc.save(filename)
            self.show_popup("Success", f"JPEG to DOCX saved as: {filename}")
        except Exception as e:
            self.show_popup("Error", f"Failed to convert JPEG to DOCX.\n{e}")

    def transition_to(self, screen_name):
        self.sm.current = screen_name

    def open_file_chooser(self, file_type):
        self.file_type = file_type
        filters = []
        title = ""
        if file_type == "image_to_pdf":
            filters = ["*.jpeg", "*.jpg"]
            title = "Select JPEG Images"
        elif file_type == "doc_to_pdf":
            filters = ["*.docx", "*.doc"]
            title = "Select DOCX/DOC Files"
        elif file_type == "pdf_to_jpeg":
            filters = ["*.pdf"]
            title = "Select PDF for JPEG Conversion"
        elif file_type == "pdf_to_docx":
            filters = ["*.pdf"]
            title = "Select PDF for DOCX/DOC Conversion"
        elif file_type == "jpeg_to_docx":
            filters = ["*.jpeg", "*.jpg"]
            title = "Select JPEG for DOCX Conversion"
        elif file_type == "docx_to_jpeg":
            filters = ["*.docx", "*.doc"]
            title = "Select DOCX/DOC for JPEG Conversion"
    

        content = BoxLayout(orientation='vertical')
        filechooser = FileChooserListView(filters=filters, multiselect=True, path=os.getcwd())
        content.add_widget(filechooser)

        button_layout = BoxLayout(size_hint=(1, 0.2))
        select_button = Button(text="Select", size_hint=(0.5, 1))
        close_button = Button(text="Cancel", size_hint=(0.5, 1))

        button_layout.add_widget(select_button)
        button_layout.add_widget(close_button)

        content.add_widget(button_layout)

        self.popup = Popup(title=title, content=content, size_hint=(0.9, 0.9))
        self.popup.open()

        select_button.bind(on_press=lambda x: self.select_files(filechooser.selection))
        close_button.bind(on_press=lambda x: self.popup.dismiss())

    def select_files(self, file_paths):
        if file_paths:
            self.selected_files = file_paths
            self.popup.dismiss()
            self.ask_save_location()

    def ask_save_location(self):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text="Enter file name:")
        filename_input = TextInput(multiline=False)

        button_layout = BoxLayout(size_hint=(1, 0.2))
        save_button = Button(text="Save", size_hint=(0.5, 1))
        close_button = Button(text="Cancel", size_hint=(0.5, 1))

        button_layout.add_widget(save_button)
        button_layout.add_widget(close_button)

        content.add_widget(label)
        content.add_widget(filename_input)
        content.add_widget(button_layout)

        self.save_popup = Popup(title='Save File As', content=content, size_hint=(0.8, 0.4))
        self.save_popup.open()

        save_button.bind(on_press=lambda x: self.perform_conversion(filename_input.text))
        close_button.bind(on_press=lambda x: self.save_popup.dismiss())

    def perform_conversion(self, filename):
        if not filename:
            self.show_popup("Error", "Please enter a file name.")
            return
        
        if self.file_type in ['image_to_pdf', 'doc_to_pdf', 'docx_to_jpeg']:
            if not filename.endswith('.pdf'):
                filename += ".pdf"
        
        try:
            if self.file_type == 'image_to_pdf':
                first_image = Image.open(self.selected_files[0])
                image_list = [Image.open(fp).convert('RGB') for fp in self.selected_files[1:]]
                first_image.convert('RGB').save(filename, save_all=True, append_images=image_list)
                self.show_popup("Success", f"PDF saved as: {filename}")
            
            elif self.file_type == 'doc_to_pdf':
                docx_to_pdf_convert(self.selected_files[0], filename)
                self.show_popup("Success", f"PDF saved as: {filename}")

            elif self.file_type == 'pdf_to_jpeg':
                images = convert_from_path(self.selected_files[0], 300, poppler_path=r'C:\Program Files\poppler\bin')
                for i, image in enumerate(images):
                    image.save(f"{filename}_page_{i+1}.jpeg", 'JPEG')
                self.show_popup("Success", f"PDF converted to JPEGs with base name: {filename}")

            elif self.file_type == 'pdf_to_docx':
                output_docx = filename if filename.endswith('.docx') else f"{filename}.docx"
                cv = Converter(self.selected_files[0])
                cv.convert(output_docx, start=0, end=None)
                cv.close()
                self.show_popup("Success", f"PDF converted to DOCX as: {output_docx}")

            # DOCX/DOC to JPEG
            elif self.file_type == 'docx_to_jpeg':
                pdf_filename = filename.replace('.pdf', '_temp.pdf')
                docx_to_pdf_convert(self.selected_files[0], pdf_filename)

                images = convert_from_path(pdf_filename, 300, poppler_path=r'C:\Program Files\poppler\bin')
                for i, image in enumerate(images):
                    image.save(f"{filename}_page_{i+1}.jpeg", 'JPEG')
                
                self.show_popup("Success", f"DOCX/DOC converted to JPEGs with base name: {filename}")

                # Geçici PDF dosyasını silme (isteğe bağlı)
                if os.path.exists(pdf_filename):
                    os.remove(pdf_filename)

            # Yeni durum - JPEG to DOCX
            elif self.file_type == 'jpeg_to_docx':
                self.jpeg_to_docx(filename)

        except Exception as e:
            self.show_popup("Error", f"Failed to convert file.\n{e}")
        finally:
            self.save_popup.dismiss()

    def show_popup(self, title, message):
        popup_content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        popup_label = Label(text=message)
        close_button = Button(text="Close", size_hint=(1, 0.2))

        popup_content.add_widget(popup_label)
        popup_content.add_widget(close_button)

        popup = Popup(title=title, content=popup_content, size_hint=(0.8, 0.4))
        popup.open()

        close_button.bind(on_press=lambda x: popup.dismiss())

if __name__ == '__main__':
    Window.size = (400, 600)
    FileConverterApp().run()