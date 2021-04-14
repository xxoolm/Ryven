import ryvencore_qt as rc
import msvcrt


class AutoNode_msvcrt_SetErrorMode(rc.Node):
    title = 'SetErrorMode'
    type_ = 'msvcrt'
    description = '''Wrapper around SetErrorMode.'''
    init_inputs = [
        rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.SetErrorMode(self.input(0)))
        


class AutoNode_msvcrt_get_osfhandle(rc.Node):
    title = 'get_osfhandle'
    type_ = 'msvcrt'
    description = '''Return the file handle for the file descriptor fd.

Raises OSError if fd is not recognized.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.get_osfhandle(self.input(0)))
        


class AutoNode_msvcrt_getch(rc.Node):
    title = 'getch'
    type_ = 'msvcrt'
    description = '''Read a keypress and return the resulting character as a byte string.

Nothing is echoed to the console. This call will block if a keypress is
not already available, but will not wait for Enter to be pressed. If the
pressed key was a special function key, this will return '\000' or
'\xe0'; the next call will return the keycode. The Control-C keypress
cannot be read with this function.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.getch())
        


class AutoNode_msvcrt_getche(rc.Node):
    title = 'getche'
    type_ = 'msvcrt'
    description = '''Similar to getch(), but the keypress will be echoed if possible.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.getche())
        


class AutoNode_msvcrt_getwch(rc.Node):
    title = 'getwch'
    type_ = 'msvcrt'
    description = '''Wide char variant of getch(), returning a Unicode value.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.getwch())
        


class AutoNode_msvcrt_getwche(rc.Node):
    title = 'getwche'
    type_ = 'msvcrt'
    description = '''Wide char variant of getche(), returning a Unicode value.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.getwche())
        


class AutoNode_msvcrt_heapmin(rc.Node):
    title = 'heapmin'
    type_ = 'msvcrt'
    description = '''Minimize the malloc() heap.

Force the malloc() heap to clean itself up and return unused blocks
to the operating system. On failure, this raises OSError.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.heapmin())
        


class AutoNode_msvcrt_kbhit(rc.Node):
    title = 'kbhit'
    type_ = 'msvcrt'
    description = '''Return true if a keypress is waiting to be read.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.kbhit())
        


class AutoNode_msvcrt_locking(rc.Node):
    title = 'locking'
    type_ = 'msvcrt'
    description = '''Lock part of a file based on file descriptor fd from the C runtime.

Raises OSError on failure. The locked region of the file extends from
the current file position for nbytes bytes, and may continue beyond
the end of the file. mode must be one of the LK_* constants listed
below. Multiple regions in a file may be locked at the same time, but
may not overlap. Adjacent regions are not merged; they must be unlocked
individually.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='nbytes'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.locking(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_msvcrt_open_osfhandle(rc.Node):
    title = 'open_osfhandle'
    type_ = 'msvcrt'
    description = '''Create a C runtime file descriptor from the file handle handle.

The flags parameter should be a bitwise OR of os.O_APPEND, os.O_RDONLY,
and os.O_TEXT. The returned file descriptor may be used as a parameter
to os.fdopen() to create a file object.'''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
rc.NodeInputBP(label='flags'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.open_osfhandle(self.input(0), self.input(1)))
        


class AutoNode_msvcrt_putch(rc.Node):
    title = 'putch'
    type_ = 'msvcrt'
    description = '''Print the byte string char to the console without buffering.'''
    init_inputs = [
        rc.NodeInputBP(label='char'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.putch(self.input(0)))
        


class AutoNode_msvcrt_putwch(rc.Node):
    title = 'putwch'
    type_ = 'msvcrt'
    description = '''Wide char variant of putch(), accepting a Unicode value.'''
    init_inputs = [
        rc.NodeInputBP(label='unicode_char'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.putwch(self.input(0)))
        


class AutoNode_msvcrt_setmode(rc.Node):
    title = 'setmode'
    type_ = 'msvcrt'
    description = '''Set the line-end translation mode for the file descriptor fd.

To set it to text mode, flags should be os.O_TEXT; for binary, it
should be os.O_BINARY.

Return value is the previous mode.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.setmode(self.input(0), self.input(1)))
        


class AutoNode_msvcrt_ungetch(rc.Node):
    title = 'ungetch'
    type_ = 'msvcrt'
    description = '''Opposite of getch.

Cause the byte string char to be "pushed back" into the
console buffer; it will be the next character read by
getch() or getche().'''
    init_inputs = [
        rc.NodeInputBP(label='char'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.ungetch(self.input(0)))
        


class AutoNode_msvcrt_ungetwch(rc.Node):
    title = 'ungetwch'
    type_ = 'msvcrt'
    description = '''Wide char variant of ungetch(), accepting a Unicode value.'''
    init_inputs = [
        rc.NodeInputBP(label='unicode_char'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, msvcrt.ungetwch(self.input(0)))
        