def read_csv(fileName):
    resultList = []
    with open(fileName) as file:
        for line in file.readlines():
            newLine = line.strip('\n')
            # print(newLine)
            # print(list)
            resultList.append(newLine)
        print(resultList)
        return resultList


def csv_files(csv):
    csvFilesList = []
    maxLines = 3000
    totalLines = len(csv)
    numFiles = totalLines / maxLines
    if not numFiles.is_integer():
        numFiles = int(numFiles) + 1
    for ii in range(1, numFiles + 1):
        file = 'csv_file_' + str(ii) + '.csv'
        # print(file)  # csv_file_ii.csv
        csvFilesList.append(file)
    return csvFilesList


def csv_splitter(csv):
    fileArray = []
    count = 0
    maxLines = 3000
    endIndex = 3001
    startIndex = 1
    totalLines = len(csv)
    csvFiles = csv_files(csv)  # returns array of files
    header = csv[0]
    for file in csvFiles:  # for each file in array
        print(file)
        with open(file, 'w') as fh:  # open file
            fh.write(header + '\n')
            print('top - startIndex:', startIndex)
            print('top - endIndex:', endIndex)
            for ii in range(startIndex, endIndex):  # start at startIndex go to maxLines
                fh.write(str(csv[ii]) + '\n')
                count += 1  # increment count
            startIndex = endIndex
            if (totalLines - count) < maxLines:
                endIndex = totalLines
            else:
                endIndex += maxLines
        fileArray.append(file)
    return fileArray


def main(fileName):
    csvList = read_csv(fileName)
    header = csvList[0]
    # max_num_files(csvList)
    xx = csv_splitter(csvList)
    print(xx)


if __name__ == '__main__':
    main('temp.csv')


