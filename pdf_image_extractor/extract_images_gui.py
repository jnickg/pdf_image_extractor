#!/usr/bin/env python3
import tkinter
from tkinter import filedialog
from .extract_images import extract_images

def do_extract_images_with_notification(fname, out_name):
    """Extract images from a PDF file.

    Parameters
    ----------
    fname : str
        Path to the PDF file.
    out_name : str
        Path to the output directory.

    Returns
    -------
    None
    """

    total_extracted = 0
    try:
        total_extracted = extract_images(fname, out_name)
    except Exception as e:
        # use tk to show a pop-up window
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showerror(title='Error', message=f'Error: {e}')
    else:
        # use tk to show a pop-up window
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo(title='Success', message=f'{total_extracted} images extracted\nfrom PDF: {fname}\n\nto directory: {out_name}.')
        print(f'Extracted {total_extracted} images from {fname} to {out_name}.')

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Extract images from PDF')
    root.resizable(False, False)

    # Create a label
    label = tkinter.Label(root, text='Extract images from PDF')
    label.pack(pady=10)

    # Create a frame
    frame = tkinter.Frame(root)
    frame.pack(pady=10)

    # Create a label for the file name
    file_label = tkinter.Label(frame, text='File name:')
    file_label.grid(row=0, column=0, padx=10)

    # Create an entry for the file name
    file_entry = tkinter.Entry(frame, width=30)
    file_entry.grid(row=0, column=1, padx=10)

    # Create a "Browse" button to pick a file, which must be a PDF
    browse_button = tkinter.Button(frame, text='Browse',
                                      command=lambda: file_entry.insert(0,
                                                                        filedialog.askopenfilename(filetypes=[('PDF files', '*.pdf')],
                                                                                                   title='Select a PDF file',
                                                                                                   defaultextension='.pdf',
                                                                                                   initialdir='~/')))
    browse_button.grid(row=0, column=2, padx=10)

    # Create a label for the output directory
    out_label = tkinter.Label(frame, text='Output directory:')
    out_label.grid(row=1, column=0, padx=10)

    # Create an entry for the output directory
    out_entry = tkinter.Entry(frame, width=30)
    out_entry.grid(row=1, column=1, padx=10)

    # Create a "Browse" button to pick an output directory, which must be a directory
    browse_button = tkinter.Button(frame, text='Browse',
                                      command=lambda: out_entry.insert(0,
                                                                        filedialog.askdirectory(title='Select an output directory',
                                                                                                 initialdir='~/',
                                                                                                 mustexist=False)))
    browse_button.grid(row=1, column=2, padx=10)

    # Create a button to extract images
    extract_button = tkinter.Button(frame, text='Extract images',
                                    command=lambda: do_extract_images_with_notification(file_entry.get(),
                                                                                        out_entry.get()))
    extract_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()