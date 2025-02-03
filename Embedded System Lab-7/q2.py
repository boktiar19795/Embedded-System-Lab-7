import RPi.GPIO as GPIO
import time

input_motor_pin_A = 11  # pin11
input_motor_pin_B = 12  # pin12
turnon_motor = 13  # pin13
color_yellow_pinA = 38  # pin38
color_red_pinB = 40  # pin40

def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(input_motor_pin_A, GPIO.OUT)  # mode --- output
    GPIO.setup(input_motor_pin_B, GPIO.OUT)
	
    GPIO.setup(turnon_motor, GPIO.OUT)
    
    GPIO.setup(color_yellow_pinA, GPIO.OUT)  # Yellow LED pin as output
    GPIO.setup(color_red_pinB, GPIO.OUT)  # Red LED pin as output
    
    GPIO.output(turnon_motor, GPIO.LOW)  # motor stop
    
    GPIO.output(color_yellow_pinA, GPIO.LOW)  # Turn off yellow LED
    GPIO.output(color_red_pinB, GPIO.LOW)  # Turn off red LED

def loop():
    try:
        while True:
            print('Press Ctrl+C to end the program...')
            GPIO.output(turnon_motor, GPIO.HIGH)  # motor driver enable
			
            GPIO.output(input_motor_pin_A, GPIO.HIGH)  # clockwise
            GPIO.output(input_motor_pin_B, GPIO.LOW)
			
            GPIO.output(color_yellow_pinA, GPIO.HIGH)  # Turn on yellow LED
            time.sleep(6.5)

            GPIO.output(turnon_motor, GPIO.LOW)  # motor stop
            GPIO.output(color_yellow_pinA, GPIO.LOW)  # Turn off yellow LED
            time.sleep(6.5)

            GPIO.output(turnon_motor, GPIO.HIGH)  # motor driver enable
            GPIO.output(input_motor_pin_A, GPIO.LOW)  # anticlockwise
            GPIO.output(input_motor_pin_B, GPIO.HIGH)
            GPIO.output(color_red_pinB, GPIO.HIGH)  # Turn on red LED
            time.sleep(6.5)

            GPIO.output(turnon_motor, GPIO.LOW)  # motor stop
            GPIO.output(color_red_pinB, GPIO.LOW)  # Turn off red LED
            time.sleep(6.5)
    except KeyboardInterrupt:
        destroy()

def destroy():
    GPIO.output(turnon_motor, GPIO.LOW)  # motor stop
    GPIO.output(color_yellow_pinA, GPIO.LOW)  # Turn off yellow LED
    GPIO.output(color_red_pinB, GPIO.LOW)  # Turn off red LED

def main():
    setup()
    loop()

if __name__ == '__main__':
    main()

