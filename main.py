import csv

if __name__ == '__main__':

    exampleFile = open('Badprice.csv', 'rU')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    #print(exampleData)
    #for row in exampleData:
        #print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

    maxt = 0.0
    mint = 0.0
    square_sum = 0
    price_sum = 0
    row_count = len(exampleData) - 1

    for line in exampleData:
        #print(line)
        # to find max, min price
            try:
                p = float(line[9])
            except ValueError:
                continue
            maxt = max(maxt,p)
            if mint == 0.0:
                mint = p
            else:
                mint = min(mint,p)

        # to find average sq ft
            try:
                i = float(line[6])
            except ValueError:
                continue
            square_sum += i

            try:
                j = float(line[9])
            except ValueError:
                continue
            price_sum += j


    print("Maximum:",maxt)
    print("Minimum:",mint)
    print("Average Square Foot:", square_sum / row_count)
    print("Average Price:", price_sum / row_count)
