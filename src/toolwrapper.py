'''A module for interfacing with external text tools.

Copyright ® 2015-2016 Luís Gomes <luismsgomes@gmail.com>
'''


__version__ = '0.2.0'


import io
import logging
import subprocess


class ToolException(Exception):
    pass


class ToolWrapper:
    '''A base class for interfacing with a command line tool via stdin/stdout.

    Communicates with a process via stdin/stdout pipes. When the ToolWrapper
    instance is no longer needed, the close() method should be called to
    free system resources. The class supports the context manager interface; if
    used in a with statement, the close() method is invoked automatically.

    Example usage:

    >>> sed = ToolWrapper(['/bin/sed', 's/Hello/Hi/'])
    >>> sed.writeline('Hello there!')
    >>> sed.readline()
    'Hi there!'
    >>> sed.close()
    '''

    def __init__(self, argv, encoding='utf-8', start=True, cwd=None):
        self.argv = argv
        self.encoding = encoding
        self.cwd = cwd
        self.closed = True
        self.logger = logging.getLogger(self.__class__.__name__)
        if start:
            self.start()

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __repr__(self):
        return '{self.__class__.__name__}({self.argv!r}, '\
            'encoding={self.encoding!r}, cwd={self.cwd!r})'.format(self=self)

    def __str__(self):
        return self.__class__.__name__

    def start(self):
        if not self.closed:
            raise ToolException('not closed')
        self.logger.info('executing argv ' + repr(self.argv))
        self.proc = subprocess.Popen(
            ['stdbuf', '-i0', '-o0'] + self.argv,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.cwd
        )
        self.stdin = io.TextIOWrapper(
            self.proc.stdin,
            encoding=self.encoding,
            line_buffering=True
        )
        self.stdout = io.TextIOWrapper(
            self.proc.stdout,
            encoding=self.encoding,
            line_buffering=True
        )
        self.stderr = io.TextIOWrapper(
            self.proc.stderr,
            encoding=self.encoding,
            line_buffering=True
        )
        self.closed = False
        self.logger.info('spawned process %d', self.proc.pid)

    def restart(self):
        self.close()
        self.start()

    def close(self):
        '''Closes the pipe to the process.'''
        if hasattr(self, 'closed') and not self.closed:
            self.logger.info('killing process %d', self.proc.pid)
            self.proc.kill()
            self.closed = True

    def writeline(self, line):
        if self.closed:
            raise ToolException('closed')
        self.logger.debug('<< %s', line)
        self.stdin.write(line + '\n')
        self.stdin.flush()

    def readline(self):
        if self.closed:
            raise ToolException('closed')
        self.logger.debug('readline()')
        line = self.stdout.readline().rstrip('\n')
        self.logger.debug('>> ' + line)
        return line

if __name__ == '__main__':
    from doctest import testmod
    testmod()
