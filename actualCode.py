import pytesseract
from PIL import Image
import pyttsx3


def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"


def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {str(e)}")

def start():
    image_file = "img.jpeg"
    extracted_text = extract_text_from_image(image_file)
    if extracted_text:
            print("Extracted Text:")
            print(extracted_text)
            print("\nPlaying the text using the system speaker...")
            speak_text(extracted_text)



if __name__ == "__main__":
    print("Hello world from actualCode.py")