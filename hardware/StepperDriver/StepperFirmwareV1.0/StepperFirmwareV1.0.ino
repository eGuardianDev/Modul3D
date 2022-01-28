#define delayTime 5

#define g1 5 //gate 1 pin
#define g2 6 //gate 2 pin
#define g3 7 //gate 3 pin
#define g4 8 //gate 4 pin

#define msp 9//make step pin
#define crp 10//choose rotation pin
//low -> clock wise 
//high -> counter clock wise
#define cp 11//comunication pin
int incommingByte = 0;
void setup() {
  pinMode(g1, OUTPUT);
  pinMode(g2, OUTPUT);
  pinMode(g3, OUTPUT);
  pinMode(g4, OUTPUT);

  pinMode(msp, INPUT);
  pinMode(crp, INPUT);
  pinMode(cp, OUTPUT);
  Serial.begin(9600);
  int rotationState = 0;
  bool updated = false;
  bool locked = false; //used to not make more than one step per 'msp request'
  while(true){
    if(updated==false){ 
      switch(rotationState){
        case 1:
  PORTB = B00000001;
  PORTD = B01000000;
        delay(delayTime);
  PORTB = B00000000;
  PORTD = B00000000;
        break;
        case 2:
  PORTB = B00000000;
  PORTD = B11000000;
        delay(delayTime);
  PORTB = B00000000;
  PORTD = B00000000;
        break;
        case 3:
  PORTB = B00000000;
  PORTD = B10100000;
        delay(delayTime);
  PORTB = B00000000;
  PORTD = B00000000;
        break;
        case 4:
  PORTB = B00000001;
  PORTD = B00100000;
        delay(delayTime);
  PORTB = B00000000;
  PORTD = B00000000;
        break;  
      }
      updated = true;
    }
    if(digitalRead(msp) == HIGH && locked == false){
      updated = false;
      locked = true;
      if(digitalRead(crp) == LOW){
        rotationState++;
      }else if(digitalRead(crp) == HIGH)
      {
          rotationState--;
      }
      Serial.println("stepping");
    }else if(digitalRead(msp) == LOW && locked == true){
      locked = false;
    }
      if(rotationState < 1){
        rotationState =4;
      }else if(rotationState >4){
        rotationState =1;
      }
      Serial.println(rotationState);
  }
}
void loop(){
}
