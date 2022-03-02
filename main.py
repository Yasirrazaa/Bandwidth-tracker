import time
import psutil

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent
while True:
  
  bytes_received =psutil.net_io_counters().bytes_recv
  bytes_sent = psutil.net_io_counters().bytes_sent
  bytes_total = bytes_received + bytes_sent
  
  new_received = bytes_received - last_received
  new_sent = bytes_sent - last_sent
  new_total = bytes_total - last_total


  mb_received = new_received/1024/1024
  mb_sent = new_sent/1024/1024
  mb_total = new_total/1024/1024

  
print(f"{mb_received:.2f } MB received, {mb_sent:.2f } MB sent, {mb_total:.2f } MB total")
bytes_received = last_received
bytes_sent = last_sent
bytes_total = last_total
time.sleep(1)
  

