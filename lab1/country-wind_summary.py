# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# country-wind_summary.py
# Created on: 2018-09-28 10:57:13.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Local variables:
in_countries = "H:\\ESM267\\lab1\\raw\\ne_10m_admin_0_countries.shp"
out_countries = "H:\\ESM267\\lab1\\lab1.gdb\\countries"
countries = out_countries

# Process: Copy Features
arcpy.CopyFeatures_management(in_countries, out_countries, "", "0", "0", "0")

# local variables: for cell statistics
    #s_0_tif = "H:\\ESM267\\lab1\\out\\s_0.tif"
    #s_120_tif = "H:\\ESM267\\lab1\\out\\s_120.tif"
    #s_150_tif = "H:\\ESM267\\lab1\\out\\s_150.tif"
    #s_180_tif = "H:\\ESM267\\lab1\\out\\s_180.tif"
    #s_210_tif = "H:\\ESM267\\lab1\\out\\s_210.tif"
    #s_240_tif = "H:\\ESM267\\lab1\\out\\s_240.tif"
    #s_270_tif = "H:\\ESM267\\lab1\\out\\s_270.tif"
    #s_30_tif = "H:\\ESM267\\lab1\\out\\s_30.tif"
    #s_300_tif = "H:\\ESM267\\lab1\\out\\s_300.tif"
    #s_330_tif = "H:\\ESM267\\lab1\\out\\s_330.tif"
    #s_360_tif = "H:\\ESM267\\lab1\\out\\s_360.tif"
    #s_60_tif = "H:\\ESM267\\lab1\\out\\s_60.tif"
    #s_90_tif = "H:\\ESM267\\lab1\\out\\s_90.tif"
    #s_avg_tif = "H:\\ESM267\\lab1\\out\\s_avg.tif"
    #s_countries = "H:\\ESM267\\lab1\\lab1.gdb\\s_countries"

# Process: Cell Statistics
#arcpy.gp.CellStatistics_sa("H:\\ESM267\\lab1\\out\\s_0.tif;H:\\ESM267\\lab1\\out\\s_120.tif;H:\\ESM267\\lab1\\out\\s_150.tif;H:\\ESM267\\lab1\\out\\s_180.tif;H:\\ESM267\\lab1\\out\\s_210.tif;H:\\ESM267\\lab1\\out\\s_240.tif;H:\\ESM267\\lab1\\out\\s_270.tif;H:\\ESM267\\lab1\\out\\s_30.tif;H:\\ESM267\\lab1\\out\\s_300.tif;H:\\ESM267\\lab1\\out\\s_330.tif;H:\\ESM267\\lab1\\out\\s_360.tif;H:\\ESM267\\lab1\\out\\s_60.tif;H:\\ESM267\\lab1\\out\\s_90.tif", s_avg_tif, "MEAN", "DATA")
s_tifs = ["h:\\ESM267\\lab1\\out\\s_%03d.tif" % j for j in range(0, 365, 30)]

arcpy.gp.CellStatistics_sa(s_tifs, s_avg_tif, "MEAN", "DATA")

# Process: Zonal Statistics as Table
arcpy.gp.ZonalStatisticsAsTable_sa(out_countries, "NAME", s_avg_tif, s_countries, "DATA", "MIN_MAX_MEAN")

# Process: Join Field
arcpy.JoinField_management(out_countries, "NAME", s_countries, "NAME", "Min;Max;Mean")

