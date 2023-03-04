
#include <Servo.h>  
#include <AFMotor.h>

Servo s1;


#define nov 5
#define digitspervalue 1
#define Speed 150

int valRec[nov];
int stringLength = nov*digitspervalue +1;
int counter = 0;
bool counterStart = false;
String receivedString;

Servo servo_motor; 
AF_DCMotor motor1(2);
AF_DCMotor motor2(3);
void setup(){
  Serial.begin(9600); 
  motor1.setSpeed(Speed);
  motor2.setSpeed(Speed);
  s1.attach(10);
  Stop();
  s1.write(90);
  delay(800);
  s1.write(0);
  delay(800);
}

void receieveData(){
  while(Serial.available())
  {
    char c = Serial.read();

    if (c=='$'){
      counterStart = true;
    }
    if(counterStart)
      if(counter<stringLength)
      {
        receivedString = String(receivedString+c);
        counter++;
      }
      if(counter>=stringLength)
      {
        for(int i=0;i<nov;i++)
        {
          int num = (i*digitspervalue)+1;
          valRec[i]=receivedString.substring(num,num+digitspervalue).toInt();
        }
        receivedString ="";
        counter=0;
        counterStart = false;     
      }
  }
}

void loop(){
  receieveData();
  for(int i=0;i<nov;i++)
        {
          Serial.print(" ");
          Serial.print(valRec[i]);
        }
  if(valRec[0]== 1 && valRec[1]== 1){forward();}
  if(valRec[0]== 1 && valRec[1]== 0){left();}
  if(valRec[0]== 0 && valRec[1]== 1){right();}
  if(valRec[0]== 0 && valRec[1]== 0 && valRec[2]== 0 ){Stop();}
  if(valRec[0]== 0 && valRec[1]== 0 && valRec[2]== 1 ){
    Stop();
    pick();
    }
  for(int i=0;i<nov;i++)
        {
          valRec[i]=0;
        }
  delay(10);
  Stop();
}

void forward() {
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
}
void left() {
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
}
void right() {
  
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
}
void Stop() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}
void backward(){
    motor1.run(FORWARD);
    motor2.run(FORWARD);
}
void forwardpost(){
  motor1.setSpeed(100);
  motor2.setSpeed(100);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  delay(400);
  Stop();
  motor1.setSpeed(Speed);
  motor2.setSpeed(Speed);
  
}
void pick(){
  forwardpost();
  s1.write(150);
  delay(500);
  right();
  delay(440);
  Stop();
  forward();
  delay(1000);
  Stop();
  }
