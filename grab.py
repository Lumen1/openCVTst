import vidcap
from PIL import ImageTk, Image, ImageOps
import tkinter as tk
import cv2
import atexit

CAP_PROP_FRAME_COUNT = 7
CAP_PROP_FRAME_HEIGHT = 4
CAP_PROP_FRAME_WIDTH = 3

class Device:

    def __init__(self, devnum=0, showVideoWindow=0):
        self.dev = vidcap.new_Dev(devnum, showVideoWindow)

    def displayPropertyPage(self):
        self.dev.displaypropertypage()

    def displayCaptureFilterProperties(self):
        self.dev.displaycapturefilterproperties()

    def displayCapturePinProperties(self):
        self.dev.displaycapturepinproperties()

    def setResolution(self, width, height):
        self.dev.setresolution(width, height)

    def getDisplayName(self):
        return self.dev.getdisplayname()

    def getBuffer(self):
        return self.dev.getbuffer()

    def getImage(self):
        buffer, width, height = self.getBuffer()
        if buffer:
            im = Image.frombuffer('RGB', (width, height), buffer, 'raw')
            b, g, r = im.split()
            im = Image.merge("RGB", (r, g, b))
            return im

    def saveSnapshot(self, filename):
        self.getImage().save(filename)


def listDevices():
    for i in range(0,1000):
        try:
            cam = Device(devnum=i, showVideoWindow=0)
            print(f"{i} {cam.getDisplayName()}")
        except:
            break

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    atexit.register(lambda: cap.release())
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    listDevices()
    dev = Device(1)
    print(dir(dev.dev))
    window = tk.Tk()

    imageFrame = tk.Frame(window, width=1900, height=1000)
    imageFrame.grid(row=0, column=0, padx=10, pady=2)

    lmain = tk.Label(imageFrame)
    lmain.grid(row=0, column=0)

    def show_frame():
        #img = dev.getImage()
        #img = ImageOps.flip(img)
        _,frame=cap.read()
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(1, show_frame)


    # Slider window (slider controls stage position)
    # sliderFrame = tk.Frame(window, width=600, height=100)
    # sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

    show_frame()  # Display 2
    window.mainloop()  # Starts GUI
