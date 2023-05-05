"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa6767avj5o4899h2g-a.oregon-postgres.render.com",
        database="todo_uugf",
        user="root",
        password="UhoWXinxp2X4BkNgL6FyHAY21W60cIdO")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
