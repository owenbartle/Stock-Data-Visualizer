
class UserInputs:

    # Select Chart Type - Complete
    def selectChartType():

        print("\nChart Types:\n---------------------\n\t1. Bar\n\t2. Line")

        while (True):

            chartType = input("Enter the type (1, 2): ")

            if (chartType == '1' or chartType == '2'):
                chartType = int(chartType)
                return chartType
            
            else:
                print("Must choose a valid type (1. Bar Graph | 2. Line Graph)")

