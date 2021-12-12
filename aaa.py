import tkinter as tk
from Tools.pynche import ColorDB
import os
import colorsys

rgb_file = os.path.join(os.path.dirname(ColorDB.__file__), 'X', 'rgb.txt')
rgb_db = ColorDB.get_colordb(rgb_file)
colors = [x.lower().replace(' ', '') for x in rgb_db.unique_names()]

# Separating the grayscale looks nicer
grayscale = []
for v in ['black'] + ['gray{}'.format(i) for i in range(0, 101)] + ['white']:
    if v in colors:
        colors.remove(v)
        grayscale.append(v)
colors.sort(key=lambda x: colorsys.rgb_to_hls(*rgb_db.find_byname(x)))
colors = grayscale + colors

# Use white on dark colors, black on light
def calculateContrast(color):
    # Converting to 8 bit from 16 bit, and diving by 255 (255 * 256 = 65280)
    rgb = [c / 65280 for c in color]
    r, g, b = [(c / 12.92) if c <= 0.03928 else
               ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    if luminance > 0.179:
        return '#000000'
    else:
        return '#ffffff'

class ColorGrid(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.canvas = tk.Canvas(root)
        self.frame = tk.Frame(self.canvas)
        self.scroll = tk.Scrollbar(root, orient=tk.VERTICAL,
                                   command=self.canvas.yview)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.scroll.grid(row=0, column=1, sticky='nsw')
        self.canvas.create_window(0, 0, window=self.frame, anchor='nw')
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.canvas.bind('<Configure>', self._onFrameConfigure)

        columns = 8
        rows = len(colors) // columns + 1
        max_width = len(max(colors, key=lambda x: len(x)))
        for i, color in enumerate(colors):
            fg_color = calculateContrast(root.winfo_rgb(color))
            # Pseudo-label, allows for easy changing of border color
            entry = tk.Entry(self.frame, width=max_width, justify=tk.CENTER,
                             relief=tk.FLAT, disabledbackground=color,
                             disabledforeground=fg_color, cursor='arrow',
                             highlightbackground=color, highlightthickness=3)
            entry.insert(0, color)
            entry.config(state='disabled')
            entry.grid(row=i % rows, column=i // rows, sticky="ew")
            entry.bind('<Double-1>', self._clipboard_copy)
            entry.bind('<Enter>', lambda event, widget=entry: widget.config(
                       highlightbackground=widget['disabledforeground']))
            entry.bind('<Leave>', lambda event, widget=entry: widget.config(
                       highlightbackground=widget['disabledbackground']))

        self.canvas.update()
        new_height = min(self.winfo_screenheight() * 2 // 3,
                         self.canvas.bbox('all')[3])
        self.canvas.config(width=self.canvas.bbox('all')[2],
                           yscrollcommand=self.scroll.set, height=new_height)
        self.canvas.bind_all('<MouseWheel>', lambda event:
                             self.canvas.yview_scroll(int(-1 * event.delta),
                                                      'units'))

    # Copy hex code to clipboard
    def _clipboard_copy(self, event):
        entry = event.widget
        rgb_tuple = self.winfo_rgb(entry.get())
        hex_code = '#{:02x}{:02x}{:02x}'.format(*[i // 256 for i in rgb_tuple])
        self.clipboard_clear()
        self.clipboard_append(hex_code)

    def _onFrameConfigure(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

if __name__ == '__main__':
    # Better readability on high DPI displays
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
    root = tk.Tk()
    root.title("Named Color Chart")
    ColorGrid(root).grid(row=0, column=0, sticky='nsew')
    root.mainloop()