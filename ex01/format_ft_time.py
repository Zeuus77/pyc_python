from datetime import datetime

now = datetime.now()
M_seconds = datetime.now().timestamp() * 1000

formatted = now.strftime("%B-%d-%Y :")
datee = now.strftime("%B %m %Y")
print("Seconds since",formatted,f"{M_seconds:,.4f}","or",f"{M_seconds:.2e}"," in scientific notation")
print(datee)