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
	PORT->Group[0].DIR.reg = BLINKY_LED;
	PORT->Group[0].OUTTGL.reg = BLINKY_LED;
	while (1)
	{
		//to toggle the LED, we use the convenient OUTTGL register.
		PORT->Group[0].OUTTGL.reg |= BLINKY_LED;
		//coud also use..
		//PORT->Group[0].OUTSET.reg |= BLINKY_LED;
		//PORT->Group[0].OUT.reg &= ~BLINKY_LED;
		//PORT->Group[0].OUTCLR.reg |= BLINKY_LED
		//cpu-burning NOP delay loop. system startup code leaves
		//clock at default 1MHz. might need to adapt the 500k iteration number
		//(or use SysTick).
		//increase number significantly if bootloader has setup clock to be faster
		for (volatile long i = 0; i < 50000L; i++) { }
	};
	return 0;
}
