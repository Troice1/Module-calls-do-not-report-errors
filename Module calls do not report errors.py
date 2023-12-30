import os

# Function body
def ImportModule(name: str):
    while True:
        try:
            return __import__(name)
        except:
            print("Not have the module,start downloads")
            os.popen(f'pip install {str(name)}').read()

# Call, Variable names can be changed by oneself
requests = ImportModule("requests")

if requests:
    print("Import successful")
    print(requests)
else:
    print("Import fail")

