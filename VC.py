class L:
    isDirty = True

class R:
    isDirty = True

while True:
    if L.isDirty:
        L.isDirty = False
        print("moving to right other room")
    if R.isDirty:
        R.isDirty = False
        print("moving to left other room")
    if not L.isDirty and not R.isDirty:
        print("done")
        break
