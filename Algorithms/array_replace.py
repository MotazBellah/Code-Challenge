def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i, v in enumerate(inputArray):
        if v == elemToReplace:
            inputArray[i] = substitutionElem

    return inputArray
