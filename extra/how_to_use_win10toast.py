from win10toast import ToastNotifier
# Make a variable called toast:
toast = ToastNotifier()
# Show the toast variable:
toast.show_toast(
    "Notification",
    "Notification body",
    duration = 20,
    icon_path = "icon.ico",
    threaded = True,
    # When threading is enabled, the rest of your program will be allowed to execute while the toast is still active. Otherwise, your program will wait until the toast has completed before continuing.
)