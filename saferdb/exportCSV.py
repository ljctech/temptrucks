
import csv


def export_csv(q):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow([
    'DOT Number',
    'Legal Name',     'Address',     'Phone',     'Entity Type',     'Units',     'Drivers',
    'For Hire', 'Exempt For Hire', 'Private Property', 'Priv Pass', 'Priv Pass Non',
    'Migrant', 'US Mail', 'Fed Gov', 'State Gov', 'Local Gov', 'Indian Nation', 'Interstate',
    'Intrastate Only HM', 'Intrastate NonHM', 'General Freight', 'Household Goods',
    'Metal sheets coils rolls', 'Motor Vehicles', 'DriveTow away',
    'Logs Poles Beams Lumber', 'Building Materials', 'Mobile Homes',
    'Machinery Large Objects', 'Fresh Produce', 'LiquidsGases', 'Intermodal Cont',
    'Passengers', 'Oilfield Equipment', 'Livestock', 'Grain Feed Hay', 'CoalCoke',
    'Meat', 'GarbageRefuse', 'Us Mail', 'Chemicals', 'Commodities Dry Bulk',
    'Refrigerated Food', 'Beverages', 'Paper Products', 'Utilities', 'AgriculturalFarm Supplies',
    'Construction', 'Water Well'])
    qlist = q.values_list(
    'DOT_Number', 'Legal_Name', 'Physical_adress', 'Phone', 'Entity_Type', 'Units', 'Drivers',
    'Auth_For_Hire', 'Exempt_For_Hire', 'Private_Property', 'Priv_Pass_Business',
    'Priv_Pass_Non_Business', 'Migrant', 'US_Mail', 'Fed_Gov', 'State_Gov', 'Local_Gov',
    'Indian_Nation', 'Interstate', 'Intrastate_Only_HM', 'Intrastate_NonHM', 'General_Freight',
    'Household_Goods', 'Metal_sheets_coils_rolls', 'Motor_Vehicles', 'DriveTow_away', 'Logs_Poles_Beams_Lumber',
    'Building_Materials', 'Mobile_Homes', 'Machinery_Large_Objects', 'Fresh_Produce',
    'LiquidsGases', 'Intermodal_Cont', 'Passengers', 'Oilfield_Equipment', 'Livestock',
    'Grain_Feed_Hay', 'CoalCoke',
    'Meat',
    'GarbageRefuse',
    'US_Mail',
    'Chemicals',
    'Commodities_Dry_Bulk',
    'Refrigerated_Food',
    'Beverages',
    'Paper_Products',
    'Utilities',
    'AgriculturalFarm_Supplies',
    'Construction',
    'Water_Well',
    )
    for entry in qlist:
        writer.writerow(entry)

    return response
