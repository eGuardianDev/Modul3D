<h1 align="center">
Modul3D
</h1>

#### I will try to create a machine with diffrent modules that will allow it to 3d print / cnc cut / make pcbs and other things.
#### The system has custom stepper drivers that are open source and creaded by me. They still need some updates. 

## Current state
#### Most of the machine works, but there is only one module for drawing. Files can be uploaded and G-code can be send. The main computer still needs to be added and connected. The front end is ugly and doesn't scale well with phones.

## To do:
====
Phase one -> 2D implementation
- [X] Build first driver
- [X] Test first driver
- [X] Implement server logic
- [X] Build second driver
- [X] Test second driver
- [X] Add first G-code implementations
- [ ] Add drawing sharpie and test some G-code

====
Phase two -> 3D axis implementations
- [ ] Build 3d Axis
  - [X] Build driver
  - [X] Build hardware
  - [ ] Add bed

====
Phase three -> Building modules
- [ ] Build the modules
  - [X] Make the first module (Pen module)
  - [ ] Make the second module (3D-printing module)
  - [ ] Make the third module (C.N.C module)

====
Phase four -> User experience
- [ ] Back end
  - [ ] Implement more G-Code
  - [X] Add file upload
  - [ ] Make Logs
- [ ] Front end
  - [X] Add uploading files
  - [ ] Add camera
  - [ ] Last executed G-Code
  - [ ] Logs

---
# Driver 
=======
There is a seperate repo for  the stepper driver  [https://github.com/eGuardianDev/AtmegaStepperDriver](here).