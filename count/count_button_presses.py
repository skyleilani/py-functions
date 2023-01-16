def count_button_presses(button_pin):
    """
    A function that counts the number of times a button is pressed on an IoT device.
    :param button_pin: The pin number the button is connected to.
    :return: The number of times the button was pressed.
    """
    count = 0
    # Set up the button as an input
    GPIO.setup(button_pin, GPIO.IN)
    # Continuously check the button state
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            count += 1
    return count
