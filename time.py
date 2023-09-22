# 123

 
import time
import sys
from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu, CALLBACK_SCHEDULE_REPEAT, BooleanVar
from tkinter.constants import E, W, N, S
from threading import Thread  # 用于处理定时器事件，防止主线程被阻塞。   class Clock(Tk):  # 定义一个Clock类继承自Tk。  def __init__(self):    super().__init__()    self.title("专注时钟")    self.geometry("400x150")  # 设置窗口大小。    self.attributes('-topmost', True)  # 让窗口保持在顶部。    self.state("zoomed")  # 让窗口最大化。   def start(self):     self.after(1000, lambda: self.update_clock())     t = Thread(target=self.countdown)     t.daemon = True     t.start()   def update_clock(self):     current_time = time.strftime("%H:%M:%S", time.localtime())     clock_label = Label(self, text=current_time, font=("Arial", 64), bg="#ffffff", fg="#2e2e2e")     clock_label.pack(pady=10)   def countdown(self):     while True:       minute = int(Entry1.get())       second = int(Entry2.get())       total_seconds = minute * 60 + second       if total_seconds <= 0:         Entry1.delete(0, END)         Entry2.delete(0, END)         return       else:         current_seconds = total_seconds - time()         mins, secs = divmod(current_seconds, 60)         timerLabel['text'] = '距离休息还有 {} 分钟 {} 秒'.format(mins, secs)         afterFuncId = self._afterIdle(checkTimeOut)       if checkTimeOut():         print('时间到！')        break  
 
