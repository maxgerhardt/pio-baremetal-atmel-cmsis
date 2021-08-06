#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sam3x8e.h>
#include <sam3.h>
#include <component/pio.h>

int main() {
  //blackmagic-incantation for PIO (basically GPIO here) blinky
  //this is untested, probably not working -- just to illustrate that
  //peripherals are accessible.
  //PA0 as output (output enable register)
  PIOA->PIO_OER |= (1 << 0);

  return 0;
}
