import os
from supabase import create_client

def database_connect():
    url = os.environ.get("https://amddqcbkilnmquaudlzu.supabase.co")
    key = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFtZGRxY2JraWxubXF1YXVkbHp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjEyMDY0MTMsImV4cCI6MjAzNjc4MjQxM30.V_OAckK_eyeHInbQVpweyAynjWvgK81yNmggDSJfTAM")

    if not url or not key:
        raise ValueError("Supabase URL and key must be provided in environment variables.")

    supabase = create_client(url, key)
    return supabase
