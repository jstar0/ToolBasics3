import signal, time

def signalHandler(signum, time):
    print("\n获取到信号：", signum)

signal.signal(signal.SIGINT, signalHandler)
i = 0
while True:
    time.sleep(.1)
    print("\r{}".format(i), end="")
    i += 1