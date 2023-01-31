"""
Handles the logic based on input received from different actors.
"""

def user_identifier_input(user_id):
    """
    Receive the user identifier when the user enters the shop.

    Return specific message if the user is found or not.
    """
    pass

def scale_entry_input(weight):
    """
    Input of the weight when entering the shop.

    Records the weight and prepare it for exit comparison.
    """
    pass

def scale_exit_input(weight):
    """
    Input of the weight when exitting the shop.

    Compare the weight with the entry weight plus product weight.
    """
    # Exit weight needs to be equal with entry weight + total product weight

    # Add a margin of error of 100/200 grams

    # Return a specific message
    pass

def scanned_product_input(product_code):
    """
    Receive the item's code from the RFID scanner.

    Return product's details based on the product code.
    """
    pass
