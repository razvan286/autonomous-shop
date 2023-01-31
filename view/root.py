"""
Create all elements from the main window.
"""

import tkinter as tk


def create_section_scan_user_id(main_window, rfid):
    """
    Create the scan user id section.

    Elements:
        Label: title
        Entry: disabled that gets the value from the rfid
    """
    label_scan_user_id = tk.Label(main_window, text="Scan client ID", font=('Arial', 16))
    entry_user_id = tk.Entry(main_window, textvariable=rfid.get_id(), state='disabled')
    label_scan_user_id.place(x=50, y=50)
    entry_user_id.place(x=50, y=100, height=30, width=135)


def create_section_entry_weight(main_window):
    """
    Create the entry weight section.

    Elements:
        Label: title
        Entry: input the weight of the client at the entrance
        Button: store locally the client's weight
    """
    pass


def create_section_scan_product(main_window, rfid):
    """
    Create the scan product section.

    Elements:
        Label: title
        Entry: disabled that gets the product id from the rfid
        Button: add product to check list
    """
    pass


def create_section_exit_weight(main_window):
    """
    Create the exit weight section.

    Elements:
        Label: title
        Entry: input the weight of the client at the exit
        Button: compare the entry weight with the current one
    """
    pass


def create_main_window(main_window, rfid):
    """
    Create main window.
    """
    main_window.geometry("1700x600")
    main_window.title("Autonomous Shop")
    # Create all sections
    create_section_scan_user_id(main_window, rfid)
    main_window.mainloop()