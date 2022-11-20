'''
 # @ Author: Peter Bowman
 # @ Create Time: 2022-11-19 15:17:10
 # @ Modified by: Peter Bowman
 # @ Modified time: 2022-11-19 17:05:46
 # @ Description:
 '''


class directionVector():
    def __init__(self, speed:int, direction:int) -> None:
        """
        Initiate the variables requires for processing when function is called

        Args:
            🚙 speed (int): The requested speed that will be made for point adjustment
                    Example: ```new directionVector(50, 45)```
                        will put you going between right and forward at half forward speed
            direction (int): direction out of 360°
                    Example : above will put you at a 45 degree turn path for half speed
        """

        # Can be negative
        self.speed = speed

        # Direction (if direction is 360) else turn straight
        self.direction = direction if direction <= 360 and direction >= 0 else 0 
        # if direction == 0: raise Exception("Direction was Greater or Lower than excepted value. Car will travel straight now instead of imporer value")

    def __call__(self, *args, **kwds) -> tuple:
        """Translate into motor power values

        Returns:
            tuple: (Percentage of Left Motor Power, Percentage of Right Motor Power, Direction either 0 or 1)
       
        [Look at images for help](../images/__call__.jpg))

        """
        # Reduce Global Calls
        direction = self.direction
        speed = self.speed

        # Bool for direction (Forward or Backwards)
        
        # If speed is set WAY to high then set it to max
        if speed > 100:
            speed = 100
        # If speed is negative, then set it to positive because it depends on the angle not power negativity
        elif speed < 0:
            speed = abs(speed)

        # Q1 (0-90)
        if direction in range(0, 91):
            # Direction Below 
            _speed = speed * (direction / 90)
            return (speed, speed - _speed, 0) # Forward
        
        # Q2 (91-180)
        elif direction in range(91, 181):
            # Direction Below 
            _speed = speed * ((direction - 90) / 90)
            return (speed, speed - _speed, 1) # Backwards

        # Q3 (181-270)
        elif direction in range(181, 271):
            # Direction Below 
            _speed = speed * ((direction - 180) / 90)
            return (speed, speed - _speed, 1) # Backwards
        # Q4 (271-360)
        elif direction in range(271, 361):
            # Direction Below 
            _speed = speed * ((direction - 270) / 90)
            return (speed, speed - _speed, 0) # Forwards

    def __str__(self) -> str:
        tuple = self.__call__()
        left, right, direction = tuple
        direction = "forwards" if direction == 0 else "backwards"
        return f"Direction Facts:\n----------------------------\nLeft Wheel Power: {left}% of possible\nRight Wheel Power: {right}% of possible\nGoing Forward/Backwards: {direction}\n----------------------------\nOther Important Details:\n\nAngle: {self.direction}°\nSpeed: {self.speed}%\n----------------------------\n"