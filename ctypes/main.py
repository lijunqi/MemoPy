import threading
from ctypes import (
    windll,
	c_long, c_int,
	WINFUNCTYPE,
	byref,
	Structure,
)

from ctypes.wintypes import (
    WPARAM, LPARAM, DWORD, MSG,
	POINT,
)

# Some Windows constants
HC_ACTION = 0
WH_KEYBOARD_LL = 13
LLKHF_UP = 128
LLKHF_EXTENDED = 1
LLKHF_INJECTED = 16
WH_MOUSE_LL = 14
LLMHF_INJECTED = 1


VK_F10=0x79

mouseCallback=None

def keyDownCallback(vkCode, scanCode, extended, injected):
	"""Event called by winInputHook when it receives a keyDown.
	"""
	print("KeyDown vkCode: ", vkCode)
	print("KeyDown scanCode: ", scanCode)
	print("KeyDown extended: ", extended)
	print("KeyDown injected: ", injected)
	if vkCode == VK_F10:
		return 1

def keyUpCallback(vkCode, scanCode, extended, injected):
	"""Event called by winInputHook when it receives a keyUp.
	"""
	print("KeyUp vkCode: ", vkCode)
	print("KeyUp scanCode: ", scanCode)
	print("KeyUp extended: ", extended)
	print("KeyUp injected: ", injected)


class KBDLLHOOKSTRUCT(Structure):
	_fields_=[
		('vkCode', DWORD),
		('scanCode', DWORD),
		('flags', DWORD),
		('time', DWORD),
		('dwExtraInfo', DWORD),
	]


class MSLLHOOKSTRUCT(Structure):
	_fields_=[
		('pt', POINT),
		('mouseData', DWORD),
		('flags', DWORD),
		('time', DWORD),
		('dwExtraInfo', DWORD),
	]

#for k in range(256):
#    a = windll.user32.GetKeyState(k)
#    print("a[%d] = %d" %(k, a))

@WINFUNCTYPE(c_long, c_int, WPARAM, LPARAM)
def keyboardHook(code, wParam, lParam):
	""" https://learn.microsoft.com/en-us/windows/win32/winmsg/keyboardproc

	code: If code < zero,
	      the hook procedure must pass the message to the CallNextHookEx function without further processing
		  and should return the value returned by CallNextHookEx.

		  HC_ACTION   0:  The wParam and lParam parameters contain information about a keystroke message.
		  HC_NOREMOVE 3:  The wParam and lParam parameters contain information about a keystroke message,
		                  and the keystroke message has not been removed from the message queue.
						  (An application called the PeekMessage function, specifying the PM_NOREMOVE flag.)

	wParam: The virtual-key code of the key that generated the keystroke message.

	lParam: The repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag.

	Return:
	    type: LRESULT
		If code < 0, the hook procedure must return the value returned by CallNextHookEx.
		If code >= 0, and the hook procedure did not process the message,
		              it is highly recommended that you call CallNextHookEx and return the value it returns;
					  otherwise, other applications that have installed WH_KEYBOARD hooks will not receive hook notifications and may behave incorrectly as a result.
		If the hook procedure processed the message,
		it may return a nonzero value to prevent the system from passing the message to the rest of the hook chain
		or the target window procedure.
	"""
	if code != HC_ACTION:
		# Passes the hook information to the next hook procedure in the current hook chain.
		return windll.user32.CallNextHookEx(0, code, wParam, lParam)
	kbd = KBDLLHOOKSTRUCT.from_address(lParam)
	if keyUpCallback and kbd.flags&LLKHF_UP:
		if not keyUpCallback(kbd.vkCode, kbd.scanCode, bool(kbd.flags&LLKHF_EXTENDED), bool(kbd.flags&LLKHF_INJECTED)):
			return 1
	elif keyDownCallback:
		keyDownRes = keyDownCallback(kbd.vkCode, kbd.scanCode, bool(kbd.flags&LLKHF_EXTENDED), bool(kbd.flags&LLKHF_INJECTED))
		print("keyDownRes: ", keyDownRes)
		if not keyDownRes:
			return 1
		else:
			return 0
	return windll.user32.CallNextHookEx(0, code, wParam, lParam)



