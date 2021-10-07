def convert(time):
      hour = int(time[0:2])
      minutes = int(time[3:5])
      seconds = int(time[6:8])
      print(hour*3600 + minutes*60 + seconds)
    
time = input("please enter a full hour like 01:00:20   :  ")
convert(time)