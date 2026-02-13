import pandas as pd
import io

from .db import supabase


def fetch_publications_master():
   
    res = (
        supabase
        .table("publications_master")
        .select("*")
        .order("id", desc=False)
        .execute()
    )
    return res.data




def generate_publications_excel():
    data = fetch_publications_master()
    df = pd.DataFrame(data)

    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)

    return buffer