WM_MOUSEMOVE=0x0200
WM_LBUTTONDOWN=0x0201
WM_LBUTTONUP=0x0202
WM_LBUTTONDBLCLK=0x0203
WM_RBUTTONDOWN=0x0204
WM_RBUTTONUP=0x0205
WM_RBUTTONDBLCLK=0x0206

def mouseCallback(msg, x, y, injected):
	"""Event called by winInputHook when it receives a mouse event.
	"""
	try:
		curMousePos = (x,y)
		if msg == WM_MOUSEMOVE: 
			print("Mouse Move: ", curMousePos)
		elif msg == WM_LBUTTONDOWN:
			print("Mouse Left")
		elif msg == WM_RBUTTONDOWN:
			print("Mouse Right")
	except Exception as exc:
		print("xxxxxx mouse callback Error: ", str(exc))
	return True


@WINFUNCTYPE(c_long, c_int, WPARAM, LPARAM)
def mouseHook(code,wParam,lParam):
	if code != HC_ACTION:
		return windll.user32.CallNextHookEx(0,code,wParam,lParam)
	msll = MSLLHOOKSTRUCT.from_address(lParam)
	if not mouseCallback(wParam, msll.pt.x, msll.pt.y, msll.flags&LLMHF_INJECTED):
		return 1
	return windll.user32.CallNextHookEx(0,code,wParam,lParam)


##################################################################################################################
def hookThreadFunc():
    # * SetWindowsHookEx 可用于将 DLL 注入另一个进程. 32 位 DLL 无法注入 64 位进程, 64 位 DLL 无法注入 32 位进程.
	# * Installs an application-defined hook procedure into a hook chain.
	# * You would install a hook procedure to monitor the system for certain types of events.
	# * These events are associated either with a specific thread or with all threads in the same desktop as the calling thread.
	keyHookID = windll.user32.SetWindowsHookExW(
		WH_KEYBOARD_LL, # 钩子类型
		keyboardHook,   # 回调函数地址
		windll.kernel32.GetModuleHandleW(None), # A handle to the DLL containing the hook procedure pointed to by the lpfn parameter.
		0 # The ID of the thread with which the hook procedure is to be associated.
		  # For desktop apps, if this parameter is zero,
		  # the hook procedure is associated with all existing threads running in the same desktop as the calling thread. 
	)
	if keyHookID == 0:
		raise OSError("Could not register keyboard hook")
	print("Key Hook ID: ", keyHookID)
	mouseHookID = windll.user32.SetWindowsHookExW(WH_MOUSE_LL, mouseHook, windll.kernel32.GetModuleHandleW(None), 0)
	if mouseHookID == 0:
		raise OSError("Could not register mouse hook")
	print("Mouse Hook ID: ", mouseHookID)

	msg = MSG()
	if msg is None:
		print("=== msg is None ===")
	else:
		print("=== msg: ", msg)
	if byref(msg) is None:
		print("=== byref msg is None ===")
	else:
		print("=== byref msg: ", byref(msg))
	while windll.user32.GetMessageW(byref(msg), None, 0, 0):
		print("===> Get Msg: ", msg)
		pass
	if windll.user32.UnhookWindowsHookEx(keyHookID) == 0:
		raise OSError("could not unregister key hook %s"%keyHookID)
	if windll.user32.UnhookWindowsHookEx(mouseHookID)==0:
		raise OSError("could not unregister mouse hook %s"%mouseHookID)


def main():
	hookThread = threading.Thread( name=__name__, target=hookThreadFunc)
	hookThread.start()
	hookThread.join()
	print("Done.")

if __name__ == "__main__":
	print("Start")
	main()
