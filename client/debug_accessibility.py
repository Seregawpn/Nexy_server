
import sys
import ctypes
import ctypes.util
from CoreFoundation import CFStringCreateWithCString, kCFStringEncodingUTF8

def test_ax_prompt():
    print("--- DIAGNOSTIC: Accessibility Prompt ---")
    print(f"Process ID: {sys.argv[0]}")
    
    # Load ApplicationServices
    lib_path = ctypes.util.find_library("ApplicationServices")
    if not lib_path:
        print("ERROR: Could not find ApplicationServices framework.")
        return

    print(f"Loaded ApplicationServices: {lib_path}")
    app_services = ctypes.cdll.LoadLibrary(lib_path)
    
    # Define AXIsProcessTrustedWithOptions
    # Boolean AXIsProcessTrustedWithOptions(CFDictionaryRef options);
    AXIsProcessTrustedWithOptions = app_services.AXIsProcessTrustedWithOptions
    AXIsProcessTrustedWithOptions.argtypes = [ctypes.c_void_p]
    AXIsProcessTrustedWithOptions.restype = ctypes.c_bool
    
    # Create Option Dictionary (CFDictionary)
    # This is complex in pure ctypes without PyObjC. 
    # Attempting to use a simplified check or see if we can trigger it.
    
    # If we are effectively on Sequoia, just calling this MIGHT crash if not entitlement-checked.
    # However, constructing the CFDictionary correctly via ctypes is verbose.
    # Let's try importing PyObjC if available, else skip complex CF construction
    # and just call the simple `AXIsProcessTrusted()` (no options) to see basic status,
    # AND then try the crashing call if we can construct the dict.
    
    try:
        import ApplicationServices as AS
        print("PyObjC 'ApplicationServices' import successful.")
        
        options = {AS.kAXTrustedCheckOptionPrompt: True}
        print("Calling AXIsProcessTrustedWithOptions(prompt=True) via PyObjC...")
        
        is_trusted = AS.AXIsProcessTrustedWithOptions(options)
        print(f"Result: {is_trusted}")
        print("SUCCESS: Did not crash.")
        
    except ImportError:
        print("PyObjC not found. Falling back to complex ctypes or aborting.")
        # Without PyObjC, constructing a CFDictionary is hard in a quick script.
        # But the goal is to see if it *crashes*.
        # The app uses `AXIsProcessTrustedWithOptions` so it likely has PyObjC or specific wrappers.
        print("Cannot robustly test crash without PyObjC installed in this env.")

if __name__ == "__main__":
    test_ax_prompt()
