from django.db import models

# Create your models here.


class Question(models.Model):

    def __str__(self):
        return self.DOT_Number

    DOT_Number = models.CharField(max_length=10, primary_key=True)#q.DOT_Number = tr[25].contents[3].get_text()
    Entity_Type = models.CharField(max_length=200)#18
    Operating_Status = models.CharField(max_length=200)#tr[19].get_text()
    Legal_Name = models.CharField(max_length=200)#q= Question(Address = tr[20].get_text())

    Phone = models.CharField(max_length=15)# tr[23].contents[3].get_text()
    Address = models.CharField(max_length=200)# tr[24].contents[3].get_text()

    Units = models.CharField(max_length=10)#tr[27].contents[3].get_text()
    Drivers = models.CharField(max_length=10)#tr[27].contents[7].get_text()
    Mileage = models.CharField(max_length=200)


    For_Hire = models.CharField(max_length=200)
    Exempt_For_Hire = models.CharField(max_length=200)
    Private_Property = models.CharField(max_length=200)
    Priv_Pass = models.CharField(max_length=200)
    Priv_Pass_Non = models.CharField(max_length=200)
    Migrant = models.CharField(max_length=200)
    US_Mail = models.CharField(max_length=200)
    Fed_Gov = models.CharField(max_length=200)
    State_Gov = models.CharField(max_length=200)
    Local_Gov = models.CharField(max_length=200)
    Indian_Nation = models.CharField(max_length=200)


    Interstate = models.CharField(max_length=200)
    Intrastate_Only_HM = models.CharField(max_length=200)
    Intrastate_NonHM = models.CharField(max_length=200)

    General_Freight = models.CharField(max_length=200)
    Household_Goods = models.CharField(max_length=200)
    Metal_sheets_coils_rolls = models.CharField(max_length=200)
    Motor_Vehicles = models.CharField(max_length=200)
    DriveTow_away = models.CharField(max_length=200)
    Logs_Poles_Beams_Lumber = models.CharField(max_length=200)
    Building_Materials = models.CharField(max_length=200)
    Mobile_Homes = models.CharField(max_length=200)
    Machinery_Large_Objects = models.CharField(max_length=200)
    Fresh_Produce = models.CharField(max_length=200)

    LiquidsGases = models.CharField(max_length=200)
    Intermodal_Cont = models.CharField(max_length=200)
    Passengers = models.CharField(max_length=200)
    Oilfield_Equipment = models.CharField(max_length=200)
    Livestock = models.CharField(max_length=200)
    Grain_Feed_Hay = models.CharField(max_length=200)
    CoalCoke = models.CharField(max_length=200)
    Meat = models.CharField(max_length=200)
    GarbageRefuse = models.CharField(max_length=200)
    US_Mail = models.CharField(max_length=200)

    Chemicals = models.CharField(max_length=200)
    Commodities_Dry_Bulk = models.CharField(max_length=200)
    Refrigerated_Food = models.CharField(max_length=200)
    Beverages = models.CharField(max_length=200)
    Paper_Products = models.CharField(max_length=200)
    Utilities = models.CharField(max_length=200)
    AgriculturalFarm_Supplies = models.CharField(max_length=200)
    Construction = models.CharField(max_length=200)
    Water_Well = models.CharField(max_length=200)

class Query(models.Model):

    def __str__(self):
        return self.DOT_Number
    fields = models.CharField(max_length=200)
