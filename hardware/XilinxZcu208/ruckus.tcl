# Load RUCKUS environment and library
source -quiet $::env(RUCKUS_DIR)/vivado_proc.tcl

# Check for valid FPGA
if { $::env(PRJ_PART) != "XCZU48DR-FSVG1517-2-E" } {
   puts "\n\nERROR: PRJ_PART must be either XCZU48DR-FSVG1517-2-E in the Makefile\n\n"; exit -1
}

# Load shared source code
loadRuckusTcl "$::DIR_PATH/../../shared"
loadConstraints -dir "$::DIR_PATH/xdc"
loadSource -lib axi_soc_ultra_plus_core -dir "$::DIR_PATH/rtl"

# Set the board part
set_property board_part xilinx.com:zcu208:part0:2.0 [current_project]

# Load the block design
if { $::env(VIVADO_VERSION) >= 2022.1 } {
   loadBlockDesign -path "$::DIR_PATH/bd/2022.1/AxiSocUltraPlusCpuCore.bd"
   # loadBlockDesign -path "$::DIR_PATH/bd/2022.1/AxiSocUltraPlusCpuCore.tcl"
} else {
   loadBlockDesign -path "$::DIR_PATH/bd/2021.2/AxiSocUltraPlusCpuCore.bd"
   # loadBlockDesign -path "$::DIR_PATH/bd/2021.2/AxiSocUltraPlusCpuCore.tcl"
}
