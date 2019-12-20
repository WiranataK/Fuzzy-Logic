import csv
import pandas as pd

def bacafile():
    with open('influencers.csv', 'r') as file:
        reader = csv.reader(file)
        array = []
        line = 0
        for row in reader:
            if line != 0:
                row[1] = int(row[1])
                row[2] = float(row[2])
                array.append(row)
            line +=1
    return array

def fuzifikasifollowers(arrayinfluencers):
    line = 0
    for row in arrayinfluencers:
        newfollower = []
        f = float(row[1])
        if row[1] <= 30000:
            newfollower.extend((1, 0, 0))
        elif row[1] <= 35000 and row[1] > 30000:
            newfollower.extend(((35000 - f) / (35000 - 30001), (f - 30001) / (35000 - 30001), 0))
        elif row[1] > 35000 and row[1] <= 65000:
            newfollower.extend((0, 1, 0))
        elif row[1] <= 70000 and row[1] > 65000:
            newfollower.extend((0, (70000 - f) / (70000 - 65001), (f - 65001) / (70000 - 65001)))
        elif row[1] > 70000:
            newfollower.extend((0, 0, 1))  
        row.append(newfollower)

def fuzifikasiengagement(arrayinfluencers):
    for row in arrayinfluencers:
        newfollower = []
        if row[2] <= 3:
            newfollower.extend((1, 0, 0))
        elif row[2] <= 3.5 and row[2] > 3:
            newfollower.append((3.5 - row[2]) / (3.5 - 3.01))
            newfollower.append((row[2] - 3.01) / (3.5 - 3.01))
            newfollower.append(0)
        elif row[2] > 3.5 and row[2] <= 6.5:
            newfollower.extend((0, 1, 0))
        elif row[2] <= 7 and row[2] > 6.5:
            newfollower.append(0)
            newfollower.append((7 - row[2]) / (7 - 6.51))
            newfollower.append((row[2] - 6.51) / (7 - 6.51))
        elif row[2] > 7:
            newfollower.extend((0, 0, 1))
        row.append(newfollower)

def inferensi(arrayinfluencers):
    for row in arrayinfluencers:
        newfollower = []
        nano = max(min(row[3][0], row[4][0]), min(row[3][0], row[4][1]), min(row[3][1], row[4][0]))
        micro = max(min(row[3][0], row[4][2]), min(row[3][1], row[4][1]), min(row[3][2], row[4][0]))
        medium = max(min(row[3][1], row[4][2]), min(row[3][2], row[4][1]), min(row[3][2], row[4][2]))
        newfollower.extend((nano, micro, medium))
        row.append(newfollower)

def defuzifikasiutama(arrayinfluencers):
    for row in arrayinfluencers:
        defuzifikasi = ((row[5][2] * 75) + (row[5][1] * 50) + (row[5][0] * 25)) / (row[5][0] + row[5][1] + row[5][2])
        row.append(defuzifikasi)

def selection_sort(arrayinfluencers):
    # This value of i corresponds to how many values were sorted
    for i in range(len(arrayinfluencers)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(arrayinfluencers)):
            if arrayinfluencers[j][6] > arrayinfluencers[lowest_value_index][6]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        arrayinfluencers[i], arrayinfluencers[lowest_value_index] = arrayinfluencers[lowest_value_index], arrayinfluencers[i]  

def main():
    influencersarray = bacafile()
    fuzifikasifollowers(influencersarray)
    fuzifikasiengagement(influencersarray)
    inferensi(influencersarray)
    defuzifikasiutama(influencersarray)
    selection_sort(influencersarray)

    for i in influencersarray[0:20]:
        print(i)
        
    df = pd.DataFrame(influencersarray[0:20])
    filecsv = df.to_csv('chosen.csv', index = False)

if __name__ == "__main__":
    main()