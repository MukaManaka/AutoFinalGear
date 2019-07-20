import os
import sys
import shutil

def dump_device_info():
    """
    显示设备信息
    """
    size_str = os.popen('adb shell wm size').read()
    device_str = os.popen('adb shell getprop ro.product.device').read()
    phone_os_str = os.popen('adb shell getprop ro.build.version.release').read()
    density_str = os.popen('adb shell wm density').read()
    print("""**********
        Screen: {size}
        Density: {dpi}
        Device: {device}
        Phone OS: {phone_os}
        Host OS: {host_os}
        Python: {python}
        **********""".format(
        size=size_str.strip(),
        dpi=density_str.strip(),
        device=device_str.strip(),
        phone_os=phone_os_str.strip(),
        host_os=sys.platform,
        python=sys.version
    ))

if __name__ == '__main__':
    dump_device_info()