def count_motion(motion_sensor_pin):
    """
    A function that counts the number of times a motion is detected using IoT device motion sensor.
    :param motion_sensor_pin: The pin number the motion sensor is connected to.
    :return: The number of times motion is detected.
    """
    count = 0
    # Set up the motion sensor as an input
    GPIO.setup(motion_sensor_pin, GPIO.IN)
    # Continuously check the motion sensor state
    while True:
        if GPIO.input(motion_sensor_pin) == GPIO.HIGH:
            count += 1
    return count
