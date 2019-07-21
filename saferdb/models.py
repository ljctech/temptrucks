from django.db import models

# Create your models here.

# from django.db import models


class Question(models.Model):

    def __str__(self):
        return str(self.DOT_Number)

    def get_contact(self):
        return self.contacts.all()[0]

    DOT_Number = models.IntegerField(db_column='DOT_Number', primary_key=True)  # Field name made lowercase.
    Entity_Type = models.CharField(db_column='Entity_Type', max_length=200)  # Field name made lowercase.
    Operating_Status = models.CharField(db_column='Operating_Status', max_length=200)  # Field name made lowercase.
    Legal_Name = models.CharField(db_column='Legal_Name', max_length=200)  # Field name made lowercase.
    Phone = models.CharField(db_column='Phone', max_length=15)  # Field name made lowercase.
    Mailing_Address = models.CharField(db_column='Mailing_Address', max_length=200)  # Field name made lowercase.
    Mileage = models.CharField(db_column='Mileage', max_length=200)  # Field name made lowercase.
    Exempt_For_Hire = models.CharField(db_column='Exempt_For_Hire', max_length=200)  # Field name made lowercase.
    Private_Property = models.CharField(db_column='Private_Property', max_length=200)  # Field name made lowercase.
    Migrant = models.CharField(db_column='Migrant', max_length=200)  # Field name made lowercase.
    Fed_Gov = models.CharField(db_column='Fed_Gov', max_length=200)  # Field name made lowercase.
    State_Gov = models.CharField(db_column='State_Gov', max_length=200)  # Field name made lowercase.
    Local_Gov = models.CharField(db_column='Local_Gov', max_length=200)  # Field name made lowercase.
    Indian_Nation = models.CharField(db_column='Indian_Nation', max_length=200)  # Field name made lowercase.
    Interstate = models.CharField(db_column='Interstate', max_length=200)  # Field name made lowercase.
    Intrastate_Only_HM = models.CharField(db_column='Intrastate_Only_HM', max_length=200)  # Field name made lowercase.
    Intrastate_NonHM = models.CharField(db_column='Intrastate_NonHM', max_length=200)  # Field name made lowercase.
    General_Freight = models.CharField(db_column='General_Freight', max_length=200)  # Field name made lowercase.
    Household_Goods = models.CharField(db_column='Household_Goods', max_length=200)  # Field name made lowercase.
    Metal_sheets_coils_rolls = models.CharField(db_column='Metal_sheets_coils_rolls', max_length=200)  # Field name made lowercase.
    Motor_Vehicles = models.CharField(db_column='Motor_Vehicles', max_length=200)  # Field name made lowercase.
    DriveTow_away = models.CharField(db_column='DriveTow_away', max_length=200)  # Field name made lowercase.
    Logs_Poles_Beams_Lumber = models.CharField(db_column='Logs_Poles_Beams_Lumber', max_length=200)  # Field name made lowercase.
    Building_Materials = models.CharField(db_column='Building_Materials', max_length=200)  # Field name made lowercase.
    Mobile_Homes = models.CharField(db_column='Mobile_Homes', max_length=200)  # Field name made lowercase.
    Machinery_Large_Objects = models.CharField(db_column='Machinery_Large_Objects', max_length=200)  # Field name made lowercase.
    Fresh_Produce = models.CharField(db_column='Fresh_Produce', max_length=200)  # Field name made lowercase.
    LiquidsGases = models.CharField(db_column='LiquidsGases', max_length=200)  # Field name made lowercase.
    Intermodal_Cont = models.CharField(db_column='Intermodal_Cont', max_length=200)  # Field name made lowercase.
    Passengers = models.CharField(db_column='Passengers', max_length=200)  # Field name made lowercase.
    Oilfield_Equipment = models.CharField(db_column='Oilfield_Equipment', max_length=200)  # Field name made lowercase.
    Livestock = models.CharField(db_column='Livestock', max_length=200)  # Field name made lowercase.
    Grain_Feed_Hay = models.CharField(db_column='Grain_Feed_Hay', max_length=200)  # Field name made lowercase.
    CoalCoke = models.CharField(db_column='CoalCoke', max_length=200)  # Field name made lowercase.
    Meat = models.CharField(db_column='Meat', max_length=200)  # Field name made lowercase.
    GarbageRefuse = models.CharField(db_column='GarbageRefuse', max_length=200)  # Field name made lowercase.
    US_Mail = models.CharField(db_column='US_Mail', max_length=200)  # Field name made lowercase.
    Chemicals = models.CharField(db_column='Chemicals', max_length=200)  # Field name made lowercase.
    Commodities_Dry_Bulk = models.CharField(db_column='Commodities_Dry_Bulk', max_length=200)  # Field name made lowercase.
    Refrigerated_Food = models.CharField(db_column='Refrigerated_Food', max_length=200)  # Field name made lowercase.
    Beverages = models.CharField(db_column='Beverages', max_length=200)  # Field name made lowercase.
    Paper_Products = models.CharField(db_column='Paper_Products', max_length=200)  # Field name made lowercase.
    Utilities = models.CharField(db_column='Utilities', max_length=200)  # Field name made lowercase.
    AgriculturalFarm_Supplies = models.CharField(db_column='AgriculturalFarm_Supplies', max_length=200)  # Field name made lowercase.
    Construction = models.CharField(db_column='Construction', max_length=200)  # Field name made lowercase.
    Water_Well = models.CharField(db_column='Water_Well', max_length=200)  # Field name made lowercase.
    Auth_For_Hire = models.CharField(db_column='Auth_For_Hire', max_length=200)  # Field name made lowercase.
    City = models.CharField(db_column='City', max_length=200, db_index=True)  # Field name made lowercase.
    DBA_Name = models.CharField(db_column='DBA_Name', max_length=200)  # Field name made lowercase.
    DUNSNumber = models.CharField(db_column='DUNSNumber', max_length=200)  # Field name made lowercase.
    Granite = models.CharField(db_column='Granite', max_length=200)  # Field name made lowercase.
    MCMXFFNumber = models.CharField(db_column='MCMXFFNumber', max_length=200)  # Field name made lowercase.
    MCS150 = models.CharField(db_column='MCS150', max_length=200)  # Field name made lowercase.
    Out_Of_Service_Date = models.CharField(db_column='Out_Of_Service_Date', max_length=200)  # Field name made lowercase.
    Physical_adress = models.CharField(db_column='Physical_adress', max_length=200)  # Field name made lowercase.
    Priv_Pass_Business = models.CharField(db_column='Priv_Pass_Business', max_length=200)  # Field name made lowercase.
    Priv_Pass_Non_Business = models.CharField(db_column='Priv_Pass_Non_Business', max_length=200)  # Field name made lowercase.
    State = models.CharField(db_column='State', max_length=5, db_index=True)  # Field name made lowercase.
    StateCarrierIDNumberarrieridnumber = models.CharField(db_column='StateCarrierIDNumber', max_length=200)  # Field name made lowercase.
    US_Mail_Cargoail_cargo = models.CharField(db_column='US_Mail_Cargo', max_length=200)  # Field name made lowercase.
    ZipCode = models.CharField(db_column='ZipCode', max_length=15, db_index=True)  # Field name made lowercase.
    mCity = models.CharField(db_column='mCity', max_length=200)  # Field name made lowercase.
    mState = models.CharField(db_column='mState', max_length=5)  # Field name made lowercase.
    mZipCode = models.CharField(db_column='mZipCode', max_length=15)  # Field name made lowercase.
    Driver_Inspections = models.CharField(db_column='Driver_Inspections', max_length=200)  # Field name made lowercase.
    Driver_Out_of_service = models.CharField(db_column='Driver_Out_of_service', max_length=200)  # Field name made lowercase.
    Driver_Out_of_service_pecent = models.CharField(db_column='Driver_Out_of_service_pecent', max_length=200)  # Field name made lowercase.
    Driver_natl_average = models.CharField(db_column='Driver_natl_average', max_length=200)  # Field name made lowercase.
    Hazmat_inspections = models.CharField(db_column='Hazmat_Inspections', max_length=200)  # Field name made lowercase.
    Hazmat_out_of_service = models.CharField(db_column='Hazmat_Out_of_service', max_length=200)  # Field name made lowercase.
    Hazmat_out_of_service_pecent = models.CharField(db_column='Hazmat_Out_of_service_pecent', max_length=200)  # Field name made lowercase.
    Hazmat_natl_average = models.CharField(db_column='Hazmat_natl_average', max_length=200)  # Field name made lowercase.
    IEP_Inspections = models.CharField(db_column='IEP_Inspections', max_length=200)  # Field name made lowercase.
    IEP_Out_of_service = models.CharField(db_column='IEP_Out_of_service', max_length=200)  # Field name made lowercase.
    IEP_Oout_of_service_pecent = models.CharField(db_column='IEP_Out_of_service_pecent', max_length=200)  # Field name made lowercase.
    IEP_natl_average = models.CharField(db_column='IEP_natl_average', max_length=200)  # Field name made lowercase.
    Rating = models.CharField(db_column='Rating', max_length=200, blank=True, null=True)  # Field name made lowercase.
    Rating_Date = models.CharField(db_column='Rating_Date', max_length=200, blank=True, null=True)  # Field name made lowercase.
    Review_Date = models.CharField(db_column='Review_Date', max_length=200, blank=True, null=True)  # Field name made lowercase.
    Type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    Vehicle_Inspections = models.CharField(db_column='Vehicle_Inspections', max_length=200)  # Field name made lowercase.
    Vehicle_Out_of_service = models.CharField(db_column='Vehicle_Out_of_service', max_length=200)  # Field name made lowercase.
    Vehicle_Out_of_service_pecent = models.CharField(db_column='Vehicle_Out_of_service_pecent', max_length=200)  # Field name made lowercase.
    Vehicle_natl_average = models.CharField(db_column='Vehicle_natl_average', max_length=200)  # Field name made lowercase.
    ca_crashes_fatal = models.CharField(max_length=200, blank=True, null=True)
    ca_crashes_injury = models.CharField(max_length=200, blank=True, null=True)
    ca_crashes_total = models.CharField(max_length=200, blank=True, null=True)
    ca_crashes_tow = models.CharField(max_length=200, blank=True, null=True)
    ca_driver_Inspections = models.CharField(db_column='ca_driver_Inspections', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ca_driver_Out_of_Service = models.CharField(db_column='ca_driver_Out_of_Service', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ca_driver_Out_of_Service_Percent = models.CharField(db_column='ca_driver_Out_of_Service_Percent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ca_vahicle_Inspections = models.CharField(db_column='ca_vahicle_Inspections', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ca_vahicle_Out_of_Service = models.CharField(db_column='ca_vahicle_Out_of_Service', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ca_vahicle_Out_of_Service_Percent = models.CharField(db_column='ca_vahicle_Out_of_Service_Percent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    crashes_fatal = models.CharField(max_length=200)
    crashes_injury = models.CharField(max_length=200)
    crashes_tow = models.CharField(max_length=200)
    special = models.CharField(max_length=200)
    trcrashes_total = models.CharField(max_length=200)
    Drivers = models.IntegerField(db_column='Drivers', blank=True, null=True)  # Field name made lowercase.
    Units = models.IntegerField(db_column='Units', blank=True, null=True)  # Field name made lowercase.

class Vin(models.Model):

    def __str__(self):
        return str(self.DOT_Num)
    DOT_Num = models.ForeignKey(Question, on_delete=models.CASCADE)  # Field name made lowercase.
    vin = models.CharField(max_length=20, default='')  # Field name made lowercase.



class Dot_Contacts(models.Model):

    def __str__(self):
        return str(self.DOT_Num)
    DOT_Num = models.ForeignKey(Question, on_delete=models.CASCADE, default='99999999999', related_name = "contacts"  )  # Field name made lowercase.
    fax = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=200, default='none@none.com')


# class Contacts(models.Model):
#
#     def __str__(self):
#         return self.DOT_Number
#     DOT_Num = models.ForeignKey(Question, on_delete=models.CASCADE, default='99999999999')  # Field name made lowercase.
#     fax = models.CharField(max_length=20, default='')
#     email = models.CharField(max_length=200, default='none@none.com')

class Carrier(models.Model):
    def __str__(self):
        return str(self.DOT_Nmb)
    DOT_Nmb = models.ForeignKey(Question, on_delete=models.CASCADE)  # Field name made lowercase.
    insurance = models.CharField(max_length=200)
    renewal_date = models.DateTimeField()

class Query(models.Model):

    def __str__(self):
        return str(self.DOT_Number) or ''
    fields = models.CharField(max_length=200)


class CaliIns(models.Model):
    possibleDOT = models.IntegerField()
    legalN = models.CharField(max_length=200)
    dbaName = models.CharField(max_length=200)
    bPhone = models.CharField(max_length=20)
    insCo = models.CharField(max_length=200)
    dateEffective = models.DateField()
    workersComp = models.CharField(max_length=200)
    wcEffectiveDate = models.DateField()
    pFleet = models.IntegerField()

    forhireFleet = models.IntegerField()

class CaliIns_FK(models.Model):
    DOTNmb = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = "calins")  # Field name made lowercase.
    legalN = models.CharField(max_length=200)
    dbaName = models.CharField(max_length=200)
    bPhone = models.CharField(max_length=20)
    insCo = models.CharField(max_length=200)
    dateEffective = models.DateField()
    workersComp = models.CharField(max_length=200)
    wcEffectiveDate = models.DateField()
    pFleet = models.IntegerField()
    forhireFleet = models.IntegerField()
    renewalMonth = models.IntegerField()

class NYActiveCorp(models.Model):
    DOSID = models.IntegerField(primary_key=True)
    # DOTNmb = models.ForeignKey(Question, on_delete=models.CASCADE)
    CurrentEntityName = models.CharField(max_length=200, null=True, blank=True)
    InitialDOSFilingDate = models.CharField(max_length=200, null=True, blank=True)
    County = models.CharField(max_length=200, null=True, blank=True)
    Jurisdiction = models.CharField(max_length=200, null=True, blank=True)
    EntityType = models.CharField(max_length=200, null=True, blank=True)
    DOSProcessName = models.CharField(max_length=200, null=True, blank=True)
    DOSProcessAddress1 = models.CharField(max_length=200, null=True, blank=True)
    DOSProcessAddress2 = models.CharField(max_length=200, null=True, blank=True)
    DOSProcessCity = models.CharField(max_length=200, null=True, blank=True)
    DOSProcessState = models.CharField(max_length=200, null=True, blank=True)
    DOSProcessZip = models.CharField(max_length=200, null=True, blank=True)
    CEOName = models.CharField(max_length=200, null=True, blank=True)
    CEOAddress1 = models.CharField(max_length=200, null=True, blank=True)
    CEOAddress2 = models.CharField(max_length=200, null=True, blank=True)
    CEOCity = models.CharField(max_length=200, null=True, blank=True)
    CEOState = models.CharField(max_length=200, null=True, blank=True)
    CEOZip = models.CharField(max_length=200, null=True, blank=True)
    RegisteredAgentName = models.CharField(max_length=200, null=True, blank=True)
    RegisteredAgentAddress1 = models.CharField(max_length=200, null=True, blank=True)
    RegisteredAgentAddress2 = models.CharField(max_length=200, null=True, blank=True)
    RegisteredAgentCity = models.CharField(max_length=200, null=True, blank=True)
    RegisteredAgentState = models.CharField(max_length=200, null=True, blank=True)
    RegisteredAgentZip = models.CharField(max_length=200, null=True, blank=True)
    LocationName = models.CharField(max_length=200, null=True, blank=True)
    LocationAddress1 = models.CharField(max_length=200, null=True, blank=True)
    LocationAddress2 = models.CharField(max_length=200, null=True, blank=True)
    LocationCity = models.CharField(max_length=200, null=True, blank=True)
    LocationState = models.CharField(max_length=200, null=True, blank=True)
    LocationZip = models.CharField(max_length=200, null=True, blank=True)
