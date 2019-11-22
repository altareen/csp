def generatechord(root, progression):
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    chords = {"Major":[4, 7], "Minor":[3, 7], "Augemented fifth":[4, 8], "Minor fifth":[4, 6], "Major sixth":[4, 7, 9]}
    notes = []
    notes.append(root)
    base = scale.index(root)
    steps = chords[progression]
    for num in steps:
        offset = (base+num)%12
        notes.append(scale[offset])
    return notes

result = generatechord("B", "Major sixth")
print(result)
