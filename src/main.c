#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <samd21.h>
#include <samd21g18a.h>

//This is the D13 red LED on a Metro M0 Express.
#define BLINKY_LED PORT_PA17

int main() {
  SystemInit(); //from system_samd21.c
  //PA0 blinky)
  PORT->Group[0].DIR.reg |= BLINKY_LED;
  PORT->Group[0].OUTTGL.reg |= BLINKY_LED;
  while (1){
	    PORT->Group[0].OUT.reg |= BLINKY_LED;
		//cpu-burning NOP delay loop. system startup code leaves 
		//clock at default 1MHz. might need to adapt the 500k iteration number 
		//(or use SysTick).
		for(volatile long i=0; i < 500000L; i++) {}
	    PORT->Group[0].OUT.reg &= ~BLINKY_LED; //could also use .OUTCLR.reg |= BLINKY_LED
  }; 
  return 0;
}
