# pio-baremetal-atmel-cmsis

## Description

Uses the available framework-cmsis(-atmel) packages to create a baremetal project in which the device headers for an Arduino Due are available.

The project is currently hardcoded to for the sam3x8e chip.

## Compilation

A verbose compilation should show that the project's source files (`src/main.c`) along with the (Atmel-)CMSIS files `startup_sam3xa.c` and `system_sam3xa.c` are compiled.

Also, the linker script `sam3x8e_flash.ld` is used. To use the SRAM script, change it in `build_atmel_cmsis.py` to `sam3x8e_sram.ld` accordingly.

**Pay attention** to bootloaders on the chip -- the project is setup to take over the whole flash, overwriting a potential bootloader. Make sure you know what you're doing or have SWD capable debug probe (such as a ST-Link) ready to reflash the bootloader via SWD (easily possible with the Arduino IDE) in case it is overwritten.

```
$ pio run -v
Processing due (platform: atmelsam; board: due; platform_packages: framework-cmsis-atmel, framework-cmsis; extra_scripts: pre:build_atmel_cmsis.py)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CONFIGURATION: https://docs.platformio.org/page/boards/atmelsam/due.html
PLATFORM: Atmel SAM (6.1.0) > Arduino Due (Programming Port)
HARDWARE: AT91SAM3X8E 84MHz, 96KB RAM, 512KB Flash
DEBUG: Current (atmel-ice) External (atmel-ice, blackmagic, jlink, stlink)
PACKAGES: 
 - framework-cmsis 2.50700.210515 (5.7.0) 
 - framework-cmsis-atmel 1.2.2 
 - toolchain-gccarmnoneeabi 1.70201.0 (7.2.1)
LDF: Library Dependency Finder -> http://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 0 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
arm-none-eabi-gcc -o .pio/build/due/FrameworkCMSIS/as_gcc/startup_sam3xa.o -c -std=gnu11 -Os -ffunction-sections -fdata-sections -Wall -mthumb -nostdlib --param max-inline-insns-single=500 -mcpu=cortex-m3 -D_SAM3XA_SMC_INSTANCE_ -D_SAM3XA_PIOC_INSTANCE_ -D_SAM3XA_PIOD_INSTANCE_ -D_SAM3XA_USART3_INSTANCE_ -D_SAM3XA_TC2_INSTANCE_ -D_SAM3XA_EMAC_INSTANCE_ -DF_CPU=84000000L -DUSBCON -DPLATFORMIO=50200 -D__SAM3X8E__ -DARDUINO_SAM_DUE -I/home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL -I/home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL/sam3xa/include -I/home/max/.platformio/packages/framework-cmsis/CMSIS/Core/Include /home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL/sam3xa/source/as_gcc/startup_sam3xa.c
arm-none-eabi-gcc -o .pio/build/due/FrameworkCMSIS/system_sam3xa.o -c -std=gnu11 -Os -ffunction-sections -fdata-sections -Wall -mthumb -nostdlib --param max-inline-insns-single=500 -mcpu=cortex-m3 -D_SAM3XA_SMC_INSTANCE_ -D_SAM3XA_PIOC_INSTANCE_ -D_SAM3XA_PIOD_INSTANCE_ -D_SAM3XA_USART3_INSTANCE_ -D_SAM3XA_TC2_INSTANCE_ -D_SAM3XA_EMAC_INSTANCE_ -DF_CPU=84000000L -DUSBCON -DPLATFORMIO=50200 -D__SAM3X8E__ -DARDUINO_SAM_DUE -I/home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL -I/home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL/sam3xa/include -I/home/max/.platformio/packages/framework-cmsis/CMSIS/Core/Include /home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL/sam3xa/source/system_sam3xa.c
arm-none-eabi-gcc -o .pio/build/due/src/main.o -c -std=gnu11 -Os -ffunction-sections -fdata-sections -Wall -mthumb -nostdlib --param max-inline-insns-single=500 -mcpu=cortex-m3 -D_SAM3XA_SMC_INSTANCE_ -D_SAM3XA_PIOC_INSTANCE_ -D_SAM3XA_PIOD_INSTANCE_ -D_SAM3XA_USART3_INSTANCE_ -D_SAM3XA_TC2_INSTANCE_ -D_SAM3XA_EMAC_INSTANCE_ -DF_CPU=84000000L -DUSBCON -DPLATFORMIO=50200 -D__SAM3X8E__ -DARDUINO_SAM_DUE -Iinclude -Isrc -I/home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL -I/home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL/sam3xa/include -I/home/max/.platformio/packages/framework-cmsis/CMSIS/Core/Include src/main.c
arm-none-eabi-gcc -o .pio/build/due/firmware.elf -T sam3x8e_flash.ld --specs=nosys.specs --specs=nano.specs -Os -mthumb -Wl,--gc-sections -Wl,--check-sections -Wl,--unresolved-symbols=report-all -Wl,--warn-common -Wl,--warn-section-align -mcpu=cortex-m3 .pio/build/due/FrameworkCMSIS/as_gcc/startup_sam3xa.o .pio/build/due/FrameworkCMSIS/system_sam3xa.o .pio/build/due/src/main.o -L.pio/build/due -L/home/max/.platformio/packages/framework-cmsis-atmel/CMSIS/Device/ATMEL/sam3xa/source/as_gcc -Wl,--start-group -lc -lgcc -lm -lm -Wl,--end-group
MethodWrapper(["checkprogsize"], [".pio/build/due/firmware.elf"])
Advanced Memory Usage is available via "PlatformIO Home > Project Inspect"
RAM:   [          ]   0.0% (used 28 bytes from 98304 bytes)
Flash: [          ]   0.1% (used 532 bytes from 524288 bytes)
.pio/build/due/firmware.elf  :
section           size        addr
.text              532      524288
.relocate            0   536870912
.bss                28   536870912
.stack            1028   536870940
.heap              512   536871968
.ARM.attributes     41           0
.comment           126           0
.debug_frame        44           0
Total             2311
arm-none-eabi-objcopy -O binary .pio/build/due/firmware.elf .pio/build/due/firmware.bin
============================================================================================ [SUCCESS] Took 0.80 seconds ============================================================================================
```

## Uploading

Choose one of the available upload methods at https://docs.platformio.org/en/latest/boards/atmelsam/due.html#uploading. 

You should prefer using a SWD-capable probe, as that can also be used for live-debugging (and you can ignore the bootloader stuff)
