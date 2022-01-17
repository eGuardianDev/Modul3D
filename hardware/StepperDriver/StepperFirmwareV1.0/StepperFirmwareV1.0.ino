#define delayTime 599

#define g1 5 //gate 1 pin
#define g2 6 //gate 2 pin
#define g3 7 //gate 3 pin
#define g4 8 //gate 4 pin

#define msp 4//make step pin
#define crp 3//choose rotation pin
//low -> clock wise 
//high -> counter clock wise
#define cp 2//comunication pin

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
        digitalWrite(g1,HIGH);
        delay(delayTime);
        digitalWrite(g1,LOW);
        break;
        case 2:
        digitalWrite(g2,HIGH);
        delay(delayTime);
        digitalWrite(g2,LOW);
        break;
        case 3:
        digitalWrite(g3,HIGH);
        delay(delayTime);
        digitalWrite(g3,LOW);
        break;
        case 4:
        digitalWrite(g4,HIGH);
        delay(delayTime);
        digitalWrite(g4,LOW);
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
      if(rotationState < 1){
        rotationState =4;
      }else if(rotationState >4){
        rotationState =1;
      }
      Serial.println("stepping");
      Serial.println(rotationState);
    }else if(digitalRead(msp) == LOW && locked == true){
      locked = false;
    }
  }
}
void loop(){
}
