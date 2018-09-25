import curses
import smbus
import time
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2

bus = smbus.SMBus(2)  # Use i2c bus 2
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

#Array for empty board and start of the board
clear = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,]

board = [0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

#Starting board state
bus.write_i2c_block_data(matrix, 0, clear)
bus.write_i2c_block_data(matrix, 0, board)

#Set upencoders
myEncoder = RotaryEncoder(eQEP1)
myEncoder.setAbsolute()
myEncoder.enable()

myEncoder2 = RotaryEncoder(eQEP2)
myEncoder2.setAbsolute()
myEncoder2.enable()

#Start curses for window
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

#Create window for curses
begin_x = 0; begin_y = 0
height = 20; width = 20
win = curses.newwin(height, width, begin_y, begin_x)
x=0
y=0

while True:
    time.sleep(0.1)

    #Right Direction
    if (myEncoder2.position < -5): #Buffer for encoder, check if really negative
        myEncoder.zero() #Zero out encoders
        myEncoder2.zero()
        
        if(x < 7): #Check for wall

            if(board[2*(x+1)] & pow(2,y) == 0x00): #Check if the next space is already colored
                
                x = x+1 #Increment
                board[2*x] = pow(2,y) + board[2*x] #Color next spot Green
                bus.write_i2c_block_data(matrix, 0, board)

                board[2*x+1] = pow(2,y) + board[2*x+1] #Color the spot red as well to make orange for the cursor
                board[2*x-1] = board[2*x-1] - pow(2,y) #Remove the red from the last space to make it green
                bus.write_i2c_block_data(matrix, 0, board)
                

                
            else: #If next space is colored, just color red and remove the red from previous space
                x = x+1
                board[2*x+1] = pow(2,y) + board[2*x+1]
                board[2*x-1] = board[2*x-1] - pow(2,y)
                bus.write_i2c_block_data(matrix, 0, board)
                
        
    #Up Direction
    elif (myEncoder.position < -5): 
        myEncoder.zero()
        myEncoder2.zero()
        
        if(y < 7):

            if(board[2*x] & pow(2, y+1) == 0x00):
                
                y = y+1
                board[2*x] = pow(2,y) + board[2*x]
                bus.write_i2c_block_data(matrix, 0, board)
                
                board[2*x+1] = pow(2,y) + board[2*x+1]
                board[2*x+1] = board[2*x+1] - pow(2,y-1)
                bus.write_i2c_block_data(matrix, 0, board)
                
            else:
                y = y+1
                board[2*x+1] = pow(2,y) + board[2*x+1]
                board[2*x+1] = board[2*x+1] - pow(2,y-1)
                bus.write_i2c_block_data(matrix, 0, board)
                
        
    #Left Direction
    elif (myEncoder2.position > 5): 
        myEncoder.zero()
        myEncoder2.zero()
       
        
        if(x > 0):

            if(board[2*(x-1)] & pow(2,y) == 0x00):
                
                x = x-1
                board[2*x] = pow(2,y) + board[2*x]
                bus.write_i2c_block_data(matrix, 0, board)
                
                board[2*x+1] = pow(2,y) + board[2*x+1]
                board[2*(x+1)+1] = board[2*(x+1)+1] - pow(2,y)
                bus.write_i2c_block_data(matrix, 0, board)
            else:
                x = x-1
                board[2*x+1] = pow(2,y) + board[2*x+1]
                board[2*(x+1)+1] = board[2*(x+1)+1] - pow(2,y)
                bus.write_i2c_block_data(matrix, 0, board)
    
    #Right Direction
    elif (myEncoder.position > 5): 
        myEncoder.zero()
        myEncoder2.zero()
        
        if(y > 0):

            if(board[2*x] & pow(2,y-1) == 0x00):
                
                y = y-1
                board[2*x] = pow(2,y) + board[2*x]
                bus.write_i2c_block_data(matrix, 0, board)
                
                board[2*x+1] = pow(2,y) + board[2*x+1]
                board[2*x+1] = board[2*x+1] - pow(2,y+1)
                bus.write_i2c_block_data(matrix, 0, board)
            else:
                y = y-1
                board[2*x+1] = pow(2,y) + board[2*x+1]
                board[2*x+1] = board[2*x+1] - pow(2,y+1)
                bus.write_i2c_block_data(matrix, 0, board)