import pandas as pd
from config import OUTPUT_FILE

def export_to_csv(data):
    df = pd.DataFrame([item.dict() for item in data])
    df.to_csv(OUTPUT_FILE, index=False)
