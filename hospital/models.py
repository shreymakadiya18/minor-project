from django.db import models
from django.contrib.auth.models import User

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Doctor(models.Model):
    # doctorId = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)


symptomps_types = [
    ('None','None'),
    ('itching','itching'),
    ('skin_rash','skin_rash'),
    ('nodal_skin_eruptions','nodal_skin_eruptions'),
    ('continuous_sneezing','continuous_sneezing'),
    ('shivering','shivering'),
    ('chills','chills'),
    ('joint_pain','joint_pain'),
    ('stomach_pain','stomach_pain'),
    ('acidity','acidity'),
    ('ulcers_on_tongue','ulcers_on_tongue'),
    ('muscle_wasting','muscle_wasting'),
    ('vomiting','vomiting'),
    ('burning_micturition','burning_micturition'),
    ('spotting_ urination','spotting_ urination'),
    ('fatigue','fatigue'),
    ('weight_gain','weight_gain'),
    ('anxiety','anxiety'),
    ('cold_hands_and_feets','cold_hands_and_feets'),
    ('mood_swings','mood_swings'),
    ('weight_loss','weight_loss'),
    ('restlessness','restlessness'),
    ('lethargy','lethargy'),
    ('patches_in_throat','patches_in_throat'),
    ('irregular_sugar_level','irregular_sugar_level'),
    ('cough','cough'),
    ('high_fever','high_fever'),
    ('sunken_eyes','sunken_eyes'),
    ('breathlessness','breathlessness'),
    ('sweating','sweating'),
    ('dehydration','dehydration'),
    ('indigestion','indigestion'),
    ('headache','headache'),
    ('yellowish_skin','yellowish_skin'),
    ('dark_urine','dark_urine'),
    ('nausea','nausea'),
    ('loss_of_appetite','loss_of_appetite'),
    ('pain_behind_the_eyes','pain_behind_the_eyes'),
    ('back_pain','back_pain'),
    ('constipation','constipation'),
    ('abdominal_pain','abdominal_pain'),
    ('diarrhoea','diarrhoea'),
    ('mild_fever','mild_fever'),
    ('yellow_urine','yellow_urine'),
    ('yellowing_of_eyes','yellowing_of_eyes'),
    ('acute_liver_failure','acute_liver_failure'),
    ('fluid_overload','fluid_overload'),
    ('swelling_of_stomach','swelling_of_stomach'),
    ('swelled_lymph_nodes','swelled_lymph_nodes'),
    ('malaise','malaise'),
    ('blurred_and_distorted_vision','blurred_and_distorted_vision'),
    ('phlegm','phlegm'),
    ('throat_irritation','throat_irritation'),
    ('redness_of_eyes','redness_of_eyes'),
    ('sinus_pressure','sinus_pressure'),
    ('runny_nose','runny_nose'),
    ('congestion','congestion'),
    ('chest_pain','chest_pain'),
    ('weakness_in_limbs','weakness_in_limbs'),
    ('fast_heart_rate','fast_heart_rate'),
    ('pain_during_bowel_movements','pain_during_bowel_movements'),
    ('pain_in_anal_region','pain_in_anal_region'),
    ('bloody_stool','bloody_stool'),
    ('irritation_in_anus','irritation_in_anus'),
    ('neck_pain','neck_pain'),
    ('dizziness','dizziness'),
    ('cramps','cramps'),
    ('bruising','bruising'),
    ('obesity','obesity'),
    ('swollen_legs','swollen_legs'),
    ('swollen_blood_vessels','swollen_blood_vessels'),
    ('puffy_face_and_eyes','puffy_face_and_eyes'),
    ('enlarged_thyroid','enlarged_thyroid'),
    ('brittle_nails','brittle_nails'),
    ('swollen_extremeties','swollen_extremeties'),
    ('excessive_hunger','excessive_hunger'),
    ('extra_marital_contacts','extra_marital_contacts'),
    ('drying_and_tingling_lips','drying_and_tingling_lips'),
    ('slurred_speech','slurred_speech'),
    ('knee_pain','knee_pain'),
    ('hip_joint_pain','hip_joint_pain'),
    ('muscle_weakness','muscle_weakness'),
    ('stiff_neck','stiff_neck'),
    ('swelling_joints','swelling_joints'),
    ('movement_stiffness','movement_stiffness'),
    ('spinning_movements','spinning_movements'),
    ('loss_of_balance','loss_of_balance'),
    ('unsteadiness','unsteadiness'),
    ('weakness_of_one_body_side','weakness_of_one_body_side'),
    ('loss_of_smell','loss_of_smell'),
    ('bladder_discomfort','bladder_discomfort'),
    ('foul_smell_of urine','foul_smell_of urine'),
    ('continuous_feel_of_urine','continuous_feel_of_urine'),
    ('passage_of_gases','passage_of_gases'),
    ('internal_itching','internal_itching'),
    ('toxic_look_(typhos)','toxic_look_(typhos)'),
    ('depression','depression'),
    ('irritability','irritability'),
    ('muscle_pain','muscle_pain'),
    ('altered_sensorium','altered_sensorium'),
    ('red_spots_over_body','red_spots_over_body'),
    ('belly_pain','belly_pain'),
    ('abnormal_menstruation','abnormal_menstruation'),
    ('dischromic _patches','dischromic _patches'),
    ('watering_from_eyes','watering_from_eyes'),
    ('increased_appetite','increased_appetite'),
    ('polyuria','polyuria'),
    ('family_history','family_history'),
    ('mucoid_sputum','mucoid_sputum'),
    ('rusty_sputum','rusty_sputum'),
    ('lack_of_concentration','lack_of_concentration'),
    ('visual_disturbances','visual_disturbances'),
    ('receiving_blood_transfusion','receiving_blood_transfusion'),
    ('receiving_unsterile_injections','receiving_unsterile_injections'),
    ('coma','coma'),
    ('stomach_bleeding','stomach_bleeding'),
    ('distention_of_abdomen','distention_of_abdomen'),
    ('history_of_alcohol_consumption','history_of_alcohol_consumption'),
    ('fluid_overload','fluid_overload'),
    ('blood_in_sputum','blood_in_sputum'),
    ('prominent_veins_on_calf','prominent_veins_on_calf'),
    ('palpitations','palpitations'),
    ('painful_walking','painful_walking'),
    ('pus_filled_pimples','pus_filled_pimples'),
    ('blackheads','blackheads'),
    ('scurring','scurring'),
    ('skin_peeling','skin_peeling'),
    ('silver_like_dusting','silver_like_dusting'),
    ('small_dents_in_nails','small_dents_in_nails'),
    ('inflammatory_nails','inflammatory_nails'),
    ('blister','blister'),
    ('red_sore_around_nose','red_sore_around_nose'),
    ('yellow_crust_ooze','yellow_crust_ooze')
]

class Patient(models.Model):
    # patientId = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptom1 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    symptom2 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    symptom3 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    symptom4 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    symptom5 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptom1+","+self.symptom2+","+self.symptom3+","+self.symptom4+","+self.symptom5+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    # patientId=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptom1 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    symptom2 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    symptom3 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    symptom4 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")
    symptom5 = models.CharField(max_length=100,choices=symptomps_types,null=False,default="None")

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


