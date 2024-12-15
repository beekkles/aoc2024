import os

for i in range(1, 26):
    dfolder = os.path.join(".", f"{i:02}")
    os.makedirs(dfolder, exist_ok=True)

    open(os.path.join(dfolder, "input.txt"), "w").close()
    open(os.path.join(dfolder, "test1.txt"), "w").close()
    open(os.path.join(dfolder, "test2.txt"), "w").close()
    open(os.path.join(dfolder, "solve.py"), "w").close()
