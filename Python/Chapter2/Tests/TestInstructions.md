
#Test Instructions

## Background 
The file Mauna-Loa-Data.txt is included inside of this directory. The file has the following fields in the following 
order, one row is one entry. Each entry corresponds to a five minute interval at Mauna-Loa in Hawaii over an entire 
year.

1. The station WBAN number.
2. The UTC date of the observation.
3. The UTC time at the end of the 5-minute observation period. For example, 0420 designates the observational
period starting just after 0415 and ending at 0420; and 0000 designates the last 5-minute period of the previous day.
4. The Local Standard Time (LST) date of the observation.
5. The Local Standard Time (LST) time at the end of the 5-minute period.
6. The version number of the station datalogger program that was in effect at the time of the observation.
Note: This field should be treated as text (i.e. string).
7. Station longitude, using WGS-84.
8. Station latitude, using WGS-84.
9. Average temperature, in degrees C.
10. Total amount of precipitation, in mm.
11. Average global solar radiation received, in watts/meter^2.
12. QC flag for the average global solar radiation measurement.
13. Average infrared surface temperature, in degrees C.
14. The type of infrared surface temperature measurement: 'R' denotes raw (uncorrected); 'C' denotes corrected;
and 'U' is shown if the type is unknown/missing.
15. QC flag for the surface temperature measurement.
 Relative humidity average, as a percentage.
16. QC flag for the relative humidity measurement.
17. Average soil moisture (volumetric water content in m^3/m^3) at 5cm below the surface.
18. Average soil temperature at 5 cm below the surface, in degrees C.
19. The presence or absence of moisture due to precipitation, in Ohms. High values (>= 1000) indicate an
absence of moisture.  Low values (< 1000) indicate the presence of moisture.
20. QC flag for the wetness measurement.
21. Average wind speed, in meters per second, at a height of 1.5 meters.
22. QC flag for the wind speed measurement.

## Your Task

Print out the following values:

1. The average temperature over the entire year
2. The largest reading of global solar radiation
3. The smallest reading of wind speed
4. The standard derivative of the samples infrared surface temperature

