class sendInfo:
    hoursWorked = []
    hoursWorkedStr = []
    location = []
    daysWorked = []
    monthNum = None
    halfValNum = None
    dateRangeStr = None
    tableString = ""
    allInfo = dict()
    subjectString =  ""
  

    def __init__(self):
        print("Time to  enter your hours!", end="\n\n")
        self.monthNum = int(input("Which month? "))
        self.halfValNum = int(input("Which half of the month is it? "))
        self.dateRangeStr = self.getDateRange()
        print()

        keepGoing = True

        while(keepGoing):
            self.daysWorked.append(int(input("Which day did you work? ")))
            workedTemp = input("What hours did you work that day? ")
            self.hoursWorkedStr.append(workedTemp)
            self.hoursWorked.append(self.calculateHours(workedTemp))
            self.location.append("Chino" if input("Chino (c) or Diamond Bar (d)? ")=="c" else "Diamond Bar")  
            goAgainInput = input("Would you like enter another date? ")
            if goAgainInput.lower() == "n":
                keepGoing = False
            print()

        self.allInfo = {1: self.daysWorked, 2: self.hoursWorked, 3:self.hoursWorkedStr, 4:self.location}
        self.tableString = self.generateTable()
        

    def calculateHours(self, hoursString):
        tempArr = hoursString.split("-")
        returnArr = [int(numericStr) for numericStr in tempArr]
        if returnArr[1]<= 6:
            return (returnArr[1] + 12) - returnArr[0]
        else:
            return returnArr[1] - returnArr[0]

    def getDateRange(self):
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        monthStr = months[self.monthNum - 1]
        if self.halfValNum == 1: 
            self.subjectString = f"{self.monthNum}/1 - {self.monthNum}/15"
            return f"{monthStr} 1 through {monthStr} 15"
        else: 
            endVals = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
            self.subjectString = f"{self.monthNum}/16 - {self.monthNum}/{endVals[monthStr]}"
            return f"{monthStr} 16 through {monthStr} {endVals[monthStr]}"

    def generateTable(self):
        returnString = ""
        rowStart = "<tr>"
        rowEnd = "</tr>"
        dataStart = "<td style=\"border: 1px solid black; border-collapse: collapse;\">"
        dataEnd = "</td>"
        for i in range(len(self.daysWorked)):
            returnString += rowStart
            for j in range(1, 5):
                returnString += dataStart
                returnString += f"{self.allInfo[j][i]}"
                returnString += dataEnd
            returnString += rowEnd
        return returnString