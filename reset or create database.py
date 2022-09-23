import numpy as np

## First we have to make file to store all the names and numbers
a = np.array(['NAME:-','No.:-'])

## Saving this file
np.save("Contacts",a)

## After running the file.py a contacts.npy is created