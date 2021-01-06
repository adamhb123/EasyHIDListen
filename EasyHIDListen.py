__author__="Adam Brewer"
import subprocess
import sys
import os
import ctypes



translation_table = {"0x00": "UNASSIGNED", "0x01": "OVERRUN_ERROR", "0x02": "POST_FAIL", "0x03": "ERROR_UNDEFINED",
                     "0x04": "A", "0x05": "B", "0x06": "C", "0x07": "D", "0x08": "E", "0x09": "F", "0x0A": "G",
                     "0x0B": "H", "0x0C": "I", "0x0D": "J", "0x0E": "K", "0x0F": "L", "0x10": "M", "0x11": "N",
                     "0x12": "O", "0x13": "P", "0x14": "Q", "0x15": "R", "0x16": "S", "0x17": "T", "0x18": "U",
                     "0x19": "V", "0x1A": "W", "0x1B": "X", "0x1C": "Y", "0x1D": "Z", "0x1E": "1", "0x1F": "2",
                     "0x20": "3", "0x21": "4", "0x22": "5", "0x23": "6", "0x24": "7", "0x25": "8", "0x26": "9",
                     "0x27": "0", "0x28": "ENTER", "0x29": "ESC", "0x2A": "BACKSPACE", "0x2B": "TAB", "0x2C": "SPACE",
                     "0x2D": "MINUS", "0x2E": "EQUAL", "0x2F": "LEFT_BRACE", "0x30": "RIGHT_BRACE", "0x31": "BACKSLASH",
                     "0x32": "EUROPE_1", "0x33": "SEMICOLON", "0x34": "QUOTE", "0x35": "BACK_QUOTE", "0x36": "COMMA",
                     "0x37": "PERIOD", "0x38": "SLASH", "0x39": "CAPS_LOCK", "0x3A": "F1", "0x3B": "F2", "0x3C": "F3",
                     "0x3D": "F4", "0x3E": "F5", "0x3F": "F6", "0x40": "F7", "0x41": "F8", "0x42": "F9", "0x43": "F10",
                     "0x44": "F11", "0x45": "F12", "0x46": "PRINTSCREEN", "0x47": "SCROLL_LOCK", "0x48": "PAUSE",
                     "0x49": "INSERT", "0x4A": "HOME", "0x4B": "PAGE_UP", "0x4C": "DELETE", "0x4D": "END",
                     "0x4E": "PAGE_DOWN", "0x4F": "RIGHT", "0x50": "LEFT", "0x51": "DOWN", "0x52": "UP",
                     "0x53": "NUM_LOCK", "0x54": "PAD_SLASH", "0x55": "PAD_ASTERIX", "0x56": "PAD_MINUS",
                     "0x57": "PAD_PLUS", "0x58": "PAD_ENTER", "0x59": "PAD_1", "0x5A": "PAD_2", "0x5B": "PAD_3",
                     "0x5C": "PAD_4", "0x5D": "PAD_5", "0x5E": "PAD_6", "0x5F": "PAD_7", "0x60": "PAD_8",
                     "0x61": "PAD_9", "0x62": "PAD_0", "0x63": "PAD_PERIOD", "0x64": "EUROPE_2", "0x65": "APP",
                     "0x66": "POWER", "0x67": "PAD_EQUALS", "0x68": "F13", "0x69": "F14", "0x6A": "F15", "0x6B": "F16",
                     "0x6C": "F17", "0x6D": "F18", "0x6E": "F19", "0x6F": "F20", "0x70": "F21", "0x71": "F22",
                     "0x72": "F23", "0x73": "F24", "0x74": "EXECUTE", "0x75": "HELP", "0x76": "MENU", "0x77": "SELECT",
                     "0x78": "STOP", "0x79": "AGAIN", "0x7A": "UNDO", "0x7B": "CUT", "0x7C": "COPY", "0x7D": "PASTE",
                     "0x7E": "FIND", "0x7F": "MUTE", "0x80": "VOLUME_UP", "0x81": "VOLUME_DOWN",
                     "0x82": "LOCKING_CAPS_LOCK", "0x83": "LOCKING_NUM_LOCK", "0x84": "LOCKING_SCROLL_LOCK",
                     "0x85": "PAD_COMMA", "0x86": "EQUAL_SIGN", "0x87": "INTERNATIONAL_1", "0x88": "INTERNATIONAL_2",
                     "0x89": "INTERNATIONAL_3", "0x8A": "INTERNATIONAL_4", "0x8B": "INTERNATIONAL_5",
                     "0x8C": "INTERNATIONAL_6", "0x8D": "INTERNATIONAL_7", "0x8E": "INTERNATIONAL_8",
                     "0x8F": "INTERNATIONAL_9", "0x90": "LANG_1", "0x91": "LANG_2", "0x92": "LANG_3", "0x93": "LANG_4",
                     "0x94": "LANG_5", "0x95": "LANG_6", "0x96": "LANG_7", "0x97": "LANG_8", "0x98": "LANG_9",
                     "0x99": "ALTERNATE_ERASE", "0x9A": "SYSREQ_ATTN", "0x9B": "CANCEL", "0x9C": "CLEAR",
                     "0x9D": "PRIOR", "0x9E": "RETURN", "0x9F": "SEPARATOR", "0xA0": "OUT", "0xA1": "OPER",
                     "0xA2": "CLEAR_AGAIN", "0xA3": "CRSEL_PROPS", "0xA4": "EXSEL", "0xA8": "SYSTEM_POWER",
                     "0xA9": "SYSTEM_SLEEP", "0xAA": "SYSTEM_WAKE", "0xAB": "AUX1", "0xAC": "AUX2", "0xAD": "AUX3",
                     "0xAE": "AUX4", "0xAF": "AUX5", "0xB1": "EXTRA_LALT", "0xB2": "EXTRA_PAD_PLUS",
                     "0xB3": "EXTRA_RALT", "0xB4": "EXTRA_EUROPE_2", "0xB5": "EXTRA_BACKSLASH", "0xB6": "EXTRA_INSERT",
                     "0xB7": "EXTRA_F1", "0xB8": "EXTRA_F2", "0xB9": "EXTRA_F3", "0xBA": "EXTRA_F4", "0xBB": "EXTRA_F5",
                     "0xBC": "EXTRA_F6", "0xBD": "EXTRA_F7", "0xBE": "EXTRA_F8", "0xBF": "EXTRA_F9",
                     "0xC0": "EXTRA_F10", "0xC2": "EXTRA_SYSRQ", "0xD0": "FN1", "0xD1": "FN2", "0xD2": "FN3",
                     "0xD3": "FN4", "0xD4": "FN5", "0xD5": "FN6", "0xD6": "FN7", "0xD7": "FN8", "0xD8": "SELECT_0",
                     "0xD9": "SELECT_1", "0xDA": "SELECT_2", "0xDB": "SELECT_3", "0xDC": "SELECT_4", "0xDD": "SELECT_5",
                     "0xDE": "SELECT_6", "0xDF": "SELECT_7", "0xE0": "LCTRL", "0xE1": "LSHIFT", "0xE2": "LALT",
                     "0xE3": "LGUI", "0xE4": "RCTRL", "0xE5": "RSHIFT", "0xE6": "RALT", "0xE7": "RGUI",
                     "0xE8": "MEDIA_NEXT_TRACK", "0xE9": "MEDIA_PREV_TRACK", "0xEA": "MEDIA_STOP",
                     "0xEB": "MEDIA_PLAY_PAUSE", "0xEC": "MEDIA_MUTE", "0xED": "MEDIA_BASS_BOOST",
                     "0xEE": "MEDIA_LOUDNESS", "0xEF": "MEDIA_VOLUME_UP", "0xF0": "MEDIA_VOLUME_DOWN",
                     "0xF1": "MEDIA_BASS_UP", "0xF2": "MEDIA_BASS_DOWN", "0xF3": "MEDIA_TREBLE_UP",
                     "0xF4": "MEDIA_TREBLE_DOWN", "0xF5": "MEDIA_MEDIA_SELECT", "0xF6": "MEDIA_MAIL",
                     "0xF7": "MEDIA_CALCULATOR", "0xF8": "MEDIA_MY_COMPUTER", "0xF9": "MEDIA_WWW_SEARCH",
                     "0xFA": "MEDIA_WWW_HOME", "0xFB": "MEDIA_WWW_BACK", "0xFC": "MEDIA_WWW_FORWARD",
                     "0xFD": "MEDIA_WWW_STOP", "0xFE": "MEDIA_WWW_REFRESH", "0xFF": "MEDIA_WWW_FAVORITES"}

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("EasyHIDListen")
    print("EasyHIDListen - Created by Adam Brewer\n")
    process = subprocess.Popen([resource_path('rsc/hid_listen.exe')], stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            outstr = output.strip().decode('utf-8').split(' ')
            for i in range(0, len(outstr)):
                a = outstr[i][1:]
                trr = ''
                if '+' in outstr[i]:
                    tr = a.upper()
                    if i+1 != len(outstr) and 'd' in outstr[i+1]:
                        trr = outstr[i+1][1:]
                    print(f"PRESS\t||\tcode={tr}\ttranslation={translation_table['0x'+tr]}\t"+(f"\ttranslation_remapping={translation_table['0x'+trr]}" if trr and tr != trr else ""))
        rc = process.poll()
    process.kill()

if __name__=="__main__":
    main()
