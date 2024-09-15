import time
import RPi.GPIO as GPIO

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

p1 = GPIO.PWM(4, 50)
p2 = GPIO.PWM(17, 50)

p1.start(0.0)
p2.start(0.0)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
  return "It's working"


@app.get("/open")
async def get_open():
  p1.ChangeDutyCycle(2.5)
  p2.ChangeDutyCycle(2.5)
  return "ok"

@app.get("/close")
async def get_close():
  p1.ChangeDutyCycle(6)
  p2.ChangeDutyCycle(6)
  return "ok"

