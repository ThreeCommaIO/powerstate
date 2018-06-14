#!/usr/bin/env python
import os
import signal
import sys

def main():
    if os.getuid() != 0:
        print "This must be run as root"
        sys.exit(1)

    if not os.path.exists('/dev/cpu_dma_latency'):
        print "no PM QOS interface on this system!"
        sys.exit(1)

    try:
        fd = os.open("/dev/cpu_dma_latency", os.O_RDWR)
        os.write(fd, '\0\0\0\0')
        print "Press ^C to close /dev/cpu_dma_latency and exit"
        signal.pause()
    except KeyboardInterrupt, e:
        print "closing /dev/cpu_dma_latency"
        os.close(fd)
        sys.exit(0)

if __name__ == '__main__':
    main()




