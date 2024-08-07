import pyautogui
import time

#user input
host_name = input("Enter the Asset number of the device you want to image: ").upper()
mac_address = input("Enter the Mac Address of the device you want to image: ").upper()


# Wait a moment before starting
time.sleep(2)
# Locate the DSM Explorer icon on the taskbar
dsm_icon_pos = pyautogui.locateOnScreen('dsm.png', confidence=0.95)
if dsm_icon_pos:
   # Calculate the center position of the icon
   x = dsm_icon_pos.left + dsm_icon_pos.width / 2
   y = dsm_icon_pos.top + dsm_icon_pos.height / 2
   # Move to the center of the icon and click it
   pyautogui.moveTo(x, y, duration=0.5)
   pyautogui.click()
   print("DSM Explorer activated.")
else:
   print("DSM Explorer icon not found on the screen.")
# Allow some time for the window to activate
time.sleep(1)


# Locate the "All Computers" element on the screen
element_position = pyautogui.locateOnScreen('all_computers.png', confidence=0.7)

if element_position:
    # Get the center of the bounding box
    x, y = pyautogui.center(element_position)

    # Move to the center and right-click
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.rightClick()
    print("Right-clicked on 'All Computers'.")

    # Short delay to ensure menu is open
    time.sleep(1)

    # Press down arrow to navigate to "New Computer"
    pyautogui.press('down', presses=3)  # Adjust if "New Computer" isn't the first option
    pyautogui.press('enter')  # Select the option

    time.sleep(2)

    pyautogui.press('enter') # to open asset number

    #Host name
    pyautogui.write(host_name.upper(), interval=0.1)
    pyautogui.press('tab')
    #System address
    pyautogui.write(host_name.upper(), interval=0.1)
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.write(mac_address.upper(), interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('down', presses=2)
    pyautogui.press('enter')
    pyautogui.press('down', presses=2)
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('space')
    pyautogui.press('down', presses=2)
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('space')
    pyautogui.press('enter', presses=3)


else:
    print("'All computers'  not found on screen")

# Add a small delay before the search operation
time.sleep(7)

# Locate the "Name" image on the screen
name_pos = pyautogui.locateOnScreen('Name.png', confidence=0.7)  # Ensure 'Name.png' is the screenshot of the "Name" label

if name_pos:
    # Calculate offset positions
    offset_x = 50  # Adjust this value as needed for right offset
    offset_y = 20  # Adjust this value as needed for down offset

    # Move to the offset position
    x, y = name_pos.left + offset_x, name_pos.top + offset_y
    pyautogui.moveTo(x, y, duration=0.5)

    # Click on the "Name" field
    pyautogui.click()

    # Clear the current text
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    # Type the asset number into the "Name" field
    pyautogui.write(host_name, interval=0.1)

    # Press Enter to perform the search
    pyautogui.press('enter')
else:
    print("'Name' field not found on the screen.")

# Ensure the system is ready after performing the search
time.sleep(5)

# Locate the "Name" label on the screen
name_pos = pyautogui.locateOnScreen('Name2.png', confidence=0.7)  # Ensure 'Name2.png' is the correct screenshot of the "Name" label

if name_pos:
    # Calculate offset positions to target the computer listing accurately
    offset_x = 40   # Adjust this value as needed for the horizontal offset
    offset_y = 30  # Adjust this value as needed for the vertical offset to reach the computer listing

    # Calculate the target position
    x, y = name_pos.left + offset_x, name_pos.top + offset_y

    # Move to the offset position
    pyautogui.moveTo(x, y, duration=0.5)

    # Double-click to open the computer details
    pyautogui.doubleClick()

    print("Double-clicked on the computer listing.")
else:
    print("'Name' label not found on the screen.")

    # Ensure the system is ready after double-clicking the computer
time.sleep(3)  # Adjust the sleep time as needed

# Locate the "Details" button on the screen
details_pos = pyautogui.locateOnScreen('Details.png', confidence=0.7)

if details_pos:
    # Move to the "Details" button and click it
    pyautogui.moveTo(details_pos.left + details_pos.width / 2, details_pos.top + details_pos.height / 2, duration=0.5)
    pyautogui.click()
    print("Clicked on 'Details'.")

    # Add a delay to allow the next screen to load
    time.sleep(1)

    # Locate the "OS Installation Parameters" button on the screen
    os_params_pos = pyautogui.locateOnScreen('Os.png', confidence=0.7)

    if os_params_pos:
        # Move to the "OS Installation Parameters" button and click it
        pyautogui.moveTo(os_params_pos.left + os_params_pos.width / 2, os_params_pos.top + os_params_pos.height / 2, duration=0.5)
        pyautogui.click()
        print("Clicked on 'OS Installation Parameters'.")
    else:
        print("'OS Installation Parameters' button not found on the screen.")
else:
    print("'Details' button not found on the screen.")

# Add a delay to ensure the previous actions are complete and the screen is ready
time.sleep(2)

# Locate the "BootSpecial" icon on the screen
bootspecial_pos = pyautogui.locateOnScreen('BootSpecial.png', confidence=0.7)

if bootspecial_pos:
    # Move to the center of the "BootSpecial" icon
    pyautogui.moveTo(bootspecial_pos.left + bootspecial_pos.width / 2, bootspecial_pos.top + bootspecial_pos.height / 2, duration=0.5)
    
    # Double-click the "BootSpecial" icon
    pyautogui.doubleClick()
    print("Double-clicked on 'BootSpecial'.")
else:
    print("'BootSpecial' icon not found on the screen.")

time.sleep(2)
pyautogui.press('enter')

time.sleep(2)

# Locate the "OS Installation Parameters" icon on the screen
os_installation_params_pos = pyautogui.locateOnScreen('Os2.png', confidence=0.7)

if os_installation_params_pos:
    # Calculate the center position of the icon
    x = os_installation_params_pos.left + os_installation_params_pos.width / 2
    y = os_installation_params_pos.top + os_installation_params_pos.height / 2

    # Move to the center of the icon
    pyautogui.moveTo(x, y, duration=0.5)

    # Right-click the "OS Installation Parameters" icon
    pyautogui.rightClick()
    print("Right-clicked on 'OS Installation Parameters'.")
    pyautogui.press('down', presses=7)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=4)
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('enter')
else:
    print("'OS Installation Parameters' icon not found on the screen.")

    