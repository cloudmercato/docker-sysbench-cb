#!/usr/bin/env python3
import sys
from cb_client import runners

RUNNERS = {
    'cpu': runners.SysbenchCpuRunner,
    'memory': runners.SysbenchRamRunner,
    # 'oltp': runners.SysbenchOltpRunner,
}


def main():
    test = sys.argv.pop(1)
    runner = RUNNERS[test]()
    while 1:
        runner.run()


if __name__ == '__main__':
    main()
