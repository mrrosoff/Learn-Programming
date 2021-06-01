import pandas
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Sometimes you are going to want to do data analysis. Pandas is your friend!!!

    # The import line above will probably be red. Import pandas by rolling over it and clicking install!

    # Here I am reading a file into a dataframe. I asked for the read_csv method, but pandas can read other types too!

    df = pandas.read_csv('../../Chapter2/Tests/Mauna-Loa-Data.txt')

    # The result is kinda bad, seems like we need to add a few things, na_values marks bad data

    df = pandas.read_csv('../../Chapter2/Tests/Mauna-Loa-Data.txt',
                         header=None, delim_whitespace=True,
                         na_values=["-99999", "-9999.0", "-9999", "-99.000", "-99.00"])

    # Better this time, the lack of headers is sad though, lets label them. Taking from Chapter Two...

    df.columns = ["WBAN Number", "UTC Date", "UTC Time", "(LST) Beginning", "(LST) End", "VN", "Longitude", "Latitude",
                  "Average Temperature (C)", "Total Precipitation (mm)",
                  "Average Global Solar Radiation (watts/meter^2)", "QC Flag (AGSR)",
                  "Average Infrared Surface Temperature (C)", "Type of Infrared Surface Temperature Measurement",
                  "QC Flag (ST)", "Relative Humidity AveragTotal Precipitation (mm)e (%)", "QC Flag (RH)",
                  "Average Soil Moisture (m^3/m^3)", "Average Soil Temperature (C)",
                  "Presence or Absence of Moisture (Ohms)", "QC Flag (W)", "Average Wind Speed (m/s)", "QC flag (WS)"]

    # Get rid of bad data

    df.drop(columns=["Average Soil Moisture (m^3/m^3)", "Average Soil Temperature (C)"], inplace=True)
    df = df.dropna()

    # Better

    # Convert to Numpy Array

    data = df.iloc[:, :].values

    # Lets Plot it! Use MatPlotLib!

    plt.plot(data[:, 2], data[:, 8], 'o')
    plt.xlabel('UTC Time')
    plt.ylabel('Average Temperature (C)')

    plt.show()
