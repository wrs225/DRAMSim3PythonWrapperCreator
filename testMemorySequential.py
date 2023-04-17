import memory_system
import ctypes
import numpy as np

memsys = memory_system.MemorySystem(u'./DDR3_1Gb_x8_1333.ini',u'./')

base_addr = 0

stride = 64

curr_addr = base_addr

cycles = 0
while curr_addr != 6400:
    memsys.ClockTick()
    cycles = cycles + 1
    if(memsys.WillAcceptTransaction(curr_addr, True)):
        memsys.AddTransaction(curr_addr, True)
        curr_addr = curr_addr + stride

print(cycles)
cycles = 0
curr_addr = base_addr
while curr_addr != 6400:
    memsys.ClockTick()
    cycles = cycles + 1
    if(memsys.WillAcceptTransaction(curr_addr, False)):
        memsys.AddTransaction(curr_addr, False)
        curr_addr = curr_addr + stride
print(cycles)

memsys.PrintStats()   
