from car_control_statechart import CarControlStatechart
from yakindu.timer.timer_service import TimerService 
import time

class Callback:
  def __init__(self, sm):
    self.sm = sm

  def move(self, mode):
    print("move: " + mode)

  def brakelights(self, mode):
    print("brakelights: " + mode)

class Main:
  def __init__(self):
    self.sm = CarControlStatechart()
    self.timer_service = TimerService()
    self.callback = Callback(self.sm)

  def setup(self):
    self.sm.timer_service = self.timer_service
    self.sm.operation_callback = self.callback

  def shutdown(self):
    print('shutdown')
    self.sm.exit()
    print('end of program')

  def run(self):
    try:
      self.sm.enter()
      print("obstacle detected")
      self.sm.raise_obstacle_detected()
      time.sleep(2)
      print("obstacle detected")
      self.sm.raise_obstacle_detected()
      time.sleep(1)
      print("power down")
      self.sm.raise_power_down()
    except KeyboardInterrupt:
      self.shutdown()

if __name__ == '__main__':
  m = Main()
  m.setup()
  m.run()
