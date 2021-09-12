Import("env")
from os.path import join

pio_platform = env.PioPlatform()
atmel_cmsis_dir = pio_platform.get_package_dir("framework-cmsis-atmel")
cmsis_dir = pio_platform.get_package_dir("framework-cmsis")
board_config = env.BoardConfig()

env.Append(
  CPPPATH=[
    join(atmel_cmsis_dir, "CMSIS", "Device", "ATMEL"),
    join(atmel_cmsis_dir, "CMSIS", "Device", "ATMEL", "samd21", "include"), #conviennce for our chip
    join(cmsis_dir, "CMSIS", "Core", "Include"),
  ],
#  LINKFLAGS=["--specs=nano.specs"]
)

print("Linkflags")
print(env["LINKFLAGS"])

# link against libmath (implicit at the end), libc, libgcc
env.Replace(
   LIBS=["c", "gcc", "m", "stdc++"]
)

# fix linkerscript
# also SRAM linker script available
env.Append(LIBPATH=[join(atmel_cmsis_dir, "CMSIS", "Device", "ATMEL", "samd21", "source", "as_gcc")])
if not board_config.get("build.ldscript", ""):
    env.Replace(LDSCRIPT_PATH ="samd21g18a_flash.ld")

# build system file (starts up clocks) and startup file (contains interrupt vector table)
system_file_dir = join(atmel_cmsis_dir, "CMSIS", "Device", "ATMEL", "samd21", "source")
system_file_dir_filter = "-<*> +<system_samd21.c> +<as_gcc/startup_samd21.c>"
env.BuildSources(join("$BUILD_DIR", "FrameworkCMSIS"), system_file_dir, src_filter=system_file_dir_filter)
