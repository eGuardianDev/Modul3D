#define speeed 2

#define SteppingPin 9
#define RotationPin 10
#define ReadyComPin 11
void setup() {
  //ALL ON
  //==========
  pinMode(8, OUTPUT); //gate 1
  pinMode(7, OUTPUT); //gate 2
  pinMode(6, OUTPUT); //gate 3
  pinMode(5, OUTPUT); //gate 4

  pinMode(SteppingPin, INPUT); //Read Steps
  pinMode(RotationPin, INPUT); //Read Rotation
  pinMode(ReadyComPin, OUTPUT);//Tell main driver to be ready
  
  int state = 1; // which step to activate
  int rotate = 100; // beginning steps // to remove
  bool unlocked = false; // protection for stop stepping the same pin
  int stepLock = false;  // Locking the steps so we can send pulsing signals to tell the driver how many steps to make ( 1 pulse = 1 step )
  while (true) {
  int stepping = digitalRead(9);
  if(stepping == HIGH && stepLock == false){
    stepLock = true; 
      rotate+=1;
    unlocked = true;  
    digitalWrite(ReadyComPin, HIGH);
  }else if (stepping == LOW && stepLock == true){
    stepLock = false;
  //  digitalWrite(10,LOW);
  }
    
    if(rotate > 0){
      rotate--;
      if ((PINB&(1<<4))){
      state++;
      }else{
        state--;
      }     
      unlocked = true;
    }

    // protection against out of range steps
    if (state > 4) {
      state = 1;
    } else if (state < 1) {
      state = 4;
    }

    // doing the steps lol
    if (unlocked == true) {
      switch (state) {
        case 1:
          //one step
          PORTB = B00000001;
          PORTD = B01000000;
          delay(speeed * 2);
          PORTB = B00000000;
          PORTD = B00000000;
          break;

        case 2:
          //two steps
          PORTB = B00000000;
          PORTD = B11000000;
          delay(speeed * 2);
          PORTB = B00000000;
          PORTD = B00000000;         
          break;

          
        case 3:
          //thre steps
          PORTB = B00000000;
          PORTD = B10100000;
          delay(speeed * 2);
          PORTB = B00000000;
          PORTD = B00000000;
          break;

          
        case 4:
          //foursteps
          PORTB = B00000001;
          PORTD = B00100000;
          delay(speeed * 2 );
          PORTB = B00000000;
          PORTD = B00000000;
          break;

      }//siwtch end
      //locking the step and setting signal that is ready for another step
    unlocked = false;
    digitalWrite(11,LOW);
    }//if end
  }
}
