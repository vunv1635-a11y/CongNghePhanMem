from infrastructure.databases.mssql import init_mssql
from infrastructure.models import user_model, medical_info_model, ai_result_model, analysis_model, clinic_model, doctor_model, doctor_note_model, image_model, payment_model, risk_model, subscription_model
def init_db(app): 
    init_mssql(app)
    
from infrastructure.databases.mssql import Base