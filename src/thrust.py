'''
A program that calculates the thrust of a rocket (assuming standard atmospheric pressure = 101325 pascals) given the Mass flow rate, the exit velocity, the exit pressure and the exit area. 

Author: Seth Gower
'''

questions = ['What is the Mass Flow Rate? ', 'What is the Exit Velocity (m/s)? ', 'What is the Exit Pressure (Pascals)? ', 'What is the Exit Area (in meters)?  ', 101325]
answers = [float, float, float, float]
q = 0
while(q < 4):
    currAnswer = input(questions[q])
    try:
        currAnswer = float(currAnswer)
        if(currAnswer < 0):
            print("C'mon dude, use logic, can't be below 0")
        else:
            answers[q] = currAnswer
            q += 1
    except (TypeError, ValueError):
        print('Are you fucking kidding me TJ, enter a fucking number')
thrust = ((answers[0] * answers[1]) + (answers[2] - questions[4]) * answers[3])
print(thrust)