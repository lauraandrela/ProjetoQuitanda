from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql
import uuid

app = Flask(__name__)
app.secret_key "quitandazezinho"

usuario = "usuario"
senha = "senha"
login = False