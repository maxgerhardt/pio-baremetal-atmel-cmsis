Import("env")
from os.path import join

pio_platform = env.PioPlatform()
atmel_cmsis_dir = pio_platform.get_package_dir("framework-cmsis-atmel")
cmsis_dir = pio_platform.get_package_dir("framework-cmsis")

env.Append(
  CPPPATH=[
    join(atmel_cmsis_dir, "CMSIS", "Device", "ATMEL"),
    join(atmel_cmsis_dir, "CMSIS", "Device", "ATMEL", "sam3xa", "include"), #conviennce for our chip
    join(cmsis_dir, "CMSIS", "Core", "Include"),
  ],
  LINKFLAGS=["--specs=nosys.specs", "--specs=nano.specs"]
)

# link against libmath (implicit at the end), libc, libgcc
env.Replace(
   LIBS=["c", "gcc", "m", "stdc++"]
)

# fix linkerscript
# also SRAM linker script available
env.Append(LIBPATH=[join(atmel_cmsis_dir, "CMSIS", "Device", "ATMEL", "sam3xa", "source", "as_gcc")])
env.Replace(LDSCRIPT_PATH ="sam3x8e_flash.ld")

# build startup file
# for that we additionally need to define macros that tell it what peripherals we have.. sadly not implied automatically
env.Append(
  CPPDEFINES= [
     "_SAM3XA_SMC_INSTANCE_",
     "_SAM3XA_PIOC_INSTANCE_",
     "_SAM3XA_PIOD_INSTANCE_",
     "_SAM3XA_USART3_INSTANCE_",
     "_SAM3XA_TC2_INSTANCE_",
     "_SAM3XA_EMAC_INSTANCE_"
 ]
)

# build system file (starts up clocks) and startup file (contains interrupt vector table)
system_file_dir = join(atmel_cmsis_dir, "CMSIS", "Device", "ATMEL", "sam3xa", "source")
system_file_dir_filter = "-<*> +<system_sam3xa.c> +<as_gcc/startup_sam3xa.c>"
env.BuildSources(join("$BUILD_DIR", "FrameworkCMSIS"), system_file_dir, src_filter=system_file_dir_filter)
